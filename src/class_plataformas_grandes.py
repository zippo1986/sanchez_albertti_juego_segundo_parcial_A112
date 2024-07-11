from configuraciones import *
import pygame
class PlataformaDos(pygame.sprite.Sprite):
    def __init__(self, gravedad, posicion_inicial:tuple, ancho,alto):
        
        self.ancho= ancho
        self.alto=90  
        self.posicion_x = posicion_inicial[0]
        self.posicion_y = posicion_inicial[1]
        self.rectangulo= pygame.Rect(self.posicion_x,self.posicion_y,ancho,alto)
        rectangulo = pygame.Rect(self.posicion_x,self.posicion_y,ancho,alto)
        rectangulo.x =posicion_inicial[0] 
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)