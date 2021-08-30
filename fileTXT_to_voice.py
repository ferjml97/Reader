from gtts import gTTS
import os

file = open("lector_texto.txt", "r").read().replace("\n"," ")

language = 'es-us'

speech = gTTS(text = str(file), lang= language,  slow = False)

speech.save("audios/lector_texto.mp3")

os.system("start audios/lector_texto.mp3")