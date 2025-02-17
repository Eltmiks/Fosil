#Fosil 0.5
#created by "https://github.com/Eltmiks"

import json, pyaudio
import webbrowser as wb
from vosk import KaldiRecognizer, Model
import subprocess as sb
import cohere, requests
import api_key

model = Model("/home/pupsik/fosil/smoll")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
stream.start_stream()

co = cohere.Client(api_key.api_key)

def chat_with_cohere(text):
    try:
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=text,
            max_tokens=1500
        )
        return response.generations[0].text
    except Exception as e:
        print(f"Ошибка при запросе к Cohere: {e}")
        return "Извини, не могу сейчас ответить."

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

    elif text == "привет":
        print("привет я Fosil")
        
########################SITES###################

    elif "как думаеш" in text:
        cohere_prompt = text.replace("как думаеш", "").strip()
        cohere_response = chat_with_cohere(cohere_prompt)
        print(cohere_response)

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
   
    elif text == "открой обсидиан":    
        sb.Popen("/home/pupsik/fosil/scripts/obsi.sh")
        
    elif text == "открой окси":    
        sb.Popen(["/home/pupsik/fosil/scripts/obsi.sh"])

    elif text == "вот простим":
        sb.Popen(["/home/pupsik/fosil/scripts/steam.sh"])

    elif text == "открой стен":
        sb.Popen(["/home/pupsik/fosil/scripts/steam.sh"])

    elif text == "откройте":
        sb.Popen(["/home/pupsik/fosil/scripts/steam.sh"])
        
    elif text == "открой тим":
        sb.Popen(["/home/pupsik/fosil/scripts/steam.sh"])
        
    elif text == "откройте эскорт":
        sb.Popen(["/home/pupsik/fosil/scripts/ds.sh"]) 

    elif text == "открой корт":
        sb.Popen(["/home/pupsik/fosil/scripts/ds.sh"])

    elif text == "открой дисконт":
        sb.Popen(["/home/pupsik/fosil/scripts/ds.sh"]) 
        
    elif text == "открой дисконт":
        sb.Popen(["/home/pupsik/fosil/scripts/ds.sh"]) 
        
    elif text == "открой вес скот":
        sb.Popen(["/home/pupsik/fosil/scripts/code.sh"]) 
        
    elif text == "открой визуал студио":
        sb.Popen(["/home/pupsik/fosil/scripts/code.sh"]) 
        
    elif text == "открой код":
        sb.Popen(["/home/pupsik/fosil/scripts/code.sh"]) 
