import pygame
import json
from lib_archivos import *
from funciones import *
from clase_boton import Boton

class FormPuntaje:
    def __init__(self, pantalla: pygame.Surface, fondo, musica):
        self.pantalla = pantalla
        self.W = pantalla.get_width()
        self.H = pantalla.get_height()
        ## FONDO ###
        self.fondo = pygame.image.load(fondo)
        self.background = pygame.transform.scale(self.fondo, (self.W, self.H))
        self.recuadro_imagen = pygame.image.load("Tabla_puntaje.png")
        self.tabla_puntaje = pygame.transform.scale(self.recuadro_imagen, (400, 600))
        
        self.fuente = pygame.font.Font(None, 36)
        self.puntajes = json_a_lista("partida")  
        self.boton_volver = Boton("formulario_inicio", "", [self.W // 2, 500], 200, 100, "menú principal", (0, 0, 255), True)
        self.boton_salir = Boton("salir", "", [self.W // 2, 650], 200, 100, "Salir", (255, 0, 0), True)
        self.boton_submit = Boton("submit", "submit.png", [0 , 0], 200, 100, "", (0, 0, 255), True)
        self.musica= musica
        self.nombre = ""
        self.caja_texto = pygame.Rect(450, 391, 200, 50)
        self.color_caja = pygame.Color('lightskyblue3')
        self.color_texto = pygame.Color('black')
        
        self.botones = [self.boton_volver, self.boton_salir, self.boton_submit]
        self.musica = musica
    def reproducir_musica(self):
        reproducir_musica()
        
    def update(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    self.guardar_puntaje()
                elif evento.key == pygame.K_BACKSPACE:
                    self.nombre = self.nombre[:-1]
                else:
                    self.nombre += evento.unicode
            for boton in self.botones:
                if boton.es_presionado(evento):
                    if boton.etiqueta == "submit":
                          
                        if self.nombre:
                            self.guardar_puntaje()
                            boton.etiqueta= "formulario_rankings"
                            
                            
                        else:
                            break
                        

                    return boton.etiqueta
        self.dibujar()
        
    def dibujar(self):
        self.pantalla.blit(self.background, (0, 0))
        self.pantalla.blit(self.tabla_puntaje, (360,-40))
        
        
        for puntaje in self.puntajes:
            
            texto_puntaje = self.fuente.render(f"puntaje: {puntaje["puntaje"]}\n", True, self.color_texto)
            texto_tiempo = self.fuente.render(f"tiempo: {puntaje["tiempo"]}\n", True, self.color_texto)
            texto_cantidad_enemigos_eliminados = self.fuente.render(f"puntaje: {puntaje["cantidad_enemigos"]}\n", True, self.color_texto)
            self.pantalla.blit(texto_puntaje, (460, 166))
            self.pantalla.blit(texto_tiempo, (460, 244))
            self.pantalla.blit(texto_cantidad_enemigos_eliminados, (460, 319))
            
            
        
        for boton in self.botones:
            boton.dibujar_boton(self.pantalla)
        
        pygame.draw.rect(self.pantalla, self.color_caja, self.caja_texto, 2)
        texto_nombre = self.fuente.render(self.nombre, True, self.color_texto)
        self.pantalla.blit(texto_nombre, (self.caja_texto.x + 5, self.caja_texto.y + 5))
        pygame.display.flip()
    
    def guardar_puntaje(self):
        nuevo_puntaje = {"nombre": self.nombre}
        
        for puntaje in self.puntajes:
            nuevo_puntaje.update(puntaje)
        with open("puntajes.csv", "a") as archivo:
            
            archivo.write(",".join([str(value) for value in nuevo_puntaje.values()]) + "\n")
            
    
    def guardar_csv(lista: list, nombre_archivo: str):
        pass
        """
    Guarda los elementos de la lista en un archivo .csv.

    Args:
        lista (list): Lista de diccionarios.
        nombre_archivo (str): Nombre del archivo.
    
    if not lista:
        return  
    
    # Obtener las claves del primer diccionario para el encabezado
    encabezado = list(lista[0].keys())
    
    # Abrir el archivo en modo de escritura
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # Escribir el encabezado
        archivo.write(",".join(encabezado) + "\n")
        
        # Escribir las filas
        for elemento in lista:
            linea = ",".join(str(elemento[key]) for key in encabezado)
            archivo.write(linea + "\n")"""