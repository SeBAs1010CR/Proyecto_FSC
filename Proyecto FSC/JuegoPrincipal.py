import random
import pygame
import os
from Clases.Instancias import *


###########Globales
Numerodetirolocal = 0
Numerodetiro = 0
goles_equipo1 = 0
goles_equipo2 = 0
local = True



def reproducir_sonido_silbato_inicial():###########esto tengo que ver como hago para que suene el silbataso luego de 5s

    #if silbataso == False:
        silbato_sound = pygame.mixer.Sound("Sonidos/silbato.wav")  
        
    
        silbato_sound.play()

pygame.init()

# Dimensiones de la ventana
ANCHO = 1500
ALTO = 800


ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

ruta_imagen_fondo = os.path.join("Imagenes", "cancha.png")  
imagen_fondo = pygame.image.load(ruta_imagen_fondo).convert()  


def reproducir_sonido_inicio():
    
    silbato_sound = pygame.mixer.Sound("Sonidos/inicio.wav") 
    silbato_sound.play()

reproducir_sonido_inicio()
###################################################SONIDOS################################

def reproducir_sonido_silbato():
    silbato_sound = pygame.mixer.Sound("Sonidos/silbato.wav")  
    silbato_sound.play()


def reproducir_sonido_abucheo():
    silbato_sound = pygame.mixer.Sound("Sonidos/abucheo.wav")  
    silbato_sound.play()

def reproducir_sonido_gol():
    silbato_sound = pygame.mixer.Sound("Sonidos/gol.wav") 
    silbato_sound.play()





Escudo_MIL = os.path.join(os.path.dirname(__file__),'Imagenes', 'emil.png')
Escudo_JUV = os.path.join(os.path.dirname(__file__), 'Imagenes', 'ejuv.png')
Escudo_RIV = os.path.join(os.path.dirname(__file__), 'Imagenes', 'erp.png')

def dibujar_escudos(ventana, equipo, x, y): 
        escudo_img = pygame.image.load(equipo)
        escudo_img = pygame.transform.scale(escudo_img, (1300, 650))
        ventana.blit(escudo_img, (x, y))
        

def logo(nombre_equipo, local_o_visitante):
    if nombre_equipo == 'Juventus'and local_o_visitante == 'Local':
        return dibujar_escudos(ventana, Escudo_MIL, -540, -160)
    elif nombre_equipo == 'Juventus'and local_o_visitante == 'Visitante':
        return dibujar_escudos(ventana, Escudo_MIL, 750, -160)
###------------------------------------------archivos--------------------------------------------------------------------------------------------###
def cargar_equipo():
    nombre_equipo = ''
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
    return logo(nombre_equipo, local_o_visitante) 
    

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
            x = 1400
            y = 500
        if NUMERO_DE_TIRO == 1:
            x = 1400
            y = 550
        if NUMERO_DE_TIRO == 2:
            x = 1400
            y = 600
        if NUMERO_DE_TIRO == 3:
            x = 1400
            y = 650
        if NUMERO_DE_TIRO == 4:
            x = 1400
            y = 700
        
    else:
        color = (255, 0, 0)  # Rojo si no es gol
        if NUMERO_DE_TIRO == 0:
            x = 1400
            y = 500
        if NUMERO_DE_TIRO == 1:
            x = 1400
            y = 550
        if NUMERO_DE_TIRO == 2:
            x = 1400
            y = 600
        if NUMERO_DE_TIRO == 3:
            x = 1400
            y = 650
        if NUMERO_DE_TIRO == 4:
            x = 1400
            y = 700
    pygame.draw.circle(ventana, color, (x, y), 20)

def dibujar_tiro_local(x, y, es_gol, NUMERO_DE_TIRO):
    global goles_equipo2
    if es_gol:
        goles_equipo2 += 1
        color = (0, 255, 0)  # Verde si es gol
        if NUMERO_DE_TIRO == 0:
            x = 100
            y = 500
        if NUMERO_DE_TIRO == 1:
            x = 100
            y = 550
        if NUMERO_DE_TIRO == 2:
            x = 100
            y = 600
        if NUMERO_DE_TIRO == 3:
            x = 100
            y = 650
        if NUMERO_DE_TIRO == 4:
            x = 100
            y = 700
        
    else:
        color = (255, 0, 0)  # Rojo si no es gol
        if NUMERO_DE_TIRO == 0:
            x = 100
            y = 500
        if NUMERO_DE_TIRO == 1:
            x = 100
            y = 550
        if NUMERO_DE_TIRO == 2:
            x = 100
            y = 600
        if NUMERO_DE_TIRO == 3:
            x = 100
            y = 650
        if NUMERO_DE_TIRO == 4:
            x = 100
            y = 700
    pygame.draw.circle(ventana, color, (x, y), 20)



def verificar_tecla_presionada():
    global Numerodetiro
    global local
    local = True
    tecla_presionada = pygame.key.get_pressed()
    if tecla_presionada[pygame.K_x]:
        indice_seleccionado, teclas_seleccionadas = seleccionar_indice_portero(Paletas)
        if "x" not in teclas_seleccionadas:
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
        
        ventana.blit(imagen_fondo, (200, 50))

#################################################Informaci'on en pantalla#########################
        pygame.draw.rect(ventana, (0, 0, 0), (1350, 420, 200, 40))
        fuentetiro = pygame.font.SysFont(None, 36)  
        textotiro = fuentetiro.render(f"Tiro: {Numerodetiro}", True, (255, 255, 255))
        ventana.blit(textotiro, (1350, 420))

        pygame.draw.rect(ventana, (0, 0, 0), (767, 10, 200, 40))
        fuentegol = pygame.font.SysFont(None, 36)  
        textogol = fuentegol.render(f"Goles: {goles_equipo1}", True, (255, 255, 255))
        ventana.blit(textogol, (767, 14))

        pygame.draw.rect(ventana, (0, 0, 0), (50, 420, 100, 40))
        fuentetiro2 = pygame.font.SysFont(None, 36)  
        textotiro2 = fuentetiro2.render(f"Tiro: {Numerodetirolocal}", True, (255, 255, 255))
        ventana.blit(textotiro2, (50, 420))

        pygame.draw.rect(ventana, (0, 0, 0), (527, 10, 200, 40))
        fuentegol2 = pygame.font.SysFont(None, 36)  
        textogol2 = fuentegol2.render(f"Goles: {goles_equipo2}", True, (255, 255, 255))
        ventana.blit(textogol2, (627, 14))
#################################################Informaci'on en pantalla#########################


        pygame.draw.line(ventana, (255, 255, 255), (750, 2), (750, min(50, ALTO - 10)), 3)










        pygame.display.flip()
        cargar_equipo()
        
        coordenadas = obtener_coordenadas_mouse()
        print("Coordenadas del mouse:", coordenadas)
        
  
    pygame.quit()

juego()