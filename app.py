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


#Ver mic
#for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
    #print(f"Micrófono disponible: {index}: {name}")


# Ejemplo de hablar un mensaje
#voz.say("asdf")
#voz.runAndWait()

while True:
    with speech_recognition.Microphone(device_index=mic_id) as fuente:
        print("Calibrando el micrófono... por favor guarda silencio.")
        reconocedor.adjust_for_ambient_noise(fuente)  # Para calibrar en ambientes ruidosos
        print("Escuchando...")
        audio = reconocedor.listen(fuente)
        try:
            # Reconocer la voz utilizando Google
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {texto}")

            # Reproducir el texto reconocido usando pyttsx3
            voz.say(f"Has dicho: {texto}")
            voz.runAndWait()

        except speech_recognition.UnknownValueError:
            print("No he entendido lo que dijiste.")
            voz.say("No he entendido lo que dijiste.")
            voz.runAndWait()

        except speech_recognition.RequestError:
            print("No se pudo conectar al servicio de reconocimiento.")
            voz.say("No se pudo conectar al servicio de reconocimiento.")
            voz.runAndWait()