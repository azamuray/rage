# -*- coding: utf-8 -*-

import requests
import pyglet

url = "https://tts.voicetech.yandex.net/tts"
speaker = "ermil"

# функция преобразовывает текст в речь, а затем воспроизводит
def text_to_speech(text):
    request = requests.get(url + "?text=" + text + "&speaker=" + speaker)
    open('file.mp3', 'wb').write(request.content)
    song = pyglet.media.load('file.mp3')
    song.play()
    pyglet.app.run()

text = raw_input(" -> ")

if text == "ты робот?":
    text_to_speech("А разве не видно?")
else:
    text_to_speech("Не понимаю")
