import os
import pygame


class Equipo:
    def __init__(self, nombre, escudo, portero, jugador, VisLoc=None):
        self.nombre = nombre
        self.escudo = escudo
        self.portero = portero
        self.jugador = jugador
        self.VisLoc = VisLoc


class Jugador:##no use esta, hay una confusion en el Proyecto
    def __init__(self, nombre, funcion, ruta_imagen):
        self.nombre = nombre
        self.funcion = funcion
        self.ruta_imagen = ruta_imagen
    
    
class Artillero(Jugador):
    def __init__(self, nombre, artillero_imagen):
        self.nombre = nombre
        self.artillero_imagen = artillero_imagen
        


class Portero(Jugador):
    def __init__(self, nombre, portero_imagen):
        self.nombre = nombre
        self.portero_imagen = portero_imagen


















        




