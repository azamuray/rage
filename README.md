<p align="center"><img src="https://raw.githubusercontent.com/azamatmurdalov/rage/master/rage.png"></p>

## Robot Rage / Робот Рэйдж

Представляю вам код своего робота. Робот написан на языке программирования Python версии 3.6 (не совместим с версией 3.7 из-за библиотеки pyaudio)

На данный момент для воспроизведения голоса робота я использую технологию Yandex SpeechKit Cloud.
В дальнейшем планирую построить ядро на основе нейросетей.

## Installing / Установка

Вам также нужно запросить у Яндекса уникальный API-ключ (uuid) по ссылке https://developer.tech.yandex.ru/keys

Прежде, чем запустить робота, вы должны установить библиотеки с помощью этих команд:

      $ sudo apt-get install python-pip portaudio19-dev
      $ pip install pyaudio pygame requests lxml

После того, как вы установите эти пакеты (библиотеки), можете смело запускать робота.
