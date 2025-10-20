import os
from command_handler import CommandHandler
from command_mapping import detect_language

def main():
    print("🇷🇺 Добро пожаловать в AI Terminal X с поддержкой русского языка!")
    print("=" * 60)
    print("Вы можете использовать команды на русском или английском языке.")
    print("\n📋 Примеры русских команд:")
    print("  - 'список файлов' → 'ls'")
    print("  - 'создать папку test' → 'mkdir test'") 
    print("  - 'показать процессы' → 'ps aux'")
    print("  - 'очистить экран' → 'clear'")
    print("  - 'выход' для завершения работы")
    print("=" * 60)
    
    # Настройка модели
    use_yandex = input("Использовать Yandex GPT? (y/n): ").lower().strip() == 'y'
    
    yandex_api_key = None
    yandex_folder_id = None
    
    if use_yandex:
        yandex_api_key = input("Введите Yandex Cloud API Key: ").strip()
        yandex_folder_id = input("Введите Yandex Cloud Folder ID: ").strip()
        print("🔧 Используется Yandex GPT")
    else:
        print("🔧 Используется локальная модель (Hugging Face)")
        print("⏳ Первый запуск может занять время для загрузки модели...")
    
    handler = CommandHandler(
        use_yandex_gpt=use_yandex,
        yandex_api_key=yandex_api_key,
        yandex_folder_id=yandex_folder_id
    )
    
    while True:
        try:
            # Получаем команду от пользователя
            user_input = input("\n💻 Введите команду → ").strip()
            
            if not user_input:
                continue
                
            # Проверяем на команды выхода
            if user_input.lower() in ['exit', 'quit', 'выход', 'завершить', 'стоп']:
                print("👋 До свидания!")
                break
                
            # Определяем язык для информационного сообщения
            language = detect_language(user_input)
            if language == 'russian':
                print(f"🔍 Обрабатываю русскую команду: {user_input}")
            else:
                print(f"🔍 Processing English command: {user_input}")
            
            # Выполняем команду
            result = handler.safe_execute_command(user_input)
            
            # Выводим результат
            if result == "exit":
                print("👋 До свидания!")
                break
            elif result:
                print("📋 Результат:")
                print(result)
            else:
                print("✅ Команда выполнена успешно.")
                
        except KeyboardInterrupt:
            print("\n\n⏹️ Программа завершена пользователем.")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()
