import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
from Funciones_y_Importantes import *

motor_voz = pyttsx3.init()

def hablar(texto):
    motor_voz.say(texto)
    motor_voz.runAndWait()

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

while True:
    with sr.Microphone(device_index=mic_id) as fuente:
        print("Escuchando...")
        audio = reconocedor.listen(fuente)
        try:
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {texto}")

            # Ejecutar comandos
            for comando in comandos:
                if comando in texto.lower():
                    respuesta = comandos[comando]
                    print(respuesta)
                    hablar(respuesta)
                    
                    if comando == "salir":
                        print("Saliendo del asistente.")
                        hablar("Saliendo del asistente.")
                        exit()
                    if comando == "abre navegador":
                        subprocess.Popen(["start", "chrome"], shell=True)  # Cambia "chrome" según tu navegador
                    if comando == "abrir youtube":
                        webbrowser.open("https://www.youtube.com")  # Abre YouTube
                    break
            else:
                # Responder preguntas frecuentes
                for pregunta in preguntas_frecuentes:
                    if pregunta in texto.lower():
                        respuesta = preguntas_frecuentes[pregunta]
                        print(respuesta)
                        hablar(respuesta)
                        break
                else:
                    # Buscar en la web
                    if "buscar" in texto.lower():
                        consulta = texto.lower().replace("buscar", "").strip()
                        if consulta:
                            respuesta = "Abriendo tu búsqueda en la web."
                            print(respuesta)
                            hablar(respuesta)
                            webbrowser.open(f"https://www.google.com/search?q={consulta}")
                        else:
                            respuesta = "¿Qué deseas buscar?"
                            print(respuesta)
                            hablar(respuesta)
                    else:
                        respuesta = "No tengo un comando para eso."
                        print(respuesta)
                        hablar(respuesta)

        except sr.UnknownValueError:
            respuesta = "No he entendido lo que dijiste."
            print(respuesta)
            hablar(respuesta)
        except sr.RequestError:
            respuesta = "No se pudo conectar al servicio de reconocimiento."
            print(respuesta)
            hablar(respuesta)
