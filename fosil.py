#Fosil 0.2
#created by "https://github.com/Eltmiks"

import json, pyaudio
import webbrowser as wb
from vosk import KaldiRecognizer, Model
import subprocess as sb

model = Model("/home/pupsik/fosil/smoll")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow = False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0): 
            answer = json.loads(rec.Result())
            if answer ["text"]:
                yield answer["text"]
                
#for text in listen():
#   print(text)
    
for text in listen():
    if text == "отключись":
        print("удачи!")
        quit

########################SITES###################
        
    elif text == "привет":
        print("привет я Fosil")
    
    elif text == "открой ютуб":
        wb.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")
        
    elif text == "открой ету":
        wb.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")

    elif text == "открой эту":
        wb.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")

    elif text == "открой я тут":
        wb.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")

    elif text == "открой я туп":
        wb.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")
        
    elif text == "открой помощь":
        wb.open("https://gemini.google.com/app?hl=uk")

    elif text == "открой хаб":
        wb.open("https://github.com/Eltmiks")

    elif text == "открой хап":
        wb.open("https://github.com/Eltmiks")

    elif text == "открой ет хап":
        wb.open("https://github.com/Eltmiks")
        
    elif text == "открыть хаб":
        wb.open("https://github.com/Eltmiks")
        
    elif text == "открой хип-хоп":
        wb.open("https://github.com/Eltmiks")
        
    elif text == "открой гид хаб":
        wb.open("https://github.com/Eltmiks")

    elif text == "открой аниме":
        wb.open("https://jut.su/anime/ongoing/order-by-add/") 
        
########################APP###################
   
for text in listen():
    if text == "открой дискорд":    
        sb.Popen(["/opt/discord/Discord"])
        
    elif text == "откройте эскорт":
        sb.Popen(["/opt/discord/Discord"])     
 
    elif text == "откройте дисконт":
        sb.Popen(["/opt/discord/Discord"])     
 
    elif text == "откройте скотт":
        sb.Popen(["/opt/discord/Discord"])     



