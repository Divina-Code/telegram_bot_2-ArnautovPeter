import telebot
from MyToken import TOKEN
from random import randint


bot = telebot.TeleBot(TOKEN)  #Создаём подключение к боту

@bot.message_handler(commands=['password'])

def create_password(message):
    password = list("........")
    check = list("12345678")
    check2 = 0
    while (check2 != -1):
            a = randint(1, 2)
            if (a == 1):
                b = int(randint(1, 8))
                if (check[b - 1] != '*'):
                    password[b - 1] = randint(0, 9)
                    check[b - 1] = '*'
            elif (a == 2):
                b = randint(1, 8)
                if (check[b - 1] != -1):
                    c = int(randint(1, 2))
                    if (c == 1):
                        password[b - 1] = chr(randint(65, 90))
                        check[b - 1] = '*'
                    elif (c == 2):
                        password[b - 1] = chr(randint(97, 122))
                        check[b - 1] = '*'
            sum = int(0)
            for i in range(8):
                if (check[i] == '*'):
                    sum += 1
            if (sum == 8):
                check2 = -1
    password_s = ""
    for i in range(8):
        password_s += str(password[i])
    bot.send_message(message.chat.id, password_s)

@bot.message_handler(commands=['reverse'])

def reverse_message(message):
    bot.send_message(message.chat.id, message.text[:8:-1])

@bot.message_handler(content_types=['text'])

def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, "Привет! Я умею переворачивать слова и создавать пароли.")
    bot.send_message(message.chat.id, "/password")
    bot.send_message(message.chat.id, "/reverse your text")

#vot nazvanie ArnautovPeter_FirstBot

bot.polling() #Забираем сообщения у бота



