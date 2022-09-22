
"""from gtts import gTTS
import playsound


def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
speak("Rất vui được gặp bạn")"""


from gtts import gTTS
import playsound
import os
text = 'tôi có thể giúp gì cho bạn'
def texttospeech(text):
    print('Bot —>:',text)
    output = gTTS(text,lang='vi')
    output.save('output.mp3')
    playsound.playsound('output.mp3', True)
    os.remove('output.mp3')
texttospeech(text)