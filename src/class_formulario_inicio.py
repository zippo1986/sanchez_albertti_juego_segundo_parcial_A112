from pygame import *
from funciones import *
from configuraciones import *
from clase_boton import *

class Formulario_inicio():
    def __init__(self,pantalla:pygame.Surface,fondo,musica):
        self.pantalla =pantalla
        self.W =pantalla.get_width()
        self.H = pantalla.get_height()
        ##FONDO###
        self.fondo = pygame.image.load(fondo)
        self.background = pygame.transform.scale(self.fondo, (W,H))
        
        self.boton_start = Boton("nivel_uno","Recursos/play_game.png",[0,400],200,50,"",(0,0,255),True)
        self.boton_opciones= Boton("formulario_opciones","",[0,500],200,50, "opciones",(0,0,255),True)
        self.botones =[self.boton_start,self.boton_opciones]
        self.musica = musica
    def reproducir_musica(self):
        reproducir_musica(self.musica)
            
    def dibujar(self):
        self.pantalla.blit(self.background, (0, 0))
        #self.text_input_box.draw(self.pantalla)
        for boton in self.botones:
            boton.dibujar_boton(self.pantalla)
    def manejar_eventos(self, eventos):
        """maneja los eventos del formulario

        Args:
            eventos (pygabme.event): eventos de pygame
            musica (str): str

        Returns:
            str: retorna la etiqueta del boton 
        """
        self.dibujar()
        for evento in eventos:
            
            for boton in self.botones:
                if boton.es_presionado(evento):
                    return boton.etiqueta
        return None
    
    def update(self, eventos):
        
        self.dibujar()
        nuevo_estado = self.manejar_eventos(eventos)
        return nuevo_estado
        
    
        