import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser

# Variables #
mic_id = 1
voz = pyttsx3.init()
reconocedor = sr.Recognizer()

voz.setProperty('rate', 150)  # Velocidad de habla
voz.setProperty('volume', 1)  # Volumen (entre 0.0 y 1.0)

# Funciones para acciones #
def salir():
    print("Saliendo...")
    voz.say("Adiós Thiago")
    voz.runAndWait()
    return False  # Termina el programa

def abrir_firefox():
    print("Abriendo el mejor navegador")
    voz.say("Abriendo el mejor navegador")
    voz.runAndWait()
    subprocess.Popen(["start", "firefox"], shell=True)
    return True

def abrir_youtube():
    print("Abriendo YouTube")
    voz.say("Abriendo YouTube")
    voz.runAndWait()
    webbrowser.open("https://www.youtube.com")
    return True

# Diccionario de comandos #
comandos = {
    ("salir", "salir del programa", "salir de la app"): salir,
    ("abrir firefox", "abrir navegador", "abrir chrome"): abrir_firefox,
    ("abrir youtube",): abrir_youtube
}