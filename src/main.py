import pygame
import random
from clase_boton import *
from configuraciones import *

from class_personaje import *  
from class_enemigo import *
from class_plataforma import *
from class_plataformas_grandes import *
from class_item import *
from pygame.locals import *
from modo import *
from class_nivel import Nivel

from class_nivel_dos import *
from class_proyectil import *
 

from lib_forms import *
import sys


pygame.init()


# Configuración de formularios


nivel_unol = nivel_dos_(PANTALLA)
puntaje =None
estado_actual = "formulario_inicio"
ejecutando = True

while ejecutando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            ejecutando = False

    if estado_actual == "formulario_inicio":
        formulario_inicio.reproducir_musica()
        nuevo_estado = formulario_inicio.update(eventos)
        if nuevo_estado:
            estado_actual = nuevo_estado
    elif estado_actual == "nivel_uno":
        nuevo_estado = nivel_unol.update(eventos)
        if nuevo_estado:
            estado_actual = nuevo_estado
    elif estado_actual == "formulario_opciones":
        nuevo_estado = formulario_opciones.update(eventos)
        if nuevo_estado:
            estado_actual = nuevo_estado
    elif estado_actual == "victoria":
        
        nuevo_estado = formulario_puntaje.update(eventos)
        
        if nuevo_estado:
            estado_actual = nuevo_estado
    elif estado_actual == "formulario_rankings":
        formulario_ranking.update(eventos)
    
    elif estado_actual == "game_over":
        
        nuevo_estado = formulario_puntaje.update(eventos)
        if nuevo_estado:
            estado_actual = nuevo_estado
    """    
        if nuevo_estado:
            estado_actual = nuevo_estado
    elif estado_actual == "salir":
        ejecutando = False"""

    pygame.display.flip()
    
pygame.quit()