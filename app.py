from comandos import *
# Función para entender y ejecutar comandos #
def Entender_Comandos(texto):
    texto = texto.lower()

    for palabras_clave, funcion in comandos.items():
        if any(palabra in texto for palabra in palabras_clave):
            return funcion()  # Ejecuta la función correspondiente

    print("No tengo un comando para eso.")
    voz.say("No tengo un comando para eso.")
    voz.runAndWait()
    return True  # Continuar el bucle

# Bucle principal #
while True:
    with sr.Microphone(device_index=mic_id) as fuente:
        reconocedor.adjust_for_ambient_noise(fuente)  # Calibrar en ambientes ruidosos
        print("Escuchando...")
        audio = reconocedor.listen(fuente)

        try:
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {texto}")

            # Procesar el comando con la función
            if not Entender_Comandos(texto):
                break  # Salir del bucle si la función retorna False

        except sr.UnknownValueError:
            print("No he entendido lo que dijiste.")
            voz.say("No he entendido lo que dijiste.")
            voz.runAndWait()

        except sr.RequestError:
            print("No se pudo conectar al servicio de reconocimiento.")
            voz.say("No se pudo conectar al servicio de reconocimiento.")
            voz.runAndWait()
