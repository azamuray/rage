# -*- coding: utf-8 -*-
from gtts import gTTS

voice = gTTS(text=u'Привет Азамат. Меня зовут Рэйдж', lang='ru')
voice.save('voice_Rage.mp3')
