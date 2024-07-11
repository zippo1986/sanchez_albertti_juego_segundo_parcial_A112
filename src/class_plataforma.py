from configuraciones import *
import pygame
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,imagen, gravedad, posicion_inicial:tuple, ancho):
        self.ancho= ancho
        self.alto=90  
        self.imagen= pygame.transform.scale(pygame.image.load(imagen), (ancho,30))
        self.posicion_x = posicion_inicial[0]
        self.posicion_y = posicion_inicial[1]
        self.rectangulo = self.imagen.get_rect() 
        rectangulo = self.imagen.get_rect()
        rectangulo.x =posicion_inicial[0] 
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
        #self.desplazamiento_x = velocidad
        #self.desplazamiento_y = velocidad
        #self.transparencia = transparencia

    
   
    
    
        


            