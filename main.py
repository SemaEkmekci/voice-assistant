import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import time
import random
import os

r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Anlayamadım, lütfen tekrar eder misiniz?")
            speak("Anlayamadım, lütfen tekrar eder misiniz?")

        except sr.RequestError:
            print("Sistem Hatası")
        return voice


def response(voice):
    if "Etrafımda hangi nesneler var?" in voice:
        print("İyiyim,sen")
        speak("İyiyim,sen")
    if "Saat" in voice:
        print(datetime.now().strftime("%H:%M:%S"))
        speak(datetime.now().strftime("%H:%M:%S"))
    if "görüşürüz" in voice:
        speak("Görüşürüüüz")
        exit()
    if "fil Necati" in voice:
        speak(
            "Kımıl kımıl tüm yıldızlar. Dikkatli bakınca şekilleniyor. İşte bak şu bir koyun belki. Şu da süt annemi andırıyor. Kayan bir yıldız Dilek tutmalı İnşallah kafama düşer. Ah dileğim tuttu. Yıldız değilmiş bu bir brokoliymiş. Brokoli, bırak oni. Uç özgürce dön evine. Küçük ve sevimli brokoli. Özgür olmak en güzel şey. Uç Özgürce, Özgürceeee. Özgürceeee, Özgürcee, Özgürceee, Görümceee, Börülceeeeee Sütlüceee. Sütlüce'de inecek var"
        )


def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1, 10000)
    file = "audi-" + ".mp3"
    tts.save(file)
    # print(file)

    playsound("audi-.mp3")
    os.remove(file)


print("Merhaba, Ben sesli asistan, size nasıl yardımcı olabilirim?")
speak("Merhaba, Ben sesli asistan, size nasıl yardımcı olabilirim?")
time.sleep(1)

while True:
    voice = record()
    print(voice)
    response(voice)
