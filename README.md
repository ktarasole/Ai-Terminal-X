## ⚡ AI-Terminal-X  ( AI-powered  Terminal Assistant for **Linux )**

![Logo](img/main.png)

**Developed by:** Muhammad Izaz Haider

Your AI-powered personal terminal assistant for **Linux** (especially Kali Linux).

Order in plain English — and watch real terminal magic happen instantly! 🪄

### 📚 **Introduction**

AI-Terminal-X is **a game-changing AI-Powered Terminal Assistant** designed to revolutionize the way you interact with your Linux terminal. Whether you're a beginner, an ethical hacker, or a seasoned professional, AI-Terminal-X transforms your daily command-line operations, enhancing productivity and learning.

#### [Watch Full Demo on  LinkedIn](https://www.linkedin.com/posts/muhammad-izaz-haider-091639314_alhamdulilah-proud-to-share-my-latest-project-ugcPost-7324760286094065664-dsAJ)

#### [Blog Post](https://medium.com/@the-pentrix/ai-terminal-x-ai-powered-intelligent-linux-command-line-copilot-04629dfaf057)

### 🔥 **A Powerful Combination of**

* **Linux Terminal (XFCE)** – Reliable command execution
* **AI (Google's Gemini AI)** – Intelligent command generation
* **Python** – Seamless integration of components
* **Cybersecurity/Ethical Hacking** – Focused on security tools and commands
* **Prompt Engineering** – Natural language command input
* **Real-Time Execution** – Instant command execution
* **Safety & Control** – Safe, permission-based execution

### 🔐 **What AI-Terminal-X Does**

AI-Terminal-X is powered by  **Google’s Gemini AI** , making it **exceptionally intelligent** and capable of understanding natural language. This tool is specifically built for  **Kali Linux** , but it can work on any Linux-based terminal. With just a few simple commands, **AI-Terminal-X** can instantly generate accurate terminal commands, run them, and explain their functions — all in seconds.

### ✨ **Key Features**

✅ **AI-generated terminal commands** (Kali/Linux optimized)

✅ **No execution without permission** — you control everything

✅  **Dual-window** : AI conversation + command execution

✅ **Command logging** for easy review and reuse

✅ **Simple text input → real, working output**

✅ **Powered by Gemini 1.5 Flash** – Fast, Accurate, Lightweight

✅ **Made for students, pros, researchers, & enthusiasts**

✅ **Command Suggester** — Suggests related commands based on your input

✅ **Multi-layer risk check** to ensure safe execution of commands

✅ **Customizable aliases** for faster command execution

✅ **Interactive Mode** — Review, edit, or cancel commands before execution

✅ **Real-time feedback and explanations** for commands

✅ **Smart back navigation** between different modes

✅ **Command history** to easily reuse previous inputs

✅ **Efficient learning mode** — Ask questions and get beginner-friendly explanations

✅  **Future-proof** : Voice command integration coming soon

✅ **Secure API integration** for smooth operation

✅ **User-friendly interface** for seamless interaction

### 🔥 **LOGO**

![Logo](img/logo.png)

### 🔥 **Built for**

![Logo](img/built-for.png)

### 🔥 **Work-Flow**

![Logo](img/workflow.png)

# 🔧 Installation

### 1: 🔹 Must Install Required Modules

```sh

pip install google-generativeai python-dotenv

```

### 2: 🔹 Clone the Repository

```sh

git clone https://github.com/mizazhaider-ceh/Ai-Terminal-X.git

cd Ai-Terminal-X

```

### 3: 🔹 Run the Setup script & ai-terminal-x script

In terminal:

```sh
chmod +x setup.py

python setup.py

```

After setup.py the run.sh file will automatically create so run below command and everytime you just need to type below command in terminal ..Okay..!

```sh

./run.sh or bash run.sh

```

### 3: 🔹 Enter your Gemini API key ~ when prompted

```sh

Done!🚀

```

## 🛠️ Requirements

* Python 3.8+
* Gemini API Key (Get it [here](https://aistudio.google.com/apikey))

## 🔄 Update Notes for `Ai-Terminal-X`

> 🚀 **Latest Improvements**
>
> * 🐞 **Bug Fixes:** Major installation issues resolved – now easier and smoother to install and run.
> * 🌐 **Multi-language Support:** Now supports multiple languages for a broader user base.
> * ✨More Enhanced Prompt
> * 📝 **Text Input Upgrade:** Fixed the text overlapping issue – now supports multi-line input seamlessly.
> * 💡 **Usability Enhancements:** Improved interface for a more user-friendly experience.

### 🔐 Safety and Permissions

Before running any command, **AI-Terminal-X** checks if the command could potentially be harmful to your system. Here's how it works:

1. **Risk Check** : The system checks whether the command might be dangerous.
2. **Permission Check** : The tool will prompt you to confirm execution if needed, ensuring you approve the actions before anything is run.
3. **Security Safeguards** : Built-in security mechanisms prevent harmful commands from being executed.

### 🛠️ Troubleshooting

If you face issues while using  **AI-Terminal-X** , try the following:

1. **"Command not found" error** : Make sure your Gemini API key is set correctly in the `.env` file.
2. **API key-related errors** : Double-check that you've copied your API key properly and that it's active.

For any other issues, feel free to open an issue in the [GitHub repository](https://github.com/mizazhaider-ceh/Ai-Terminal-X/issues).

## 📚 Example Usage

| Input                                       | Generated Command     |
| ------------------------------------------- | --------------------- |
| `Show my public IP address`               | `curl ifconfig.me`  |
| `List all files in the current directory` | `ls`                |
| `Go to the home directory`                | `cd ~`              |
| `Check disk usage`                        | `df -h`             |
| `Display running processes`               | `ps aux`            |
| `Open a file with Nano editor`            | `nano filename.txt` |


## Основные улучшения:

1. **Определение языка** - автоматическое распознавание русских команд
2. **Словарь перевода** - базовые сопоставления русских команд с английскими аналогами
3. **AI-обработка** - использование LangChain для сложных преобразований
4. **Безопасность** - проверка и безопасное выполнение команд
5. **Пользовательский интерфейс** - сообщения на русском языке
6. **Документация** - README на русском языке

Теперь пользователи могут вводить команды как на русском, так и на английском языке, и система будет автоматически преобразовывать их в соответствующие команды терминала.

# 🚀 Let **AI-Terminal-X** Revolutionize Your Terminal Experience!

*"Speak simple. Work smart."*

*"Let AI turn your thoughts into commands!"* ✨
