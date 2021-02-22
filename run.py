# Робот написан на Python 3.8.5

# Логика ведения диалога c роботом Rage:
# 1. Робот записывает речь и переводит в текст
# 2. Затем он подключается к своей базе данных и ищет ответ на ваш запрос
# 3. Если робот нашел ответ, то он превращает его в wav-файл и воспроизводит

import os
import time
import pyaudio
import pygame
import json

from vosk import Model, KaldiRecognizer

from modules import module
from db.database import Session
from db.models import Command


session = Session()


class Base():

    def waiting(self, record):
        """Выключение микрофона во время воспроизведения."""
        pygame.mixer.init()
        seconds = pygame.mixer.Sound(record).get_length()
        stream.stop_stream()
        time.sleep(seconds)
        stream.start_stream()


class Voice():

    base = Base()

    def add_answer(self):
        answer_record = 'voice/study.wav'
        module.play(answer_record)
        self.base.waiting(answer_record)

        answer_record = 'voice/1.wav'
        module.play(answer_record)
        self.base.waiting(answer_record)

        first = self.speech_record()
        print("Я услышал: ", first)
        answer_record = 'voice/2.wav'
        module.play(answer_record)
        self.base.waiting(answer_record)

        second = self.speech_record()
        print("Я услышал: ", second)

        session.add(Command(question=first, answer=second))


    def get_answer(self, text):
        answer = "Я не понимаю"
        commands = session.query(Command).all()
        for instance in commands:
            if text in instance.question:
                answer = instance.answer

        exists = os.path.isfile('records/%s.wav' % answer)
        if exists:
            answer_record = 'records/%s.wav' % answer
            module.play(answer_record)
            self.base.waiting(answer_record)
        else:
            module.text_to_speech(answer)
            answer_record = 'records/%s.wav' % answer
            module.play(answer_record)
            self.base.waiting(answer_record)
            print('Я сохранил файл: %s.wav' % answer)

    def speech_record(self):
        while True:
            data = stream.read(4000)
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result())['text']
                if text != "":
                    return text


class Rage():

    power = False
    base = Base()

    def input(self):
        self.power = True
        answer_record = 'voice/welcome.wav'
        module.play(answer_record)
        self.base.waiting(answer_record)

        command = Voice()

        while self.power:

            text = command.speech_record()

            if text == "перестань слушать":
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
        answer_record = 'voice/out.wav'
        module.play(answer_record)
        self.base.waiting(answer_record)


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
    command = Voice()

    while not rage.power:

        text = command.speech_record()
        print(f"Человек: {text}")

        if text == 'rage' or text == 'рэй' or text == 'меня слышно':
            rage.input()

        elif text == 'отключайся':
            rage.output()
            break
