import pygame

from modo import *
class Vida(pygame.sprite.Sprite):
    def __init__(self,imagen,pos_x,pos_y,es_visible):
        super().__init__()
        self.imagen= pygame.image.load(imagen)
        self.tamanio = (50,50)
        self.imagen = pygame.transform.scale(self.imagen, self.tamanio)
        self.rect = self.imagen.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.es_visible = es_visible
    
        
    
    def animar (self,pantalla):
        """blitea las imagenes de las vidas en la pantalla

        Args:
            pantalla (.Surface): pantalla del juego
        """
        if self.es_visible:
            pantalla.blit(self.imagen, self.rect)
    
    
    
    
    def eliminar_item(self,lista_item):
        """Elimina el item de la pantalla

        Args:
            lista_item (list): Lista de items
        """
        lista_item.remove(self)
    def invisibilizar(self,):
        self.es_visible =False
    
     
    def update_vidas(self,pantalla):
        """se encarga de actualizar llos objetos de la clase vida

        Args:
            pantalla (.Surface): Pantalla del juego
        """
        self.animar_item(pantalla)
    
    