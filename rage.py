# -*- coding: utf-8 -*-

# Будем использовать Yandex Speachkit для синтеза речи
# (ключ нам не понадобится)

# импортируем модуль requests чтоб отправить get запрос
import requests
# импортируем модуль pyglet для воспроизведения mp3-файла
import pyglet

# формируем запрос, который вернет озвученный текст
request = requests.get("https://tts.voicetech.yandex.net/tts?text=Hello World")

# открываем (создаем) mp3-файл в режиме 'wb' (write-binary-mode)
# и записываем в него озвученный текст
open('file.mp3', 'wb').write(request.content)

# воспроизводим наш mp3-файл
song = pyglet.media.load('file.mp3')
song.play()
pyglet.app.run()
