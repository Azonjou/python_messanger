# Python WebSocket Messenger

Простой асинхронный консольный мессенджер на Python с использованием библиотеки `websockets` и `asyncio`. Поддерживает одновременное подключение нескольких клиентов и рассылку сообщений в реальном времени.

## Стек технологий

* Python 3.10+
* `websockets`
* `asyncio`

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone [https://github.com/твой-логин/python-messenger.git](https://github.com/твой-логин/python-messenger.git)
cd python-messenger
```

### 2. Настройка виртуального окружения
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Запуск проекта
1. Запустите сервер:
   ```bash
   python server.py
   ```
2. В отдельных терминалах запустите одного или нескольких клиентов:
   ```bash
   python client.py
   ```