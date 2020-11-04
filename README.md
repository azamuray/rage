<p align="center"><img src="https://raw.githubusercontent.com/azamatmurdalov/rage/master/logo.png"></p>

# Робот Рэйдж

Представляю вам код своего робота. Он написан на языке программирования Python версии 3.8.5 в стиле ООП.

На данный момент для воспроизведения голоса робота я использую технологию Yandex SpeechKit Cloud.
В дальнейшем планирую перейти на что-то автономное.


# Функционал

## Программа:

Робот может вести диалог с человеком. Он записыват речь в wav-файл, переводит в текст, сравнивает его с вопросами из своей базы данных и если находит похожий вопрос, то берет ответ из базы данных, переводит в речь и озвучивает, а если не находит вопрос, то он просто говорит: "Я тебя не понимаю". Вопросы и ответы хранятся в базе данных SQLite3.
Для перевода текста в речь и обратно используется технология Yandex SpeechKit CLoud. Также используются библиотеки Wave для создания wav-файла и Pygame для воспроизведения wav-файла.

Если задать роботу вопрос "хочешь научиться?", то он предлагает при команде "один" озвучить вопрос, затем, после команды "два", озвучить ответ, после чего он переводит эти данные в текст и сам записывает в базу данных. Таким образом робот в каком-то смысле может обучаться.

Если робот отвечает на какой-то вопрос впервые, то он создает новый wav-файл в папке records, чтоб в следующий раз сразу же воспроизвести этот файл, чем тратить время на синтез речи. Это делается для более быстрого ответа от робота.

## Железо:

Тело робота состоит из алюминевой головы с вырезами для глаз и отверстиями для динамиков. Внутри головы находятся микроконтроллер Arduino Uno, два красных диода и музыкальные колонки.
Arduino используется для подсветки диодов, а музыкальные колонки (динамики) используются для воспроизведения речи робота, и они подключены к ноутбуку через провода.
Также у робота есть туловище, но оно пока что не соединено с роботом. Да и робот пока что не может самостоятельно работать и приходится подключать его к ноутбуку.


# Установка

Вам также нужно запросить у Яндекса уникальный API-ключ (uuid) по ссылке https://developer.tech.yandex.ru/keys

Прежде, чем запустить робота, вы должны установить необходимые библиотеки следующими командами:

      $ sudo apt-get install python3-pip portaudio19-dev
      $ pip install -r requirements.txt

После того, как вы установите эти библиотеки, можете смело запускать робота.


# Версии

## Версия 1.0:

Робот может вести диалог с человеком. Он записыват речь в wav-файл, переводит в текст, сравнивает его с вопросами из своей базы данных и если находит похожий вопрос, то берет ответ из базы данных, переводит в речь и озвучивает, а если не находит вопрос, то он просто говорит: "Я тебя не понимаю". Вопросы и ответы хранятся в базе данных SQLite3.
Для перевода текста в речь и обратно используется технология Yandex SpeechKit CLoud. Также используются библиотеки Wave для создания wav-файла и Pygame для воспроизведения wav-файла.

Тело робота состоит из алюминевой головы с вырезами для глаз и отверстиями для динамиков. Внутри головы находятся микроконтроллер Arduino Uno, два красных диода и музыкальные колонки.
Arduino используется для подсветки диодов, а музыкальные колонки (динамики) используются для воспроизведения речи робота и они подключены к ноутбуку через провода.
Также у робота есть туловище, но оно пока что не соединено с роботом. Да и робот пока что не может самостоятельно работать и приходится подключать его к ноутбуку.

## Версия 1.1:

Автоматизировано добавление данных в базу данных. Если задать роботу вопрос "хочешь научиться?", то он предлагает при команде "один" озвучить вопрос, затем, после команды "два", озвучить ответ, после чего он переводит эти данные в текст и сам записывает в базу данных. Таким образом робот в каком-то смысле может обучаться.

Если робот отвечает на какой-то вопрос впервые, то он создает новый wav-файл в папке records, чтоб в следующий раз сразу же воспроизвести этот файл, чем тратить время на синтез речи. Это делается для более быстрого ответа от робота.

## Версия 1.2:

Выполнен переход на Python 3.8.5.
Код переписан с процедурного стиля на ООП.
Добавлена таблица Фразы. Теперь робот произносит различные фразы, если с ним никто не беседует.
Исправлены некоторые баги, связанные с записью команд в базу данных.
