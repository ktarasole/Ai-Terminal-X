import os
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class RussianLLM:
    """Обертка для русскоязычных моделей с Hugging Face"""
    
    def __init__(self, model_name: str = "sberbank-ai/rugpt3large_based_on_gpt2"):
        self.model_name = model_name
        self.pipeline = None
        self._load_model()
    
    def _load_model(self):
        """Загружает модель"""
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            
            if torch.cuda.is_available():
                self.model = self.model.to('cuda')
                
        except Exception as e:
            print(f"Ошибка загрузки модели: {e}")
            # Резервная модель
            self.model_name = "sberbank-ai/rugpt3small_based_on_gpt2"
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
    
    def generate_response(self, prompt: str, max_length: int = 200) -> str:
        """Генерирует ответ на промпт"""
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            
            if torch.cuda.is_available():
                inputs = {k: v.to('cuda') for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=max_length,
                    num_return_sequences=1,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Убираем промпт из ответа
            if prompt in response:
                response = response.replace(prompt, "").strip()
            
            return response
            
        except Exception as e:
            return f"Ошибка генерации: {str(e)}"

def get_command_with_huggingface(russian_command: str) -> str:
    """Получает команду используя локальную модель"""
    llm = RussianLLM()
    
    prompt = f"""
    Преобразуй русскую команду в команду терминала.
    
    Русская команда: {russian_command}
    
    Верни только команду терминала. Примеры:
    - "показать файлы" -> "ls"
    - "создать папку проект" -> "mkdir проект"
    - "текущая директория" -> "pwd"
    
    Команда терминала:
    """
    
    response = llm.generate_response(prompt)
    
    # Очищаем ответ
    lines = response.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('Русская команда') and not line.startswith('Преобразуй'):
            return line
    
    return "ERROR: Не удалось преобразовать команду"
