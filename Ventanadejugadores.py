import pygame
import os
import random
from Clases.Instancias import *
import subprocess



##########Globales
x = -350
y = 0
equipo_actual = 0 
switch1 = True
switch2 = True
switch3 = False
artillero = None
portero_actual = 0
artillero_actual = 0
mostrar_portero = False
mostrar_artillero = False
mostrar_equipo = False
mostrar_escudo = True
bloquearpotenciometro = False
empezar_juego = False




def dibujar_escudos(ventana, equipos, x, y, equipo_actual):
    if mostrar_escudo:
        ventana.blit(imagen_fondo, (-350,0)) 
        for i, equipo in enumerate(equipos):
            if i == equipo_actual:
                escudo_img = pygame.image.load(equipo.escudo)
                ventana.blit(escudo_img, (x, y))
                break 

def dibujar_porteros(ventana, porteros, x, y, portero_actual, mostrar_portero):
    if mostrar_portero:
        ventana.blit(imagen_fondo, (-350,0)) 
        for i, portero in enumerate(porteros):
            if i == portero_actual:
                portero_img = pygame.image.load(portero.portero_imagen)
                ventana.blit(portero_img, (x, y))
                break 

def dibujar_artilleros(ventana, artilleros, x, y, artillero_actual, mostrar_artillero):
    if mostrar_artillero:
        ventana.blit(imagen_fondo, (-350,0)) 
        for i, artillero in enumerate(artilleros):
            if i == artillero_actual:
                artillero_img = pygame.image.load(artillero.artillero_imagen)
                ventana.blit(artillero_img, (x, y))
                break

def dibujar_equipo(ventana, artilleros, x, y, artillero_actual, portero_actual, mostrar_equipo):
    if mostrar_equipo:
        ventana.blit(imagen_fondo, (-350,0))  
        
       
        for i, artillero in enumerate(artilleros):
            if i == artillero_actual:
                artillero_img = pygame.image.load(artillero.artillero_imagen)
                pygame.draw.rect(ventana, (255, 255, 255), (x, y, 150, 150), 0)  
                ventana.blit(artillero_img, (-550, y+200))
                break
        
       
        for i, portero in enumerate(porteros):
            if i == portero_actual:
                portero_img = pygame.image.load(portero.portero_imagen)
                pygame.draw.rect(ventana, (255, 255, 255), (x + 200, y, 150, 150), 0)  
                ventana.blit(portero_img, (-150, y+260))
                break 
        
        
        global equipo_actual  
        escudo_img = pygame.image.load(equipos[equipo_actual].escudo)
        pygame.draw.rect(ventana, (255, 255, 255), (800, y, 150, 150), 0) 
        ventana.blit(escudo_img, (-350, y-170))
        print("Dar tecla Espacio")



def guardar_equipo_1():
    with open('equipo_1.txt', 'w') as archivo:
        archivo.write(f"Nombre: {Equipo_1.nombre}, ")
        archivo.write(f"Portero: {porteros[Equipo_1.portero].nombre}, ")
        archivo.write(f"Artillero: {artilleros[Equipo_1.jugador].nombre}, ")
        archivo.write(f"VisLoc: {Equipo_1.VisLoc}")
    print('Se cargo correctamente')




pygame.init()
ANCHO = 800
ALTO = 700
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dibujar Escudos")

####################################### Cargar imágenes de la moneda, el escudo y la corona#######################################################################
ruta_imagen_fondo_jugadores1 = os.path.join("Imagenes", "ventjugadores.png")  
imagen_fondo = pygame.image.load(ruta_imagen_fondo_jugadores1).convert()
Ventana2 = "Ventanadejugadores2.py"

######################################Varaibles###############################
ruta_coin = os.path.join("Imagenes", "coin.gif")
coin_img = pygame.image.load(ruta_coin)
Escudo = os.path.join("Imagenes", "coinlocal.png")
Corona = os.path.join("Imagenes", "coinvisitante.png")

Visitante = pygame.image.load(Corona)
Local = pygame.image.load(Escudo)

contador = 0
juegoplay = False
bandera = False
mostrado = False

x_moneda = ANCHO // 2 - coin_img.get_width() // 2
y_moneda = 500  
velocidad_y = 3000

equipos = [MIL, JUV, RIV]#instyancias
indices_equipos = list(range(len(equipos)))
porteros = [Max, Ben, Ava]
artilleros = [Dan, leo, sam]
######################################Varaibles###############################

def crear_instancia_equipo():
    global Equipo_1
    equipo_seleccionado = equipos[equipo_actual]
    Equipo_1 = Equipo(equipo_seleccionado.nombre , equipo_actual, portero_actual, artillero_actual)
    print("Equipo:")
    print("Nombre:", Equipo_1.nombre)
    print("Portero:", Equipo_1.portero)
    print("Artillero:", Equipo_1.jugador)
    print("VisLoc:", Equipo_1.VisLoc)
    
    ######Piclk 

# Bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and bloquearpotenciometro == False:
                    if switch1 == True:
                        equipo_actual = (equipo_actual - 1) % len(equipos)
                    elif switch1 == False and switch2 == False:
                        portero_actual = (portero_actual - 1) % len(porteros)
                    elif switch1 == False and switch2 == True:
                        artillero_actual = (artillero_actual - 1) % len(artilleros)
                        switch3 = True
                
                elif event.key == pygame.K_RIGHT and bloquearpotenciometro == False:
                    if switch1 == True:
                        equipo_actual = (equipo_actual + 1) % len(equipos)
                    elif switch1 == False and switch2 == False:
                        portero_actual = (portero_actual + 1) % len(porteros)
                    elif switch1 == False and switch2 == True:
                        artillero_actual = (artillero_actual + 1) % len(artilleros)
                        switch3 = True

                ####Tecla Enter
                #seleccion de equipo
                elif event.key == pygame.K_e: 
                    switch2 = not switch2  
                    switch1 = False
                    #seleccion de portero
                    if switch2 == False and switch1 == False:
                        mostrar_portero = True
                    #seleccion de artillero
                    if switch2 == True and switch1 == False:
                        mostrar_artillero = True
                    #da inicio juego
                    if switch3 == True: 
                        mostrar_equipo = True
                        bloquearpotenciometro = True
                        crear_instancia_equipo()
                    #esta parte es para lanzar la moneda, son switch para desaparecer las imagenes
                if event.key == pygame.K_SPACE:
                        empezar_juego = True
                        mostrar_equipo = False
                        mostrar_artillero = False
                        mostrar_portero = False
                        mostrar_escudo = False
                    

    if empezar_juego == True:
            ventana.blit(imagen_fondo, (-350,0))
            # Calcular el tiempo transcurrido desde el último fotograma en segundos
            dt = pygame.time.Clock().tick(60) / 1000.0

        
            if contador < 100 and bandera == False:
                y_moneda -= velocidad_y * dt
                contador += 1
       

            elif bandera == False:
                y_moneda += velocidad_y * dt
                contador +=1
     
        
            if contador >= 100:
                if y_moneda >= ALTO:
                    y_moneda = -4000
                    

            
            if contador <= 200:
                ventana.blit(coin_img, (x_moneda, int(y_moneda))) 


            if contador >= 200 and y_moneda >= 100 and juegoplay == False:
                if not mostrado:
                    resul = random.choice([Visitante, Local])
                    ventana.blit(resul, (ANCHO // 2 - resul.get_width() // 2, ALTO // 2 - resul.get_height() // 2))
                    equiposegunmoneda = resul
                    mostrado = True
                    pygame.display.flip() 
                    pygame.time.delay(2000)
                if resul == Visitante:
                    Equipo_1.VisLoc = 'Visitante'
                    print("Equipo:")
                    print("Nombre:", Equipo_1.nombre)
                    print("Portero:", Equipo_1.portero)
                    print("Artillero:", Equipo_1.jugador)
                    print("VisLoc:", Equipo_1.VisLoc)
                    guardar_equipo_1()


                
                    
                if resul == Local:
                    Equipo_1.VisLoc = 'Local'  
                    print("Equipo:")
                    print("Nombre:", Equipo_1.nombre)
                    print("Portero:", Equipo_1.portero)
                    print("Artillero:", Equipo_1.jugador)
                    print("VisLoc:", Equipo_1.VisLoc)
                    guardar_equipo_1()
            if contador == 300:
                bandera = True
                juegoplay = True
                guardar_equipo_1()
                pygame.quit()
                subprocess.Popen(["python", Ventana2])

                        
   
    dibujar_escudos(ventana, equipos, x, y, equipo_actual)
    dibujar_porteros(ventana, porteros, x, y, portero_actual, mostrar_portero)
    dibujar_artilleros(ventana, artilleros, x, y, artillero_actual, mostrar_artillero)
    dibujar_equipo(ventana, artilleros, x, y, artillero_actual, portero_actual, mostrar_equipo)
    
    pygame.display.flip()


    







pygame.quit()  