while True:
    record()
    text = speech_to_text()
    print("Я услышал: ", text)

    if text == "выключись":
        play('voice/out.wav')
        time.sleep(2)
        break

    elif text != None:
        answer = "я тебя не понимаю"
        for command in rows:
            if text in command[0]:
                answer = command[1]
        # text_to_speech(answer)
        answer = input('Введите ответ: ')
        time.sleep(5)
        if answer == "я тебя не понимаю":
            study = "Если знаешь ответ, то скажи мнею. Я запомню"
            text_to_speech(study)
            time.sleep(5)
            record()
            new = speech_to_text()
            if new == "да": 
                ask = input("Задай свой вопрос")
                answer = input("А таперь сам же на него ответь")
                cursor.execute("""INSERT INTO commands VALUES ('%s', '%s')""" % (ask, answer))
                conn.commit()

    elif text == None:
        play('voice/ask.wav')
        time.sleep(3)