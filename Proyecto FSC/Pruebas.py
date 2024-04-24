import pygame
import random
import os
import time

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
ANCHO = 800
ALTO = 600
BAJO = 0
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Lanzamiento de Moneda")

# Definir colores
NEGRO = (0, 0, 0)

# Cargar imágenes de la moneda, el escudo y la corona
ruta_dan = os.path.join("Imagenes", "dan.png")
ruta_leo = os.path.join("Imagenes", "leo.png")
ruta_sam = os.path.join("Imagenes", "sam.png")
dan_img = pygame.image.load(ruta_dan)
leo_img = pygame.image.load(ruta_leo)
sam_img = pygame.image.load(ruta_sam)
contador = 0
juegoplay = False
bandera = False

x_moneda = ANCHO // 2 - dan_img.get_width() // 2
y_moneda = 500  
velocidad_y = 3000  

# Bucle principal
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False





















    # Calcular el tiempo transcurrido desde el último fotograma en segundos
    dt = pygame.time.Clock().tick(60) / 1000.0

    # Actualizar posición de la moneda
    if contador < 100 and bandera == False:
        y_moneda -= velocidad_y * dt
        contador += 1
        print(contador)
        print(y_moneda)

    elif bandera == False:
        y_moneda += velocidad_y * dt
        contador +=1
        print(contador)
        print(y_moneda)
    # Si la moneda llega al borde inferior de la ventana, reiniciar la posición
    if contador >= 100:
        if y_moneda >= ALTO:
            y_moneda = -4000
            

    # Dibujar la moneda
    ventana.fill(NEGRO)
    if contador <= 200:
        ventana.blit(dan_img, (x_moneda, int(y_moneda)))  # Convertir la posición a entero para evitar bordes borrosos
    resul = random.choice([leo_img, sam_img])
    if contador == 193 and y_moneda == 107 and juegoplay == False:
        bandera = True
        print("si")
        ventana.blit(resul, (ANCHO // 2 - resul.get_width() // 2, ALTO // 2 - resul.get_height() // 2))
    if contador >= 400:
        juegoplay = True








































    pygame.display.flip()

# Salir de Pygame
pygame.quit()
