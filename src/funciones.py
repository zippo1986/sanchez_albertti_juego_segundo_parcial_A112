from class_nivel import *
from class_enemigo import *

from class_personaje import*
from class_vida import *
from pygame.locals import *
from modo import *
from class_plataforma import *
from class_plataformas_grandes import *
from class_item import *
import pygame


def draw_text(surface, text, font, color, x, y):
    """Escribe texto 

    Args:
        surface (.Surface): Pantalla del juego
        texto (_type_): texto a escribir
        font (.font): fuente de texto
        color (tuple): tupla de rgb
        x (int): posicion en x
        y (int): posicion en y
    """
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
import pygame

def reproducir_musica(archivo_musica, volumen=0.5, bucle=-1):
    """Reproduce música en Pygame.

    Args:
        archivo_musica (str): Ruta al archivo de música.
        volumen (float): Volumen de la música (0.0 a 1.0). Por defecto es 0.5.
        bucle (int): Número de veces que la música se repetirá. -1 para repetición infinita. Por defecto es -1.
    """
    # Inicializar el mezclador de sonido de Pygame
    pygame.mixer.init()
    
    # Cargar el archivo de música
    pygame.mixer.music.load(archivo_musica)
    
    # Establecer el volumen de la música
    pygame.mixer.music.set_volume(volumen)
    
    # Reproducir la música
    pygame.mixer.music.play()