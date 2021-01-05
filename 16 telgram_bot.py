import telebot
from MyToken import TOKEN
from random import randint
import random

s = False
s2 = False
word_list = ('питон', 'палка', 'машина', 'слово', 'программирование')
word0 = random.choice(word_list)
word = list(word0)
ans = list("*" * len(word0))
kol = 0

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
    global s
    s = True

@bot.message_handler(commands=['play'])

def play_gallows(message):
    global s2
    s2 = True
    bot.send_message(message.chat.id, "*" * len(word))

@bot.message_handler(commands=['start'])

def bot_start(message):
    bot.send_message(message.chat.id, "Привет! Я умею переворачивать слова и создавать пароли.")
    bot.send_message(message.chat.id, "/password")
    bot.send_message(message.chat.id, "/reverse")


@bot.message_handler(content_types=['text'])

def otvet_na_text(message):
    print(message)
    global s, s2, kol
    if (s == True):
        bot.send_message(message.chat.id, message.text[::-1])
        s = False
    elif (s2 == True):
        if (message.text in word):
            for i in range(len(word)):
                if(word[i] == message.text):
                    ans[i] = message.text
        else:
            kol += 1
            bot.send_message(message.chat.id, "Этой буквы нет.")

        ans_s = ""
        for i in range(len(ans)):
            ans_s += str(ans[i])

        bot.send_message(message.chat.id, ans_s)
        bot.send_message(message.chat.id, "Количество ошибок: " + str(kol))

        if (ans == word):
            bot.send_message(message.chat.id, "Вы выиграли.")
            bot.send_message(message.chat.id, "Поздравляю")
            kol = 0

        if (kol == 5):
            bot.send_message(message.chat.id, "Вы проиграли.")
            bot.send_message(message.chat.id, "Удачи в следующий раз.")
            s2 = False
    else:
        bot.send_message(message.chat.id, "Введите команду.")

#vot nazvanie ArnautovPeter_FirstBot

bot.polling() #Забираем сообщения у бота



