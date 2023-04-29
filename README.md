
## Мониторинг цены на фьючерм ETHUSDT

Программа в реальном времени следит за ценой фьючерса ETHUSDT, при изменении цена на 1% за последние 60 минут выводит сообщение в консоль и отправляет сообщение в телеграмм. Цена ETH береться с coingecko.com

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
  git git@github.com:EgorFedotov/price_tracking.git
```

Переходим в дерикторию с проектом

```bash
  cd price_tracking
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


