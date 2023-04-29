import random
import time
import os

import requests
import telegram
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def get_price():
    '''Функция определяет цену eth к usdt.'''
    eth_price = requests.get(
        'https://api.coingecko.com/api/v3/coins/ethereum?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false')
    eth_price = eth_price.json()['market_data']['current_price']['usd']
    return eth_price


def send_message(bot, message):
    """отправка сообщения."""
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except telegram.error.TelegramError as error:
        print(f'Сообщение не отправлено {error}')


def main():
    last_price = None
    last_time = None
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    while True:
        try:
            price = get_price()
            if not last_price:
                last_price = price
                last_time = time.time()
            else:
                change = (price / last_price - 1) * 100
                if abs(change) > 1 and time.time() - last_time < 3600:
                    message = (f'Цена ETH изменилась больне 1% {change}, цена eth: {price}')
                    print(message)
                    send_message(bot, message)
                last_price = price
                last_time = time.time()
            time.sleep(random.randint(5, 10))
        except KeyError as e:
            print(f'Ждем 3 минуты, не проходит get Запрос{e}')
            send_message(bot, 'Ждем 3 минуты, не проходит get Запрос')
            time.sleep(180)
        except Exception as e:
            print(f'Error: {e}')
            send_message(bot, f'error: {e}')


if __name__ == '__main__':
    main()
