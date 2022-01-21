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


class Base:

    model = Model("speech_to_text")
    rec = KaldiRecognizer(model, 16000)
    stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=16000,
                                    input=True,
                                    frames_per_buffer=8000)

    def waiting(self, record):
        """Выключение микрофона во время воспроизведения."""
        pygame.mixer.init()
        seconds = pygame.mixer.Sound(record).get_length()
        self.stream.stop_stream()
        time.sleep(seconds)
        self.stream.start_stream()


class Voice(Base):

    def add_answer(self):
        answer_record = 'voice/study.wav'
        module.play(answer_record)
        self.waiting(answer_record)

        answer_record = 'voice/1.wav'
        module.play(answer_record)
        self.waiting(answer_record)

        first = self.speech_record()
        print("Я услышал: ", first)
        answer_record = 'voice/2.wav'
        module.play(answer_record)
        self.waiting(answer_record)

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
            self.waiting(answer_record)
        else:
            module.text_to_speech(answer)
            answer_record = 'records/%s.wav' % answer
            module.play(answer_record)
            self.waiting(answer_record)
            print('Я сохранил файл: %s.wav' % answer)

    def speech_record(self):
        while True:
            data = self.stream.read(4000)
            if self.rec.AcceptWaveform(data):
                text = json.loads(self.rec.Result())['text']
                if text != "":
                    return text


class Rage(Voice):

    power = True
    command = None

    def __init__(self):
        if not os.path.isdir("records"):
            os.mkdir("records")

        answer_record = 'voice/welcome.wav'
        module.play(answer_record)
        self.waiting(answer_record)

    def on(self, command: str = None):
        while self.power:
            self.command = command if command else self.speech_record()

            exit_commands = ("отключайся", "отключись", "выключись", "перестань слушать", "заткнись",)

            if not self.command:
                answer_record = 'voice/ask.wav'
                module.play(answer_record)
                self.waiting(answer_record)
            elif self.command in exit_commands:
                self.off()
                self.power = False
            elif self.command == "хочешь научиться":
                self.add_answer()
            elif self.command:
                print(f"Человек: {self.command}")
                self.get_answer(self.command)

    def off(self):
        answer_record = 'voice/out.wav'
        module.play(answer_record)
        self.waiting(answer_record)


if __name__ == '__main__':

    rage = Rage()
    rage.on()
