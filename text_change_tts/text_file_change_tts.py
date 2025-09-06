from gtts import gTTS
from playsound3 import playsound
import os

os.chdir(os.path.dirname(__file__))

text_file = "txt.txt"
with open(text_file, "rt", encoding="UTF8") as f:
    read_file = f.read()
    
tts = gTTS(text=read_file, lang="ko")

tts.save("Korean_song.mp3")

playsound("Korean_song.mp3")