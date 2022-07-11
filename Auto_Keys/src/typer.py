import keyboard
import pyautogui
import os as self
import time
from time import sleep
import sys
import speech_recognition as sr
import playsound
from gtts import gTTS

time.sleep(3.5)

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    speak("Hello!")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))

    return said

print("Speak Now.. ")
text = get_audio()
if "" in text:
    sys.exit("Nothing To Write! [CLSD]: Closed Connection.")

keyboard.write(text)
