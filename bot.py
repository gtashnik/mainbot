import telebot

bot = telebot.TeleBot("")


aboutme = 'Hello, My name is Dmitry Safarov. Am a web developer. I develop various websites and applications using PHP and JavaScript. I use WordPress and Yii2. I can also develop CMS from scratch'

web = 'I can develop any kind of web applications from simple landing pages to complicated web portals and online shops.\n\n'

contacts = 'My contacts are:\ntelegram: @SafarovDeem\nwebsite: https://findimension.com'


keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = telebot.types.KeyboardButton('Web development')
itembtn2 = telebot.types.KeyboardButton('About me')
itembtn3 = telebot.types.KeyboardButton('Contacts')
keyboard1.add(itembtn1, itembtn2, itembtn3)
#keyboard1.row('Web development', 'About me', 'Contacts', 'WordPress', 'Yii2', 'Python')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('About me', 'Contacts')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome!\n\nif you need a web application, feel free to contact!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'About me':
        bot.send_message(message.chat.id, aboutme, reply_markup=keyboard1)
    elif message.text == 'Web development':
        bot.send_message(message.chat.id, web, reply_markup=keyboard1)
    elif message.text == 'Contacts':
        bot.send_message(message.chat.id, contacts, reply_markup=keyboard1)
    


bot.polling()


