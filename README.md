
## Мониторинг цены на фьючерм ETHUSDT

Программа в реальном времени следит за ценой фьючерса ETHUSDT, при изменении цена на 1% за последние 60 минут выводит сообщение к консоль и отправляет сообщение в телеграмм. Цена ETH береться с coingecko.com

## Используемые инструменты

- Python

- requests

- python-telegram-bot


## Инструкция по развертыванию проекта

В корне дирректории создаем файл .env и добавляем туда 

- TELEGRAM_TOKEN

- TELEGRAM_CHAT_ID

Клонируем репозиторий к себе на ПК

```bash
  git 
```

Переходим в дерикторию с проектом

```bash
  cd infra_sp2
  cd api_yamdb
```

Устанавливаем Виртуальное окружение

```bash
  py -3.7 -m venv venv
```

Активируем виртуальное окружение

```bash
  source venv/Scripts/activate
```

Устанавливаем зависимости

```bash
  pip install -r requirements.txt
```

Запускаем программу

```bash
  python main.py
```


# В корне дерриктории infa создайте файл .env и добавьте туда:
  - SECRET_KEY
  - DB_ENGINE
  - DB_NAME
  - POSTGRES_USER
  - POSTGRES_PASSWORD
  - DB_HOST
  - DB_PORT


# Документация доступна по адрессу: http://localhost/redoc/

## 🚀 Автор
Егор Федотов


