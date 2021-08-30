![Python](http://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=ffffff)

---

# Reader
Text to speech reader with Python

### Description
In the first file, `text_to_voice` is a text to speech converter program 
and file, `fileTXT-to_voice` is a text's file to speech converter program using 
the file `lector_texto.txt` that is a text file to convert to speech
and folder `audios` is a folder to save audios and now, has the audios outcomes added.

#### gTTS (Google Text-to-Speech)
<img src="https://i.imgur.com/UdocDTY.jpeg" align="right" height="200" width="320" vspace="35">
<div style="text-align: justify;">
  It´s a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
  Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. 
  Or simply pre-generate Google Translate TTS request URLs to feed to an external program. 
 
</div> <br> 


**Features**
 - Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
 - Customizable text pre-processors which can; *provide pronunciation corrections*

**Installation**
  
  ``` 
  $ pip install gTTS
  ```

**Quickstart**  

  **` Command Line: `**  
  
  ```
  $ gtts-cli 'hello' --output hello.mp3
  ```
  **` Module: `**  
  ```
  >>> from gtts import gTTS
  >>> tts = gTTS('hello')
  >>> tts.save('hello.mp3')
  >>> 
  ```
 
  
See http://gtts.readthedocs.org/ for documentation and examples. 

> 🛑 It's recommended to have basic knowledge of ![Python](http://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=ffffff)

### Enlaces de Interés
- [Python W3SCHOOLS](https://www.w3schools.com/python/default.asp "Python W3SCHOOLS")
- [Text Reader](https://www.textfromtospeech.com/es/text-to-voice/#:~:text=Una%20herramienta%20de%20texto%20a,en%20voz%20alta%20textos%20digitales.&text=Luego%2C%20a%20trav%C3%A9s%20de%20un,de%20audio%20de%20ese%20texto. "Text Reader")
- [Page library gTTS](https://pypi.org/project/gTTS/ "Page library gTTS")
- [Documentation gTTS](https://gtts.readthedocs.io/en/latest/ "Documentation gTTS")

---

con ❤ **[@ferjml97](https://github.com/ferjml97)** 🙂
