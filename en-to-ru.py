from translate import Translator
from gtts import gTTS
import os
import speech_recognition as sr
stop1=1
while stop1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        try:
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")
        if str(r.recognize_google(audio_text))=="stop":
            stop1=0
    translator= Translator(to_lang="ru")
    translation=translator.translate(r.recognize_google(audio_text))

    tts = gTTS(text=translation, lang='ru')
    tts.save("good.mp3")
    os.system("good.mp3")
    import pyttsx3

text = 'какой-нибудь текст'
tts = pyttsx3.init()
rate = tts.getProperty('rate') #Скорость произношения
tts.setProperty('rate', rate-40)

volume = tts.getProperty('volume') #Громкость голоса
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

tts.say(text)
tts.runAndWait()
