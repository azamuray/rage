# Робот написан на Python 3.6

# Логика ведения диалога c роботом Рэйдж:
# 1. Робот записывает речь и сохраняет в wav-файл
# 2. После чего он преобразовывает сохраненный wav-файл в текст
# 3. Затем он подключается к своей базе данных и ищет ответ на ваш запрос
# 4. Если робот нашел ответ, то он превращает его в wav-файл и воспроизводит

import os
import time
import random
import pyaudio
import json

from vosk import Model, KaldiRecognizer


from modules import module
from database.database import CommandManager, PhraseManager


class Phrase(PhraseManager):

    phrase = PhraseManager()

    def get_phrase(self):
        phrase_list = self.phrase.get_phrase_list()
        id = 0
        for i in phrase_list:
            id += 1
            if id == random.randint(1, len(phrase_list)):
                answer = i[1]
                module.text_to_speech(answer)
                module.play('records/%s.wav' % answer)
                time.sleep(3)


class Command(CommandManager):

    def add_answer(self):
        module.play('voice/study.wav')
        time.sleep(8)
        module.play('voice/1.wav')
        time.sleep(1)

        module.record()
        first = module.speech_to_text()
        print("Я услышал: ", first)
        module.play('voice/2.wav')
        time.sleep(1)

        module.record()
        second = module.speech_to_text()
        print("Я услышал: ", second)
        time.sleep(3)

        self.create_command(first, second)

    def get_answer(self, text):
        answer = "Я не понимаю"
        command_list = self.get_command_list()
        for i in command_list:
            if text in i[0]:
                answer = i[1]

        exists = os.path.isfile('records/%s.wav' % answer)
        if exists:
            module.play('records/%s.wav' % answer)
        else:
            module.text_to_speech(answer)
            module.play('records/%s.wav' % answer)
            print('Я сохранил файл: %s.wav' % answer)
        time.sleep(3)


class Rage():

    power = False

    def input(self):
        self.power = True
        module.play('voice/welcome.wav')
        time.sleep(2)

        while self.power:

            command = Command()

            text = self.speech_record()

            if text == "":
                print("Rage: пока что тихо")
                continue

            elif text == "перестань слушать":
                self.power = False

            elif text == "хочешь научиться":
                command.add_answer()

            elif text != None:
                print(f"Человек: {text}")
                command.get_answer(text)

            elif text == None:
                module.play('voice/ask.wav')
                time.sleep(3)

    def output(self):
        module.play('voice/out.wav')
        time.sleep(2)

    def speech_record(self):
        data = stream.read(4000)
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())['text']
            return text
        return ""


if __name__ == '__main__':

    model = Model("speech_to_text")
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8000)
    stream.start_stream()

    rage = Rage()

    while not rage.power:

        text = rage.speech_record()
        print(f"Человек: {text}")
        if text == 'rage' or text == 'рэй':
            rage.input()

        elif text == 'выключись':
            rage.output()
            break

        elif text == None:
            phrase = Phrase()
            phrase.get_phrase()
