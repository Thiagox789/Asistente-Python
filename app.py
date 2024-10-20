from comandos import *
import tkinter as tk
from tkinter import messagebox, font

def reconocer_voz():
    with sr.Microphone() as fuente:
        reconocedor.adjust_for_ambient_noise(fuente)  # Calibrar en ambientes ruidosos
        print("Escuchando...")
        voz.say("Escuchando, por favor habla.")
        voz.runAndWait()
        audio = reconocedor.listen(fuente)
        try:
            texto = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {texto}")
            # Procesar el comando
            Entender_Comandos(texto)
        except sr.UnknownValueError:
            voz.say("No he entendido lo que dijiste.")
            voz.runAndWait()
        except sr.RequestError:
            voz.say("No se pudo conectar al servicio de reconocimiento.")
            voz.runAndWait()

# Crear ventana principal de Tkinter
root = tk.Tk()
root.title("Control de Voz")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Color de fondo de la ventana

# Crear un marco para organizar los elementos
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Título de la aplicación
titulo_font = font.Font(family="Arial", size=16, weight="bold")
titulo = tk.Label(frame, text="Control de Voz", font=titulo_font, bg="#f0f0f0")
titulo.pack(pady=10)

# Crear botones con estilo
btn_reconocer = tk.Button(frame, text="Iniciar Reconocimiento de Voz", command=reconocer_voz, 
                          bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
btn_reconocer.pack(pady=10)

btn_salir = tk.Button(frame, text="Salir", command=salir, 
                      bg="#f44336", fg="white", font=("Arial", 12), padx=10, pady=5)
btn_salir.pack(pady=10)

# Iniciar el bucle de eventos de Tkinter
root.mainloop()