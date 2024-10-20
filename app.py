import speech_recognition  
import pyttsx3
import subprocess
import webbrowser

reconocedor = speech_recognition.Recognizer()
voz = pyttsx3.init()

voz.setProperty('rate', 150)  # Velocidad de habla
voz.setProperty('volume', 1)  # Volumen (entre 0.0 y 1.0)

# Ejemplo de hablar un mensaje
voz.say("Hola, ¿cómo estás?")
voz.runAndWait()