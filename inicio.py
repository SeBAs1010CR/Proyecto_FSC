import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os
from estadisticasvent import mostrar_estadisticas
from Configuracion import mostrar_config


Jugar = "Ventanadejugadores.py"

"Una clase para que funcione el gif"
class AnimaciondeGIF(tk.Label):#clase
    def __init__(self, master, gif_frames, delay=40): 
        self.frames = gif_frames #es un contador de cuadros o Frames
        self.delay = delay
        self.index = 0
        super().__init__(master)
        self.act_anim()

    def act_anim(self): #metodo de la clase
        self.config(image=self.frames[self.index]) #se actualiza el widget Label con el siguiente cuadro del gif
        self.index = (self.index + 1) % len(self.frames) #aca se incrementa el indice para mnostrar el siguientre cuadro y si es mas largo que len entonces vuelve a 0
        #próxima actualización del cuadro
        self.after(self.delay, self.act_anim)

def obtener_cuadrosps(img): #iteracion para obtener frames
    with Image.open(img) as gif:
        indice = 0
        cuadros = []
        while True:
            try:
                gif.seek(indice)
                cuadro = ImageTk.PhotoImage(gif)
                cuadros.append(cuadro)
            except EOFError:
                break
            indice += 1
        return cuadros

"Ventana principal del juego"
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Futbolito")
    ventana.minsize(1500, 700)
    ventana.maxsize(1500, 700)
    ventana.configure(background="black")

    ruta_gif_inicio = os.path.join(os.path.dirname(__file__), 'imagenes', 'Inicio.gif')
    gif_frames = obtener_cuadrosps(ruta_gif_inicio)

    animated_label = AnimaciondeGIF(ventana, gif_frames)
    animated_label.pack()

    def volver(pag):
        """
        Vuelve a la pag principa;l
        """
        # Cerrar la ventana actual y volver a la principal
        pag.destroy()  # Cierra la ventana actual
        ventana.deiconify()

    def acercade():
        """
        una ventrana con los creadores del juego.
        """
        acercade = tk.Toplevel()
        ventana.iconify()
        acercade.title("Acerca de")
        acercade.minsize(600, 600)
        acercade.maxsize(600, 600)
        acercade.configure(background="black")


        ruta_imagenacercade = os.path.join(os.path.dirname(__file__), 'Imagenes', 'acercade.png')
        imagenacercade = Image.open(ruta_imagenacercade)
        imagenacercade_tk = ImageTk.PhotoImage(imagenacercade)

        label4 = tk.Label(acercade, image=imagenacercade_tk)
        label4.image = imagenacercade_tk
        label4.pack()

        boton_volver = tk.Button(acercade, text="Volver", width=10, height=2, bg="Yellow", fg="Black",
                                 font=("fixedsys", 16), command=lambda: volver(acercade))
        boton_volver.place(x=70, y=470)
    def Jugarfutbolito():
        ventana.iconify()
        subprocess.Popen(["python", Jugar])
    #Botones
    boton_acercade = tk.Button(ventana, text="Acerca De", width=20, height=1, bg="Yellow", fg="Black",
                               font=("fixedsys", 17), command=acercade)
    boton_acercade.place(x=60, y=625)

    boton_estadisticas = tk.Button(ventana, text="Estadísticas", width=20, height=1, bg="Yellow", fg="Black",
                               font=("fixedsys", 17), command=mostrar_estadisticas)
    boton_estadisticas.place(x=400, y=625)

    boton_config = tk.Button(ventana, text="Configuración", width=20, height=1, bg="Yellow", fg="Black",
                               font=("fixedsys", 17), command=mostrar_config)
    boton_config.place(x=740, y=625)

    boton_jugar = tk.Button(ventana, text="Jugar", width=20, height=1, bg="Red", fg="Black",
                               font=("fixedsys", 17), command=Jugarfutbolito)
    boton_jugar.place(x=1080, y=625)




    ventana.mainloop()

ventana_principal()