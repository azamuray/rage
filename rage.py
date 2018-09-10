# -*- coding: utf-8 -*-

import requests
import pyaudio
import wave

# преобразовываем текст в речь и записываем в wav-файл
def text_to_speech(text):
    url = 'https://tts.voicetech.yandex.net/tts'
    get_file = requests.get(url + '?text=' + text + '&format=wav&speaker=ermil')
    open('file.wav', 'wb').write(get_file.content)

# воспроизводим полученный wav-файл c помощью pyaudio и wave
def play():

    #задаем количество сэмплов
    CHUNK = 1024

    #открываем файл wav-формата
    f = wave.open(r"file.wav","rb")

    #создаем объект PyAudio
    p = pyaudio.PyAudio()

    #открываем поток (набор) данных
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    data = f.readframes(CHUNK)

    #запускаем поток
    while data:
        stream.write(data)
        data = f.readframes(CHUNK)

    #останавливаем поток
    stream.stop_stream()
    stream.close()

    #закрываем PyAudio
    p.terminate()

# создаем базу команд
base = ["Привет = Приветствую тебя, человек",
        "Видишь меня? = Пока что не вижу, у меня глаз",
        "Понимаешь меня? = Я робот, я не могу понять",
        "Ты такой грустный = Роботы не бывают грустными",
        "Ты робот? = Конечно робот"]

# запускаем робота
answer = "Я тебя не понимаю"
while True:
    text = raw_input(" -> ")
    for comand in base:
        comand = comand.split(" = ")
        if text == comand[0]:
            answer = comand[1]
        elif text == "Выключись":
            break
    text_to_speech(answer)
    play()
