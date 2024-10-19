import speech_recognition as sr
import pyttsx3
import os
import subprocess

#Variables
reconocedor = sr.Recognizer()
motor_voz = pyttsx3.init()
mic_id = 1
# Comandos
comandos = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte?",
    "abre navegador": "Abriendo el navegador.",
    "cierra navegador": "Cerrando el navegador.",
    "qué hora es": "Lo siento, no puedo decir la hora en este momento."
    "Abrir youtube"
}

def hablar(texto):
    motor_voz.say(texto)  # Convertir texto a voz
    motor_voz.runAndWait()  # Esperar a que termine de hablar

