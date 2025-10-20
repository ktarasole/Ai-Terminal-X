import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub

# Добавляем словарь для перевода русских команд
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

def enhance_command_mapping():
    """Улучшенное сопоставление команд с поддержкой русского языка"""
    template = """
    Ты - помощник для преобразования естественного языка в команды терминала.
    Пользователь может давать команды на русском или английском языке.
    
    Доступные команды на русском:
    {russian_commands}
    
    Преобразуй следующий запрос в соответствующую команду терминала.
    Если запрос на русском - сначала переведи на английский, затем найди команду.
    
    Запрос: {query}
    
    Верни ТОЛЬКО команду без объяснений.
    Если не можешь определить команду, верни "ERROR: Unknown command".
    
    Команда:
    """
    
    prompt = PromptTemplate(
        input_variables=["query", "russian_commands"],
        template=template
    )
    
    return prompt

def detect_language(text):
    """Определяет язык текста"""
    russian_chars = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if any(char in russian_chars for char in text.lower()):
        return 'russian'
    return 'english'

def get_command_from_russian(russian_command):
    """Получает команду из русского текста"""
    # Инициализируем модель HuggingFaceHub
    llm = HuggingFaceHub(
        repo_id="IlyaGusev/fred_t5_ru_turbo",
        model_kwargs={"temperature": 0, "max_length": 1000}
    )
    
    prompt = enhance_command_mapping()
    
    russian_commands_list = "\n".join([f"- {ru}: {en}" for ru, en in RUSSIAN_COMMAND_MAPPING.items()])
    
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(query=russian_command, russian_commands=russian_commands_list)
    
    return result.strip()
