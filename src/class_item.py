import pygame

from modo import *
class Item(pygame.sprite.Sprite):
    def __init__(self,etiqueta,imagen,pos_x,pos_y,es_visible,esta_coleccionado,tamanio:tuple):
        super().__init__()
        self.etiqueta=etiqueta
        self.imagen= pygame.image.load(imagen)
        self.tamanio = tamanio
        self.imagen = pygame.transform.scale(self.imagen, self.tamanio)
        self.rect = self.imagen.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.es_visible = es_visible
        self.coleccionado= esta_coleccionado
        self.otorga_puntaje = True
        
    
    def animar_item (self,pantalla):
        """Muestra el item

        Args:
            pantalla (.Surface): La pantalla del juego
        """
        
        if self.es_visible:
            pantalla.blit(self.imagen, self.rect)
    
    

    def eliminar_item(self,lista_item):
        """elimina item de la lista

        Args:
            lista_item (list): lista de items
        """
        lista_item.remove(self)
    def invisibilizar(self,lista_):
        """invisibilza el item

        Args:
            lista_ (list): lista de items
        """
        self.es_visible =False
    def quitar_puntaje(self):
        
        self.otorga_puntaje = False
     

    def coleccionar_item(self):
        self.coleccionado =True 
                    
    
    def dibujar_rect(self,pantalla):
        for item in self.lista_items:
            pygame.draw.rect(pantalla,"Blue", item.rect,2)
    
    
                
    
                

    



        
                
                
