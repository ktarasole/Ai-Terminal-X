import os
from command_handler import safe_execute_command
from command_mapping import detect_language

def main():
    print("Добро пожаловать в AI Terminal X с поддержкой русского языка!")
    print("=" * 60)
    print("Вы можете использовать команды на русском или английском языке.")
    print("Примеры русских команд:")
    print("  - 'список файлов' → 'ls'")
    print("  - 'создать папку test' → 'mkdir test'") 
    print("  - 'показать процессы' → 'ps aux'")
    print("  - 'выход' для завершения работы")
    print("=" * 60)
    
    while True:
        try:
            # Получаем команду от пользователя
            user_input = input("\nВведите команду → ").strip()
            
            if not user_input:
                continue
                
            # Проверяем на команды выхода
            if user_input.lower() in ['exit', 'quit', 'выход', 'завершить', 'стоп']:
                print("До свидания!")
                break
                
            # Определяем язык для информационного сообщения
            language = detect_language(user_input)
            if language == 'russian':
                print(f"🔍 Обрабатываю русскую команду: {user_input}")
            else:
                print(f"🔍 Processing English command: {user_input}")
            
            # Выполняем команду
            result = safe_execute_command(user_input)
            
            # Выводим результат
            if result == "exit":
                print("До свидания!")
                break
            elif result:
                print("Результат:")
                print(result)
            else:
                print("Команда выполнена успешно.")
                
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена пользователем.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()
