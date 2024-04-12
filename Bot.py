import os
import telebot
from transcribe_audio import *
from AI_model import *
from pathlib import Path

bot = telebot.TeleBot("6892313744:AAFL-7ru7PxSZhdzQ9SnVh1kt_LcqkGtV8k")


@bot.message_handler(commands=['hi', 'hello', 'start'])
def cmd1(message):
    bot.reply_to(message, "Hello, I am Edo, How may i help you today ?")


@bot.message_handler(func=lambda msg:True)
def echo_back(message):
    res = agent_executor.invoke({"input":message.text})
    bot.reply_to(message, res["output"])


@bot.message_handler(content_types=['voice'])
def listen_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('audio_data/query.ogg', 'wb') as file:
        file.write(downloaded_file)
    text_message = get_audio('audio_data/query.ogg')   
    res = agent_executor.invoke({"input":text_message})
    bot.send_message(message.chat.id, res["output"])



bot.infinity_polling()