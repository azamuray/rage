# -*- coding: utf-8 -*-

import requests
import pyaudio
import wave
import sqlite3

# преобразовываю текст в речь и записываю в wav-файл
def text_to_speech(text):
    url = 'https://tts.voicetech.yandex.net/tts'
    get_file = requests.get(url + '?text=' + text + '&format=wav&speaker=ermil')
    open('file.wav', 'wb').write(get_file.content)

# воспроизвожу полученный wav-файл c помощью pyaudio и wave
def play():

    # задаю количество сэмплов
    CHUNK = 1024

    # открываю файл wav-формата
    f = wave.open(r"file.wav","rb")

    # создаю объект PyAudio
    p = pyaudio.PyAudio()

    # открываю поток (набор) данных
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    data = f.readframes(CHUNK)

    # запускаю поток
    while data:
        stream.write(data)
        data = f.readframes(CHUNK)

    # останавливаю поток
    stream.stop_stream()
    stream.close()

    # закрываю PyAudio
    p.terminate()

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
