import pygame
from pygame.locals import *

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,imagen, pos_x, pos_y,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.imagen= pygame.image.load(imagen)
        self.rect=self.imagen.get_rect()
        self.velocidadDisparo = 10
        self.rect.centerx=pos_x
        self.rect.centery= pos_y
        self.direccion = direccion #es el personaje.que_hace
        
    def eliminar_disparo(self,lista_disparo):
        """Elimina el disparo de la lista de disparos

        Args:
            lista_disparo (list): lista de instancias de la clase disparo
        """
        lista_disparo.remove(self)

        

    def dibujar_rect(self,pantalla,un_jugador):
        """Dibuja el rectangulo

        Args:
            pantalla (.Surface): PANTALLA
            un_jugador (jugador): Instancia dela clase jugador
        """
        for proyectil in un_jugador.listaDisparo:
            pygame.draw.rect(pantalla,"Blue", proyectil.rect,0)
    def blitear_proyectil(self,pantalla):
        """Muestra el proyectil en la pantalla

        Args:
            pantalla (.Surface): Pantalla del juego
        """
        
        pantalla.blit(self.imagen,(self.rect.centerx, self.rect.centery) )
    def definir_trayectoria(self):
        """determina la trayectoria del proyectil segun el atributo .que_hace de la clase jugador
        """
        print(self.direccion)
        if self.direccion == "camina_izquierda" or self.direccion == "salta":
            self.rect.centerx -= self.velocidadDisparo
        else:
            self.rect.centerx += self.velocidadDisparo
    def update(self,pantalla):
        """Actualiza los metodos del proyectil

        Args:
            pantalla (.Surface): Pantalla del juego
        """
        self.definir_trayectoria()
        self.blitear_proyectil(pantalla)
        
    

        
    
   


