import os
import requests
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms.base import LLM
from typing import Optional, List, Dict, Any

# Базовый словарь для перевода русских команд
RUSSIAN_COMMAND_MAPPING = {
    "список файлов": "ls",
    "показать файлы": "ls",
    "создать папку": "mkdir",
    "удалить папку": "rmdir", 
    "перейти в папку": "cd",
    "текущая папка": "pwd",
    "копировать файл": "cp",
    "переместить файл": "mv",
    "удалить файл": "rm",
    "показать содержимое": "cat",
    "поиск в файле": "grep",
    "изменить разрешение": "chmod",
    "показать процессы": "ps",
    "завершить процесс": "kill",
    "сетевые соединения": "netstat",
    "проверить связь": "ping",
    "скачать файл": "wget",
    "распаковать архив": "tar -xzf",
    "создать архив": "tar -czf",
    "показать историю": "history",
    "очистить экран": "clear"
}

class YandexGPT(LLM):
    """Кастомная реализация для Yandex GPT"""
    
    def __init__(self, folder_id: str, api_key: str, temperature: float = 0):
        super().__init__()
        self.folder_id = folder_id
        self.api_key = api_key
        self.temperature = temperature
        self.url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.api_key}",
            "x-folder-id": self.folder_id
        }
        
        data = {
            "modelUri": f"gpt://{self.folder_id}/yandexgpt/latest",
            "completionOptions": {
                "temperature": self.temperature,
                "maxTokens": 1000
            },
            "messages": [
                {
                    "role": "system",
                    "text": "Ты помогаешь преобразовывать русские команды в команды терминала. Отвечай только командой."
                },
                {
                    "role": "user", 
                    "text": prompt
                }
            ]
        }
        
        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            result = response.json()
            return result['result']['alternatives'][0]['message']['text']
        except Exception as e:
            return f"Ошибка Yandex GPT: {str(e)}"
    
    @property
    def _llm_type(self) -> str:
        return "yandex-gpt"

def enhance_command_mapping():
    """Улучшенное сопоставление команд с поддержкой русского языка"""
    template = """
    Пользователь просит выполнить действие на русском языке. Преобразуй это в команду терминала.
    
    Примеры преобразования:
    - "покажи файлы в текущей папке" -> "ls"
    - "создай папку с именем проект" -> "mkdir проект"
    - "покажи какие процессы работают" -> "ps aux"
    - "заверши процесс с id 123" -> "kill 123"
    
    Запрос: {query}
    
    Верни ТОЛЬКО команду терминала без каких-либо пояснений.
    Если запрос непонятен или не может быть преобразован в команду, верни "ERROR: Неизвестная команда".
    
    Команда:
    """
    
    prompt = PromptTemplate(
        input_variables=["query"],
        template=template
    )
    
    return prompt

def detect_language(text):
    """Определяет язык текста"""
    russian_chars = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    text_lower = text.lower()
    russian_count = sum(1 for char in text_lower if char in russian_chars)
    total_letters = sum(1 for char in text_lower if char.isalpha())
    
    if total_letters == 0:
        return 'english'
    
    if russian_count / total_letters > 0.3:
        return 'russian'
    return 'english'

def get_command_from_russian(russian_command, yandex_api_key, yandex_folder_id):
    """Получает команду из русского текста используя Yandex GPT"""
    # Сначала проверяем базовые команды
    cmd_lower = russian_command.lower().strip()
    for ru_cmd, en_cmd in RUSSIAN_COMMAND_MAPPING.items():
        if ru_cmd in cmd_lower:
            # Пытаемся извлечь аргументы
            if ru_cmd != cmd_lower:
                args = cmd_lower.replace(ru_cmd, '').strip()
                return f"{en_cmd} {args}"
            return en_cmd
    
    # Если нет в базовом словаре, используем Yandex GPT
    try:
        llm = YandexGPT(folder_id=yandex_folder_id, api_key=yandex_api_key)
        prompt = enhance_command_mapping()
        chain = LLMChain(llm=llm, prompt=prompt)
        result = chain.run(query=russian_command)
        return result.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"
