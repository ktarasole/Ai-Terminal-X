import subprocess
import os
from command_mapping import get_command_from_russian, detect_language, RUSSIAN_COMMAND_MAPPING
from alternative_models import get_command_with_huggingface

class CommandHandler:
    def __init__(self, use_yandex_gpt=False, yandex_api_key=None, yandex_folder_id=None):
        self.use_yandex_gpt = use_yandex_gpt
        self.yandex_api_key = yandex_api_key
        self.yandex_folder_id = yandex_folder_id
    
    def execute_command(self, command):
        """Выполняет команду и возвращает результат"""
        try:
            # Определяем язык команды
            language = detect_language(command)
            
            # Если команда на русском, преобразуем её
            if language == 'russian':
                print(f"🔄 Обнаружена русская команда: {command}")
                
                if self.use_yandex_gpt and self.yandex_api_key and self.yandex_folder_id:
                    command = get_command_from_russian(
                        command, 
                        self.yandex_api_key, 
                        self.yandex_folder_id
                    )
                else:
                    command = get_command_with_huggingface(command)
                
                print(f"✅ Преобразованная команда: {command}")
            
            # Проверяем базовые русские команды
            cmd_lower = command.lower()
            for ru_cmd, en_cmd in RUSSIAN_COMMAND_MAPPING.items():
                if ru_cmd in cmd_lower and cmd_lower.startswith(ru_cmd):
                    command = command.replace(ru_cmd, en_cmd, 1)
                    break
            
            # Выполняем команду
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                return result.stdout if result.stdout else "Команда выполнена успешно"
            else:
                return f"❌ Ошибка: {result.stderr}"
                
        except Exception as e:
            return f"💥 Исключение: {str(e)}"

    def handle_special_commands(self, command):
        """Обрабатывает специальные команды на русском"""
        special_commands = {
            "помощь": "help",
            "справка": "help", 
            "выход": "exit",
            "завершить": "exit",
            "стоп": "exit",
            "история": "history"
        }
        
        cmd_lower = command.lower().strip()
        if cmd_lower in special_commands:
            return special_commands[cmd_lower]
        
        return None

    def safe_execute_command(self, command):
        """Безопасное выполнение команды с проверкой"""
        # Проверяем специальные команды
        special_cmd = self.handle_special_commands(command)
        if special_cmd:
            return special_cmd
        
        # Выполняем обычную команду
        return self.execute_command(command)

# Глобальный хендлер для обратной совместимости
default_handler = CommandHandler()

def safe_execute_command(command):
    return default_handler.safe_execute_command(command)
