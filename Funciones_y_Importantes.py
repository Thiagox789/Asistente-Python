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
    "Abrir youtube" "Abriendo youtube capo :)"
}

def hablar(texto):
    motor_voz.say(texto)  # Convertir texto a voz
    motor_voz.runAndWait()  # Esperar a que termine de hablar

comandos = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte?",
    "abre navegador": "Abriendo el navegador.",
    "cierra navegador": "Cerrando el navegador.",
    "salir": "Saliendo del asistente.",
    "abrir youtube": "Abriendo YouTube.",  # Nuevo comando para abrir YouTube
}

preguntas_frecuentes = {
    "qué es la inteligencia artificial": "La inteligencia artificial es una rama de la informática que se ocupa de crear sistemas que imitan la inteligencia humana.",
    "quién es el presidente de argentina": "El presidente de Argentina es Javier Milei.",
}