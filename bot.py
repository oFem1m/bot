TOKEN = '837306184:AAEYogiApuVCRNF2iJhOdYXHBDFZnmU8wQs'
import telebot as tb
import datetime
import random
import digit
import weather
bot = tb.TeleBot(token=TOKEN)
user = bot.get_me()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat2 = message.chat
    chat_id = message.chat.id
    bot.send_message(message.from_user.id, f'������, {chat2.first_name}, � ���! ������ ������, ��� � ����? ������ ��� /help')


@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    with open('commands.txt') as comm:
        bot.send_message(chat_id, comm)

@bot.message_handler(commands=['time'])
def send_time(message):
    bot.reply_to(message, datetime.datetime.now().time())
        
@bot.message_handler(regexp=r'\b([kK��])([aA��@4])\1\s*[��dD][��eE6][��lL]\2\b')
def send_dela(message):
    bot.reply_to(message, '�� ��')

@bot.message_handler(regexp=r'\b[��pP][��rR][��iI��eE][��vV��fF][��eE][��tT��dD]\b')
def send_hello(message):
    chat2 = message.chat
    chat_id = message.chat.id
    bot.send_message(chat_id, f'������, {chat2.first_name}, � ���! ������ ������, ��� � ����? ������ ��� /help')
    
@bot.message_handler(commands=['file'])
def send_file(message):
    bot.reply_to(message, 'https://yadi.sk/d/ffl-toEP3yzDNA')
    
@bot.message_handler(commands=['place'])
def send_place1(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '��������� ����������')
    bot.register_next_step_handler(message, send_place2)
def send_place2(message):
    chat_id = message.chat.id
    text1 = message.text
    C = (text1.split())
    try:
        bot.send_location(chat_id, C[0], C[1])
    except:
        bot.send_message(chat_id, "��� �� ���������� ;(")
    
@bot.message_handler(commands=['weather'])
def send_weather1(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '��������� �������� ������ ��� ��� ����������')
    bot.register_next_step_handler(message, send_weather2)
def send_weather2(message):
    chat_id = message.chat.id
    text1 = message.text
    C = (text1.split())
    if digit.is_digit(C[0]):
        bot.send_message(chat_id, weather.weather_coords(C[0], C[1]))
    else:
        bot.send_message(chat_id, weather.weather_city(C[0]))

    
@ bot.message_handler ( func = lambda  m : True )
def  echo_all (message):
    bot.reply_to (message, message.text)


bot.polling()
