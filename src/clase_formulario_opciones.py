from pygame import *
from funciones import *
from configuraciones import *
from clase_boton import *

class Formulario_opciones():
    def __init__(self,pantalla:pygame.Surface,fondo,musica):
        self.pantalla =pantalla
        self.W =pantalla.get_width()
        self.H = pantalla.get_height()
        ##FONDO###
        self.fondo = pygame.image.load(fondo)
        self.background = pygame.transform.scale(self.fondo, (W,H))
        
        self.boton_volver = Boton("formulario_inicio","",[0,400],100,100,"Volver",(0,0,255),True)
        self.boton_musica_on= Boton("musica_on","",[0,500],100,100, "musica_on",(0,0,255),True)
        self.boton_musica_off= Boton("musica_off","",[0,500],100,100, "musica_off",(0,0,255),False)
        self.botones =[self.boton_volver,self.boton_musica_on,self.boton_musica_off]
        self.musica = musica
        
    def dibujar(self):
        
        self.pantalla.blit(self.background, (0, 0))
        #self.text_input_box.draw(self.pantalla)
        for boton in self.botones:
            if boton.es_visible:
                boton.dibujar_boton(self.pantalla)
    def manejar_eventos(self, eventos):
        """Maneja los eventos del formulario

        Args:
            eventos (pygane.event): eventos de pygame

        Returns:
            str: retorna la etiqueta del boton 
        """
        self.dibujar()
        for evento in eventos:
            
            for boton in self.botones:
                if boton.es_presionado(evento):
                    if boton.etiqueta == "formulario_inicio":
                        return boton.etiqueta
                    elif boton.etiqueta == "musica_on":
                        self.mute_music()
                        boton.es_visible = False  
                        for b in self.botones:
                            if b.etiqueta == "musica_off":
                                b.es_visible = True
                                break
                    elif boton.etiqueta == "musica_off":
                        self.unmute_music()                
                        boton.es_visible = False  
                        for b in self.botones:
                            if b.etiqueta == "musica_on":
                                b.es_visible = True
                                break
        return None
    def mute_music(self):
        pygame.mixer.music.set_volume(0)

# Función para desmutear la música (volver a su volumen original)
    def unmute_music(self):
        pygame.mixer.music.set_volume(1)
    
    
        
    
    def update(self, eventos):
        
        self.dibujar()
        nuevo_estado = self.manejar_eventos(eventos)
        return nuevo_estado