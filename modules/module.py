import pygame
import requests


# преобразовывает текст в речь и записывает ее в wav-файл
def text_to_speech(text):
    url = 'https://tts.voicetech.yandex.net/tts?text='
    get_file = requests.get(url + text + '&format=wav&speaker=ermil')
    open('records/%s.wav' % text, 'wb').write(get_file.content)

# воспроизводит полученный wav-файл c помощью pygame
def play(fname):
    pygame.init()
    pygame.mixer.Sound(fname).play()
