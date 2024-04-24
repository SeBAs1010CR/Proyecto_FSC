import tkinter as tk


elegirjugadores = False

Ventana_Config = tk.Tk()
Ventana_Config.title("Configuracion")
Ventana_Config.minsize(300, 300)
Ventana_Config.maxsize(300, 300)
Ventana_Config.configure(background="black")


def Manual():
    global elegirjugadores
    boton_manual.cget("bg")
    boton_auto.config(bg="white")
    elegirjugadores = True
    print(elegirjugadores)
    boton_manual.config(bg="yellow")



def Automatico():
    global elegirjugadores
    boton_auto.cget("bg")
    boton_manual.config(bg="white")
    elegirjugadores = False
    print(elegirjugadores)
    boton_auto.config(bg="yellow")



















boton_auto = tk.Button(Ventana_Config, text="Automatico", bg="white", fg="black", command=Automatico)
boton_auto.pack(pady=20)


boton_manual = tk.Button(Ventana_Config, text="Manual", bg="white", fg="black", command=Manual)
boton_manual.pack(pady=20)

# Ejecutar el bucle principal de Tkinter
Ventana_Config.mainloop()

