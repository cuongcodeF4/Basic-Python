import speech_recognition as sr
from gtts import gTTS
import playsound
from datetime import datetime
import os
import webbrowser as wb


now = datetime.now()

def speak(text):
    print("ASSITANT:" + text)
    output = gTTS(text, lang='vi')
    file="sf.mp3"
    output.save(file)
    playsound.playsound(file,True)
    os.remove(file)

def welcome():
    # Chao hoi
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Chào buổi sáng!")
    elif hour >= 12 and hour < 18:
        speak("Chào buổi chiều!")
    elif hour >= 18 and hour < 24:
        speak("Chào buổi tối")
    speak("Tôi có thể giúp gì cho bạn không?")


def command():
    c=sr.Recognizer()#nghe người dùng nói
    with sr.Microphone() as source:
        print("Assistant đang nghe....")
        audio_data=c.record(source, duration=5)
    try:
        text = c.recognize_google(audio_data,language='vi')
        print("BẠN: " + text)
    except sr.UnknownValueError:
        print('Xin lỗi bạn tôi không nghe bạn nói gì. Bạn có thể đánh máy để yêu cầu!')
        text = str(input('Yêu cầu của bạn: '))
    return text

if __name__  =="__main__":
    welcome()
    while True:
        text = command().lower()
        if text == "":
            speak("Tôi không nghe rõ bạn nói gì. Bạn có thể nói lại không!")
        elif "xin chào" in text:
            speak("Xin chào bạn. Rất vui được giao tiếp với bạn")

        elif "ngày" in text:
            computer= now.strftime("Hôm nay là ngày %d tháng %m ")
            speak(computer)
        elif "giờ" in text:
            computer = "Bây giờ là:"+now.strftime("%H {x} %M {y} %S {z}").format(x="giờ",y="phút",z="giây")
            speak(computer)
        elif "mở google" in text:
            speak("Bạn muốn tìm kiếm cái gì?")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là kết quả của {search} trên google')
        elif "mở youtube" in text:
            speak("Bạn muốn tìm kiếm cái gì?")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là kết quả của {search} trên youtube')
        elif "mở video" in text:
            meme = r"C:\Users\Admin\Rose.mp3"
            os.startfile(meme)
        elif "bye" in text:
            computer="Chào tạm biệt mọi người"
            speak(computer)
            break
        else:
            computer="Tôi không hiểu bạn đang nói gì. Bạn có thể nói lại không?"
            speak(computer)



