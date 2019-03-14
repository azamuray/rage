# Робот написан на Python 3.6

# Логика ведения диалога c роботом Рэйдж:
# 1. Робот записывает нашу речь и сохраняет в wav-файл
# 2. После чего он преобразовывает сохраненный wav-файл в текст
# 3. Затем он подключается к своей базе данных и ищет ответ на ваш текст
# 4. Если робот нашел ответ, то он превращает его в wav-файл

import os
import time
import sqlite3
import random
from modules import module

# делает соединение с базой данных
connection = sqlite3.connect('base.db')
cursor = connection.cursor()
rows = cursor.execute("SELECT * FROM commands").fetchall()

# запуск
while True:

    # запись речи
    module.record()
    text = module.speech_to_text()
    print(text)
    
    if text == "rage":

        hello = False
        while True:
            
            # приветствие
            if hello == False:
                hello = True
                module.play('voice/welcome.wav')
                time.sleep(2)
            
            # запись речи
            module.record()
            text = module.speech_to_text()
            print("Я услышал: ", text)
            
            # обучение робота
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

                cursor.execute("""INSERT INTO commands VALUES ('%s', '%s')""" % (first, second))
                connection.commit()

            # переходит в спящий режим
            elif text == "перестань слушать":
                break
                time.sleep(2)

            # поиск и сравнение по БД
            elif text != None:
                answer = "Я не понимаю"
                rows = cursor.execute("SELECT * FROM commands").fetchall()
                for command in rows:
                    if text in command[0]:
                        answer = command[1]

                exists = os.path.isfile('records/%s.wav' % answer)
                if exists:
                    module.play('records/%s.wav' % answer)
                else:
                    module.text_to_speech(answer)
                    module.play('records/%s.wav' % answer)
                    print('Я сохранил файл: %s.wav' % answer)
                time.sleep(3)

            # робот задает вопрос
            elif text == None:
                module.play('voice/ask.wav')
                time.sleep(3)


    # выключение
    elif text == "выключись":
        module.play('voice/out.wav')
        time.sleep(2)
        break

    if text == None:
        rows = cursor.execute("SELECT * FROM phrases").fetchall()
        id = 0
        for command in rows:
            id += 1
            if id == random.randint(1, len(rows)):
                answer = command[0]
                module.text_to_speech(answer)
                module.play('records/%s.wav' % answer)
                time.sleep(3)

    else:
        print("Rage слушает...")