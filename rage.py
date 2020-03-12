# Робот написан на Python 3.6

# Логика ведения диалога c роботом Рэйдж:
# 1. Робот записывает речь и сохраняет в wav-файл
# 2. После чего он преобразовывает сохраненный wav-файл в текст
# 3. Затем он подключается к своей базе данных и ищет ответ на ваш запрос
# 4. Если робот нашел ответ, то он превращает его в wav-файл и воспроизводит

import os
import time
import random
from modules import module

from database.database import CommandManager, PhraseManager


command = CommandManager()
phrase = PhraseManager()

# Запуск
while True:

    # Запись речи
    module.record()
    text = module.speech_to_text()
    print(text)
    
    if text == "rage":
        hello = False
        while True:
            
            # Приветствие
            if hello == False:
                hello = True
                module.play('voice/welcome.wav')
                time.sleep(2)
            
            # Запись речи
            module.record()
            text = module.speech_to_text()
            print("Я услышал: ", text)
            
            # Обучение робота
            if text == "хочешь научиться":
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

                command.create_command(first, second)

            # Переходит в спящий режим
            elif text == "перестань слушать":
                break
                time.sleep(2)

            # Поиск и сравнение по БД
            elif text != None:
                answer = "Я не понимаю"
                command_list = command.get_command_list()
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

            # Робот задает вопрос
            elif text == None:
                module.play('voice/ask.wav')
                time.sleep(3)


    # Выключение
    elif text == "выключись":
        module.play('voice/out.wav')
        time.sleep(2)
        break

    if text == None:
        phrase_list = phrase.get_phrase_list()
        id = 0
        for i in phrase_list:
            id += 1
            if id == random.randint(1, len(phrase_list)):
                answer = i[1]
                module.text_to_speech(answer)
                module.play('records/%s.wav' % answer)
                time.sleep(3)

    else:
        print("Rage слушает...")