from Funciones_y_Importantes import *

while True:
    with sr.Microphone(device_index=mic_id) as fuente:
        print("Escuchando...")
        audio = reconocedor.listen(fuente)
        try:
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {texto}")

            # Ejecutar comandos
            for comando in comandos:
                if comando in texto.lower():  # Comparar en minúsculas para facilitar la comparación
                    respuesta = comandos[comando]  # Ejecutar el comando correspondiente
                    print(respuesta)
                    hablar(respuesta)  # Hacer que el asistente hable
                    break
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
