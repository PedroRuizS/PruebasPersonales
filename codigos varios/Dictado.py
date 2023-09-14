""" import speech_recognition as sr
import pyaudio
import concurrent.futures
import random
import keyboard
import pydirectinput
import pyautogui
from gtts import gTTS
import os
init_rec = sr.Recognizer()


i=1 #eso no se pa q es
bandera=0 #la bandera nos sirve para saber en que momento se sale del while, si esta en 1 se cumplio la condicion
texto = ("Escribe el texto a dictar") #el texto a dictar
num = int("Escribe cada cuantas palabras se va a detener")#Cada cuantas palabras se va a generar el audio
palabrasDictar = texto.split()#dividimos el texto completo en palabras


for palabra in palabrasDictar:
    contador=+1
    lectura = " ".join(palabrasDictar[:num])
    tts = gTTS(lectura, lang='es')#creamos un objeto text to speech para leer el texto
    archivo_audio = "primeras_cinco_palabras.mp3"
    tts.save(archivo_audio)

# Reproducir el archivo de audio
    os.system(f"start {archivo_audio}")

# Eliminar el archivo de audio después de la reproducción (opcional)
    os.remove(archivo_audio)
    if palabra==num:
        print("Continua el dictado o se detiene")
        while bandera != 1:
            with sr.Microphone() as source:
             print("listen")
            audio = init_rec.listen(source)
            print("record")

            audio_data = init_rec.record(source, duration=5)
            print("recognise")

            speech = init_rec.recognize_google(audio, language = 'en-US	')
        
            text = init_rec.recognize_google(audio_data)
            
            print(text)
            if text== "continua":
               bandera=1
            
bandera = 0   


 """



 ###El codigo q me corrigio chatgpt 

import speech_recognition as sr
from gtts import gTTS
import os

# Inicializamos el reconocedor de voz
init_rec = sr.Recognizer()

# Texto a dictar
texto = input("Escribe el texto a dictar: ")

# Número de palabras por fragmento
num = int(input("Escribe cada cuántas palabras se va a detener: "))

# Dividimos el texto completo en palabras
palabrasDictar = texto.split()

# Variable para controlar el bucle
bandera = 0

for i in range(0, len(palabrasDictar), num):
    fragmento = palabrasDictar[i:i+num]
    lectura = " ".join(fragmento)
    
    # Crear un objeto gTTS para leer el fragmento
    tts = gTTS(lectura, lang='es')
    
    # Guardar el discurso en un archivo de audio
    archivo_audio = "fragmento_audio.mp3"
    tts.save(archivo_audio)
    
    # Reproducir el archivo de audio
    os.system(f"start {archivo_audio}")
    
    # Eliminar el archivo de audio después de la reproducción
    os.remove(archivo_audio)
    
    # Pedir al usuario que continúe o se detenga
    if i + num < len(palabrasDictar):
        print("Presiona Enter para continuar o escribe 'detener' para detener la lectura.")
        respuesta = input()
        if respuesta.lower() == "detener":
            break

print("Lectura completada.")
