import speech_recognition  
import pyttsx3
import subprocess
import webbrowser

#Variables#
mic_id = 1
voz = pyttsx3.init()
reconocedor = speech_recognition.Recognizer()

voz.setProperty('rate', 150)  # Velocidad de habla
voz.setProperty('volume', 1)  # Volumen (entre 0.0 y 1.0)


def Entender_Comandos(texto):
    texto = texto.lower()  # Convertir a minúsculas para evitar problemas de comparación

    if "salir" in texto or "salir del programa" in texto or "salir de la app" in texto:
        print("Saliendo...")
        voz.say("Adiós Thiago")
        voz.runAndWait()
        return False  # Salir del programa

    elif "abrir firefox" in texto or "abrir navegador" in texto or "abrir chrome" in texto:
        print("Abriendo el mejor navegador")
        voz.say("Abriendo el mejor navegador")
        voz.runAndWait()
        subprocess.Popen(["start", "firefox"], shell=True)  # Cambia "chrome" si es necesario
        return True

    elif "abrir youtube" in texto:
        print("Abriendo YouTube")
        voz.say("Abriendo YouTube")
        voz.runAndWait()
        webbrowser.open("https://www.youtube.com")
        return True

    else:
        print("No tengo un comando para eso.")
        voz.say("No tengo un comando para eso.")
        voz.runAndWait()
        return True  # Mantener el bucle activo
while True:
    with speech_recognition.Microphone(device_index=mic_id) as fuente:
        reconocedor.adjust_for_ambient_noise(fuente)  # Calibrar en ambientes ruidosos
        print("Escuchando...")
        audio = reconocedor.listen(fuente)

        try:
            # Reconocer la voz utilizando Google
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {texto}")

            # Procesar el comando con la función
            if not Entender_Comandos(texto):
                break  # Salir del bucle si la función retorna False

        except speech_recognition.UnknownValueError:
            print("No he entendido lo que dijiste.")
            voz.say("No he entendido lo que dijiste.")
            voz.runAndWait()

        except speech_recognition.RequestError:
            print("No se pudo conectar al servicio de reconocimiento.")
            voz.say("No se pudo conectar al servicio de reconocimiento.")
            voz.runAndWait()