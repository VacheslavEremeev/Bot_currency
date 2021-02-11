import telebot

URL_USD = 'https://banki24.by/minsk/kurs/usd'
URL_EUR= 'https://banki24.by/minsk/kurs/eur'
URL_RUB = 'https://banki24.by/minsk/kurs/rub'
TOKEN = '1695008999:AAFAhqP5iLnKm3uvpEwpUy5fezoZRPgbl_U'

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'

BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_RUB = 'RUB'

BUTTON_GET_ALL_LIST = 'Вывести весь список банков'
BUTTON_BEST_BUY_VALUE = 'Вывести лучший курс для покупки'
BUTTON_BEST_SELL_VALUE = 'Вывести лучший курс для продажи'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD, BUTTON_EUR)
KEYBOARD_START.row(BUTTON_RUB)

KEYBOARD_CHOISE = create_keyboard()
KEYBOARD_CHOISE.row(BUTTON_GET_ALL_LIST)
KEYBOARD_CHOISE.row(BUTTON_BEST_BUY_VALUE, BUTTON_BEST_SELL_VALUE)
KEYBOARD_CHOISE.row(BUTTON_START)