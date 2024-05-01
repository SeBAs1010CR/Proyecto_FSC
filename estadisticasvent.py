import tkinter as tk

switch = False
def mostrar_estadisticas():
    ventana = tk.Tk()
    ventana.title("Estadísticas del Partido")
    ventana.configure(bg="black")  


    ventana.geometry("400x300")


    marco = tk.Frame(ventana, bg="Black", padx=20, pady=100) 
    marco.pack()


    with open("estadisticas.txt", "r") as archivo:
        lineas = archivo.readlines()


    for i in range(0, len(lineas), 3):
        equipo = lineas[i].strip()
        tiros = lineas[i+1].strip()
        goles = lineas[i+2].strip()


        etiqueta_equipo = tk.Label(marco, text=equipo, padx=10, bg="Black", fg="white")  
        etiqueta_tiros = tk.Label(marco, text=tiros, padx=10, bg="Black", fg="white")  
        etiqueta_goles = tk.Label(marco, text=goles, padx=10, bg="Black", fg="white")  

        
        etiqueta_equipo.grid(row=i, column=0, sticky="w") 
        etiqueta_tiros.grid(row=i, column=1, sticky="w")   
        etiqueta_goles.grid(row=i, column=2, sticky="w")   

    ventana.mainloop()

