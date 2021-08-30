from gtts import gTTS
import os

text = "Hola me llamo Fernando, y tú?"

language = 'es-us'

speech = gTTS(text = text, lang= language,  slow = False)

speech.save("audios/texto.mp3")

os.system("start audios/texto.mp3")
