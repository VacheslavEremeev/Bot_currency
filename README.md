# Bot_currency ( Доступен в Telegram по имени @belar_bot_currency_bot )
Бот в Телеграме. Парсит данные с сайта по курсу валют в городе Минск (с адреса: https://banki24.by/minsk/kurs/usd ). 

Чтобы начать с ним общение, необходимо написать '/start'.
После Бот спросит пользователя какая валюта его интересует.
Доступен вывод не только по долларам, но и по евро и рублям.
После выбора валюты (есть кнопки, самому ничего писать не надо)
Бот предоставит пользователю кнопки для вывода
лучших курсов валют (продажи и покупки) с названиями банков.
Либо может вывести список всех банков. Четвёртая кнопка
вернёт пользователя в начало (этап выбора валюты - USD/EUR/RUB).
Размещен Бот на внешнем сервере heroku.
(Локально запускается из файла main.py)

При создании Бота возможна ошибка:
AttributeError: 'TeleBot' object has no attribute 'message_handler' 

Не паникуй. Скорее всего помогут вот эти команды (но это не точно;) :
pip install PyTelegramBotAPI==2.2.3
pip install PyTelegramBotAPI==3.6.7
Или поищи решение здесь:
[1 ссыль]  https://stackoverflow.com/questions/64951712/telebot-object-has-no-attribute-message-handler
[2 ссыль]  https://www.pythonanywhere.com/forums/topic/26658/
[3 ссыль]  https://stackoverflow.com/questions/59909321/im-writing-a-telegram-bot-with-python

Если есть вопросы и/или предложения найти меня можно здесь:
https://vk.com/evrotigan
