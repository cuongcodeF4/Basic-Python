import pyttsx3

friday=pyttsx3.init()

voices = friday.getProperty('voices')
friday.setProperty('voice', voices[0].id)
friday.say("Hôm nay là một ngày đẹp trời ")
friday.runAndWait()