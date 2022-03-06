
from gtts import gTTS
from pygame import mixer
import tempfile
import os
import sys

def speak(sentence,lang):
    tts=gTTS(text=sentence, lang=lang)
    tts.save("test.mp3")
    os.system("mpg123"+" test.mp3")

if __name__ == '__main__':
    speak("apple",'en')
