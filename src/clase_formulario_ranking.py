import pygame
from funciones import *
from clase_boton import *
from caja_ingreso import *
from lib_archivos import *
from lib_archivos import *
from lib_ordenamiento import *

class FormularioRanking:
    
    def __init__(self, pantalla: pygame.Surface, fondo, musica):
        self.pantalla = pantalla
        self.W = pantalla.get_width()
        self.H = pantalla.get_height()
        ## FONDO ###
        self.fondo = pygame.image.load(fondo)
        self.background = pygame.transform.scale(self.fondo, (self.W, self.H))
        self.recuadro_rankings = pygame.image.load("tabla_rankings.png")
        self.tabla_rankings = pygame.transform.scale(self.recuadro_rankings, (400, 600))
        self.rect_ancho =200
        self.rect_alto = 50 
        self.posiciones = [
    (419, 266),
    (419, 344),
    (519, 398),
    (419, 466),
    (419, 521)
]
        self.rect1 = pygame.Rect(419, self.posiciones[0][1], self.rect_ancho, self.rect_alto)
        self.rect2 = pygame.Rect(self.posiciones[1][0], self.posiciones[1][1], self.rect_ancho, self.rect_alto)
        self.rect3 = pygame.Rect(self.posiciones[2][0], self.posiciones[2][1], self.rect_ancho, self.rect_alto)
        self.rect4 = pygame.Rect(self.posiciones[3][0], self.posiciones[3][1], self.rect_ancho, self.rect_alto)
        self.rect5 = pygame.Rect(self.posiciones[4][0], self.posiciones[4][1], self.rect_ancho, self.rect_alto)
        self.lista_rects = [self.rect1,self.rect2,self.rect3,self.rect4,self.rect5]
        self.fuente = pygame.font.Font(None, 36)
        self.color_texto = pygame.Color('white')
        self.puntajes = json_a_lista("partida")  
        self.boton_volver = Boton("formulario_inicio", "", [self.W // 2, 500], 200, 100, "Volver al menú principal", (0, 0, 255), True)
        self.boton_salir = Boton("salir", "", [self.W // 2, 650], 200, 100, "Salir", (255, 0, 0), True)
        
        
    def dibujar(self):
        self.pantalla.blit(self.background, (0, 0))
        self.pantalla.blit(self.tabla_rankings, (360,-40))
        
    def obtener_lista_rankings(self):
        lista_puntajes = archivo_a_lista("puntajes.csv")  
        
        return lista_puntajes      
    def ordenar_ranking (self):
        lista_rankings =  self.obtener_lista_rankings()
        if len(lista_rankings) > 1:
            ordenar_un_criterio(lista_rankings,"puntaje")
            
        return lista_rankings    
            
    def renderizar_texto_ranking(self):
        lista_rankings = self.ordenar_ranking()
        
        lista_diccionario_pos =[]
        for posicion in lista_rankings:
            diccionario_posicion = {}
            
            diccionario_posicion["nombre"] = self.fuente.render(f"{posicion["nombre"]}", True, self.color_texto)
            diccionario_posicion["puntaje"] = self.fuente.render(f"{posicion["puntaje"]}",True,self.color_texto)
            lista_diccionario_pos.append(diccionario_posicion)
        
        return lista_diccionario_pos
    
    def blitear_posiciones_ranking(self):
        lista_posiciones = self.renderizar_texto_ranking()
        
        for i, posicion in enumerate(lista_posiciones):
            if i < len(self.lista_rects):
                rect = self.lista_rects[i]
                self.pantalla.blit(posicion["nombre"], (rect.x, rect.y -20))
                self.pantalla.blit(posicion["puntaje"], (rect.x + 100, rect.y -20)) 
                
    def update (self,eventos):
        self.dibujar()
        
        self.blitear_posiciones_ranking()
    
        

            
            
            
            
        
    
        
    