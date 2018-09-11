# -*- coding: utf-8 -*-

import pygame
import requests
import sqlite3

# преобразовываю текст в речь и записываю в wav-файл
def text_to_speech(text):
    url = 'https://tts.voicetech.yandex.net/tts'
    get_file = requests.get(url + '?text=' + text + '&format=wav&speaker=ermil')
    open('file.wav', 'wb').write(get_file.content)

# воспроизвожу полученный wav-файл c помощью pyaudio и wave
def play():
    pygame.init()
    pygame.mixer.Sound('file.wav').play()

# делаю соединение с базой данных
connection = sqlite3.connect('base.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM commands")
rows = cursor.fetchall()

# запускаю робота
while True:
    answer = "Я тебя не понимаю"
    text = raw_input(" -> ")
    text = unicode(text, "UTF-8")
    for comand in rows:
        if text == comand[0]:
            answer = comand[1]
    if text == u"Выключись":
        break
    text_to_speech(answer)
    play()
