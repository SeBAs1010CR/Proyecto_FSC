import random
import pygame
import os
import time
from estadisticasvent import mostrar_estadisticas
from Clases.Instancias import *


with open("configuracion.txt", "r") as archivo:
    contenido = archivo.read().strip()
###########Globales
Numerodetirolocal = 0
Numerodetiro = 0
goles_equipo1 = 0
goles_equipo2 = 0
local = True
nombre_equipo = ""
nombre_portero = ""
nombre_artillero = ""
nombre_equipo2 = ""
nombre_portero2 = ""
nombre_artillero2 = ""
nombre_equipo2
estbandera = False
temporizador_inicio = 0
yen = False
Estado = contenido
def detener_programa():
    global estbandera
    if Numerodetirolocal == 5:
        pygame.draw.rect(ventana, "Grey", (300, 580, 600, 50))
        pygame.draw.rect(ventana, "White", (300, 580, 600, 50), 3)
        pygame.draw.rect(ventana, "Black", (325, 590, 550, 30))
        fuente = pygame.font.SysFont(None, 36)
        texto = fuente.render("Presione para finalizar el juego", True, "White")  
        ventana.blit(texto, (400, 592))
        estbandera = True



def iniciar_temporizador():
    global temporizador_inicio
    temporizador_inicio += 1
    print(temporizador_inicio)

def reproducir_sonido_silbato_inicial():###########esto tengo que ver como hago para que suene el silbataso luego de 5s

    #if silbataso == False:
        silbato_sound = pygame.mixer.Sound("Sonidos/silbato.wav")  
        
    
        silbato_sound.play()

pygame.init()

# Dimensiones de la ventana
ANCHO = 1200
ALTO = 650


ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

ruta_imagen_fondo = os.path.join("Imagenes", "cancha.png")  
imagen_fondo = pygame.image.load(ruta_imagen_fondo).convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 500))  





###################################################SONIDOS################################

def reproducir_sonido_silbato():
    global yen
    yen = True
    silbato_sound = pygame.mixer.Sound("Sonidos/silbato.wav")  
    silbato_sound.play()
    return pygame.time.get_ticks()

def reproducir_sonido_inicio():
    
    silbato_sound = pygame.mixer.Sound("Sonidos/inicio.wav") 
    silbato_sound.play()
    time.sleep(5)
    reproducir_sonido_silbato()


def segundoslocal():
    global temporizador_inicio
    global local
    if temporizador_inicio == 70:
        temporizador_inicio = 0
        local = False
        dibujar_tiro_local(1300, 530, False, Numerodetirolocal)
        reproducir_sonido_abucheo()
        pygame.time.delay(8000)
        reproducir_sonido_silbato()

def segundosVis():
    global temporizador_inicio
    global local
    if temporizador_inicio == 70:
        local = True
        temporizador_inicio = 0
        dibujar_tiro(1300, 530, False, Numerodetiro)
        reproducir_sonido_abucheo()
        pygame.time.delay(8000)
        reproducir_sonido_silbato()

def reproducir_sonido_abucheo():
    silbato_sound = pygame.mixer.Sound("Sonidos/abucheo.wav")  
    silbato_sound.play()

def reproducir_sonido_gol():
    silbato_sound = pygame.mixer.Sound("Sonidos/gol.wav") 
    silbato_sound.play()


def cargar_estadisticas():

    with open('estadisticas.txt', 'w') as archivo:
        archivo.write(str(nombre_equipo) + "\n")
        archivo.write("Tiros: " + str(Numerodetiro) + "\n")
        archivo.write("Goles: " + str(goles_equipo1) + "\n")
        archivo.write(str(nombre_equipo2) + "\n")
        archivo.write("Tiros: " + str(Numerodetirolocal) + "\n")
        archivo.write("Goles: " + str(goles_equipo2) + "\n")
        
    





Escudo_MIL = os.path.join(os.path.dirname(__file__),'Imagenes', 'emil.png')
Escudo_JUV = os.path.join(os.path.dirname(__file__), 'Imagenes', 'ejuv.png')
Escudo_RIV = os.path.join(os.path.dirname(__file__), 'Imagenes', 'erp.png')

def dibujar_escudos(ventana, equipo, x, y): 
        escudo_img = pygame.image.load(equipo)
        escudo_img = pygame.transform.scale(escudo_img, (1200, 550))
        ventana.blit(escudo_img, (x, y))

def dibujar_escudos2(ventana, equipo, x, y): 
        escudo_img2 = pygame.image.load(equipo)
        escudo_img2 = pygame.transform.scale(escudo_img2, (1200, 550))
        ventana.blit(escudo_img2, (x, y))


    
def logo2(nombre_equipo2, local_o_visitante2):
    if nombre_equipo2 == 'Juventus'and local_o_visitante2 == 'Local':
        return dibujar_escudos2(ventana, Escudo_JUV, -480, -140)
    elif nombre_equipo2 == 'Juventus'and local_o_visitante2 == 'Visitante':
        return dibujar_escudos2(ventana, Escudo_JUV, 500, -140)
    elif nombre_equipo2 == 'River Plate'and local_o_visitante2 == 'Local':
        return dibujar_escudos2(ventana, Escudo_RIV, -480, -140)
    elif nombre_equipo2 == 'River Plate'and local_o_visitante2 == 'Visitante':
        return dibujar_escudos2(ventana, Escudo_RIV, 500, -140)
    elif nombre_equipo2 == 'Milan'and local_o_visitante2 == 'Local':
        return dibujar_escudos2(ventana, Escudo_MIL, -480, -140)
    elif nombre_equipo2 == 'Milan'and local_o_visitante2 == 'Visitante':
        return dibujar_escudos2(ventana, Escudo_MIL, 500, -140)
###------------------------------------------archivos--------------------------------------------------------------------------------------------###
def cargar_equipo():
    global nombre_equipo
    with open("equipo_1.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(", ")
            for parte in partes:
                clave, valor = parte.split(": ")
                if clave == "Nombre":
                    nombre_equipo = valor
                elif clave == "Portero":
                    nombre_portero = valor
                elif clave == "Artillero":
                    nombre_artillero = valor
                elif clave == "VisLoc":
                    local_o_visitante = valor
    return logo2(nombre_equipo, local_o_visitante) 
def cargar_equipo2():
    global nombre_equipo2
    global nombre_artillero2
    global nombre_portero2
    with open("equipo_2.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(", ")
            for parte in partes:
                clave, valor = parte.split(": ")
                if clave == "Nombre":
                    nombre_equipo2 = valor
                elif clave == "Portero":
                    nombre_portero2 = valor
                elif clave == "Artillero":
                    nombre_artillero2 = valor
                elif clave == "VisLoc":
                    local_o_visitante2 = valor
    return logo2(nombre_equipo2, local_o_visitante2) 

    

###------------------------------------------archivos--------------------------------------------------------------------------------------------###

Paletas = ["z", "x", "c", "v", "b", "n"]

def seleccionar_indice_portero(Paletas):
    indice = random.choice(["AN1", "AN2", "AN3"])
    if indice == "AN1":
        teclas = random.choice([Paletas[:2], Paletas[2:4], Paletas[4:]])
    elif indice == 'AN2':
        teclas = random.choice([Paletas[:3], Paletas[3:]])
    elif indice == 'AN3':
        teclas = random.choice([Paletas[::2], Paletas[1::2]])
    print('La combinacion aleatoria es:', indice, teclas)
    return indice, teclas

def dibujar_tiro(x, y, es_gol, NUMERO_DE_TIRO):
    global goles_equipo1 
    if es_gol:
        goles_equipo1 += 1
        color = (0, 255, 0)  # Verde si es gol
        if NUMERO_DE_TIRO == 0:
            x = 1088
            y = 380
        if NUMERO_DE_TIRO == 1:
            x = 1088
            y = 430
        if NUMERO_DE_TIRO == 2:
            x = 1088
            y = 480
        if NUMERO_DE_TIRO == 3:
            x = 1088
            y = 530
        if NUMERO_DE_TIRO == 4:
            x = 1088
            y = 580
        
    else:
        color = (255, 0, 0)  # Rojo si no es gol
        if NUMERO_DE_TIRO == 0:
            x = 1088
            y = 380
        if NUMERO_DE_TIRO == 1:
            x = 1088
            y = 430
        if NUMERO_DE_TIRO == 2:
            x = 1088
            y = 480
        if NUMERO_DE_TIRO == 3:
            x = 1088
            y = 530
        if NUMERO_DE_TIRO == 4:
            x = 1088
            y = 580
    pygame.draw.circle(ventana, color, (x, y), 20)

def dibujar_tiro_local(x, y, es_gol, NUMERO_DE_TIRO):
    global goles_equipo2

    if es_gol:
        goles_equipo2 += 1
        color = (0, 255, 0)  # Verde si es gol
        if NUMERO_DE_TIRO == 0:
            x = 100
            y = 380
        if NUMERO_DE_TIRO == 1:
            x = 100
            y = 430
        if NUMERO_DE_TIRO == 2:
            x = 100
            y = 480
        if NUMERO_DE_TIRO == 3:
            x = 100
            y = 530
        if NUMERO_DE_TIRO == 4:
            x = 100
            y = 580
        
    else:
        color = (255, 0, 0)  # Rojo si no es gol
        if NUMERO_DE_TIRO == 0:
            x = 100
            y = 380
        if NUMERO_DE_TIRO == 1:
            x = 100
            y = 430
        if NUMERO_DE_TIRO == 2:
            x = 100
            y = 480
        if NUMERO_DE_TIRO == 3:
            x = 100
            y = 530
        if NUMERO_DE_TIRO == 4:
            x = 100
            y = 580
            
    pygame.draw.circle(ventana, color, (x, y), 20)


tiempo_ultimo_pitido = 0
def verificar_tecla_presionada():
    global Numerodetiro
    global local
    local = True
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[pygame.K_x]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "x" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro(1100, 560, True, Numerodetiro)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro(1100, 530, False, Numerodetiro)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_z]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "z" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro(1300, 560, True, Numerodetiro)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro(1300, 530, False, Numerodetiro)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_c]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "c" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro(1300, 560, True, Numerodetiro)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro(1300, 530, False, Numerodetiro)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_v]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "v" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro(1300, 560, True, Numerodetiro)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro(1300, 530, False, Numerodetiro)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_b]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "b" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro(1300, 560, True, Numerodetiro)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro(1300, 530, False, Numerodetiro)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_n]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "n" not in teclas_seleccionadas:
            
            print("¡Gooool!")
            dibujar_tiro(1300, 560, True, Numerodetiro)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            
            print("No es gol")
            dibujar_tiro(1300, 530, False, Numerodetiro)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()



def verificar_tecla_presionada_Local():
    global Numerodetirolocal
    global local
    local = False
    tecla_presionada = pygame.key.get_pressed()
    
    if tecla_presionada[pygame.K_x]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "x" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro_local(10, 560, True, Numerodetirolocal)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro_local(10, 530, False, Numerodetirolocal)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_z]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "z" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro_local(10, 560, True, Numerodetirolocal)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro_local(10, 530, False, Numerodetirolocal)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_c]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "c" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro_local(10, 560, True, Numerodetirolocal)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro_local(10, 530, False, Numerodetirolocal)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_v]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "v" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro_local(10, 560, True, Numerodetirolocal)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro_local(10, 530, False, Numerodetirolocal)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_b]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "b" not in teclas_seleccionadas:
            print("¡Gooool!")
            dibujar_tiro_local(10, 560, True, Numerodetirolocal)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            print("No es gol")
            dibujar_tiro_local(10, 530, False, Numerodetirolocal)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()


    elif tecla_presionada[pygame.K_n]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "n" not in teclas_seleccionadas:
            
            print("¡Gooool!")
            dibujar_tiro_local(10, 560, True, Numerodetirolocal)
            reproducir_sonido_gol()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()
        else:
            
            print("No es gol")
            dibujar_tiro_local(10, 530, False, Numerodetirolocal)
            reproducir_sonido_abucheo()
            pygame.time.delay(8000)
            reproducir_sonido_silbato()

####==========================================================================posiiciones====================================================###
def obtener_coordenadas_mouse():
    return pygame.mouse.get_pos()
####==============================================================================================================================###

def juego():
    global Numerodetiro
    global goles_equipo1
    global goles_equipo2
    global local
    global Numerodetirolocal
    global estbandera
    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if local == False:
                        verificar_tecla_presionada()
                        Numerodetiro += 1
                    else:
                        verificar_tecla_presionada_Local()
                        Numerodetirolocal += 1
                elif event.key == pygame.K_z:
                    verificar_tecla_presionada()
                    Numerodetiro += 1
                elif event.key == pygame.K_c:
                    verificar_tecla_presionada()
                    Numerodetiro += 1
                elif event.key == pygame.K_v:
                    verificar_tecla_presionada()
                    Numerodetiro += 1
                elif event.key == pygame.K_b:
                    verificar_tecla_presionada()
                    Numerodetiro += 1
                elif event.key == pygame.K_n:
                    verificar_tecla_presionada()
                    Numerodetiro += 1
                elif event.key == pygame.K_SPACE and estbandera == True:
                    pygame.quit()
                    mostrar_estadisticas()
        
        ventana.blit(imagen_fondo, (200, 50))

#################################################Informaci'on en pantalla#########################
        pygame.draw.rect(ventana, (0, 0, 0), (1050, 320, 200, 40))
        fuentetiro = pygame.font.SysFont(None, 36)  
        textotiro = fuentetiro.render(f"Tiro: {Numerodetiro}", True, (255, 255, 255))
        ventana.blit(textotiro, (1050, 320))

        pygame.draw.rect(ventana, (0, 0, 0), (620, 10, 200, 40))
        fuentegol = pygame.font.SysFont(None, 36)  
        textogol = fuentegol.render(f"Goles: {goles_equipo1}", True, (255, 255, 255))
        ventana.blit(textogol, (620, 14))

        pygame.draw.rect(ventana, (0, 0, 0), (50, 320, 100, 40))
        fuentetiro2 = pygame.font.SysFont(None, 36)  
        textotiro2 = fuentetiro2.render(f"Tiro: {Numerodetirolocal}", True, (255, 255, 255))
        ventana.blit(textotiro2, (50, 320))

        pygame.draw.rect(ventana, (0, 0, 0), (477, 10, 140, 40))
        fuentegol2 = pygame.font.SysFont(None, 36)  
        textogol2 = fuentegol2.render(f"Goles: {goles_equipo2}", True, (255, 255, 255))
        ventana.blit(textogol2, (477, 14))
#################################################Informaci'on en pantalla#########################


        pygame.draw.line(ventana, (255, 255, 255), (600, 2), (600, min(50, ALTO - 10)), 3)







        
        if Estado == "Auto":    
            if local == False:
                segundosVis()
            else:
                segundoslocal()
            pygame.display.flip()
            if yen == True:
                iniciar_temporizador()
        else:
            print("Error")
        cargar_equipo()
        cargar_equipo2()
        detener_programa()
        
        
        coordenadas = obtener_coordenadas_mouse()
        #print("Coordenadas del mouse:", coordenadas)
        
  
    pygame.quit()
reproducir_sonido_inicio()
juego()
