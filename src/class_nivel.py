import pygame
import pygame.sprite
from modo import *
from class_enemigo import *
from funciones import *
import sys
from class_item import *

from lib_archivos import *
from funciones import *

class Nivel():
    
    def __init__ (self,imagen_fondo,pantalla,personaje_principal,piso, lista_plataformas,lista_platformas_dos,lista_items,lista_enemigos, lista_vidas,lista_coins,musica):
        pygame.font.init()  
        
        self.sonido_disparo=pygame.mixer.Sound("sonidos/lasershot.mp3")
        self.sonido_coin = pygame.mixer.Sound("sonidos/sonido_moneda.mp3")
        self.sonido_item =pygame.mixer.Sound("sonidos/sonido_item.mp3")
        self.fuente = pygame.font.Font(None, 36)
        self.fondo = imagen_fondo
        self._slave= pantalla
        self.musica =musica
        self.flag_disparo =False
        self.jugador= personaje_principal
        self.plataformas = lista_plataformas
        self.plataformas_dos = lista_platformas_dos
        self.items = lista_items
        self.enemigos = lista_enemigos
        self.vidas = lista_vidas
        self.piso = piso
        self.coins = lista_coins
        
        self.puntaje= 0
        self.tiempo_ultimo_disparo =0 
        self.flag_disparo = False
        self.tiempo_espera = 3000
        self.cantidad_enemigos = len(self.enemigos)
        self.cantidad_enemigos_eliminados = 0
    def reproducir_musica(self):
        reproducir_musica(self.musica)
    def update(self,lista_eventos):
        """Actualiza los elementos del nivel

        Args:
            lista_eventos (list): lista de eventos

        Returns:
            tuple: tupla con el estado del nivel el puntaje y la cantidad de enemigos muertos 
        """
        
        self.blit_pantalla()
        
        self.blit_plataformas()
        self.mostrar_puntaje(PANTALLA,self.puntaje)
        self.mostrar_tiempo(PANTALLA)
        self.obtener_tiempo()
        
        self.jugador.update(self._slave, self.plataformas,self.items, self.enemigos,self.coins)
        self.chequear_vidas()
            
        for proyectil in self.jugador.listaDisparo:
            proyectil.update(PANTALLA)
        self.gestionar_items()
        self.gestionar_enemigos()
       
        self.dibujar_rectangulos()
        self.leer_inputs()
        self.gestionar_coins()
        self.get_modo(lista_eventos)
        if self.jugador.cantidad_vidas == 0:
            return "game_over"
        for item in self.items:
            if item.etiqueta == "puerta_abierta":
                
                
                if self.jugador.lados["right"].colliderect(item.rect):
                    ranking_partida = self.crear_partida_rankings()
                    guardar_json(ranking_partida,"partida")
                    
                    
                    return "victoria"
        
        
    def crear_partida_rankings (self):
        """arma un diccionario con los datos del nivel. Puntaje obtenido, tiempo y cantidad de enemigos eliminados

        Returns:
            _type_: _description_
        """
        lista_rankings= []
        ranking = {}
        
        ranking ["puntaje"] = self.puntaje
        ranking ["tiempo"] = self.obtener_tiempo()
        ranking["cantidad_enemigos"] = self.cantidad_enemigos_eliminados
        lista_rankings.append(ranking)
        return lista_rankings
    
    def get_modo(self,lista_eventos):
        """controla el modo test y el modo desarrollo 

        Args:
            lista_eventos (list): lista de eventos del juego
        """
        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  
                    x, y = pygame.mouse.get_pos()
                    print(f"Posición del mouse - X: {x}, Y: {y}")
    
    def sumar_puntaje(self,puntaje):
        """Suma puntaje

        Args:
            puntaje (puntaje ganado): el puntaje que gano. Por ej si agarra un item va 10
        """
        self.puntaje += puntaje
        
    def obtener_tiempo(self):
        """Obtiene el tiempo actual

        Returns:
            (pygame.time): retorna el tiempo actual de juego en segundos 
        """
        tiempo= pygame.time.get_ticks()
        tiempo_actual = 90 - tiempo //1000
        return tiempo_actual 
    def mostrar_tiempo(self, pantalla):
        """Muestra el tiempo_actual

        Args:
            pantalla (pygame.Surface): objeto surface  que corresponde a la pantalla del juego
        """
        tiempo_actual = self.obtener_tiempo()  
        tiempo_texto = self.fuente.render(f"Tiempo: {tiempo_actual}", True, (255,255,255))
        pantalla.blit(tiempo_texto, (10, 30))
    
        
    def mostrar_puntaje(self, pantalla, puntaje):
        """Muestra el puntaje

        Args:
            pantalla (Pygame.Surface): Pantalla del juego
            puntaje (int): puntaje actual
        """
        
        texto_puntaje = self.fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))  # Blanco

        
        pantalla.blit(texto_puntaje, (10, 10))
    
    def dibujar_rectangulos(self):
        """Dibuja los rectangulos
        """
        if get_modo ():
        #for enemigo in enemigos:
         #   for lado_enemigo in enemigo.lados:
          #      pygame.draw.rect(display, "Orange",enemigo.lados[lado_enemigo],2)        
            for lado in self.piso.lados:
                pygame.draw.rect(self._slave, "Blue", self.piso.lados[lado], 2)
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Orange", self.jugador.lados[lado],2)
            #for rectangulo in rectangulos_plat:
            #    pygame.draw.rect(self._slave,"Blue", rectangulo,2)
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave,"Blue", plataforma.lados[lado],2)
            for proyectil in self.jugador.listaDisparo:
                pygame.draw.rect(self._slave,"Blue", proyectil.rect,2)
            
            for item in self.items:
                if item.es_visible:
                    pygame.draw.rect(self._slave,"Blue",item.rect,2 )
            for enemigo in self.enemigos:
                    pygame.draw.rect(self._slave,"Blue",enemigo.rectangulo,2 )
            for coin in self.coins:
                pygame.draw.rect(self._slave,"Blue",coin.rect,2)
            
            

    def blit_pantalla(self):
        """blitea la pantalla
        """
        self._slave.fill((0, 0, 0))
        self._slave.blit(self.fondo,(0,0))
    def blit_plataformas(self):
        for plataforma in self.plataformas_dos:
            self._slave.blit(plataforma.imagen,(plataforma.posicion_x,plataforma.posicion_y-8))
    
            
            
            
            
    def gestionar_items(self):
        """chequea la colision con el item y determina el comportamiento a partir de su recoleccion
        """
        self.colision_item()
        self.chequear_coleccion_item()
        
    def gestionar_enemigos(self):
        """gestiona el comportamiento de los enemigos:
        si colisionan los rectangulos bottom del jugador con el top del enemigo, elimina al enemigo, lo elimina de la lista. Lo mismo sucede si el rectangulo del disparo choca con su rectangulo
        """
        for enemigo in self.enemigos:    
            if self.cheq_col(self.jugador.lados["bottom"],enemigo.rectangulo):
                
                enemigo.matar_enemigo(self._slave,self.enemigos)
                self.cantidad_enemigos = self.cantidad_enemigos -1
                self.cantidad_enemigos_eliminados += 1
                self.sumar_puntaje(10)
            
            for disparo in self.jugador.listaDisparo:
                if self.cheq_col(disparo.rect,enemigo.rectangulo):
                    enemigo.matar_enemigo(self._slave,self.enemigos)
                    disparo.eliminar_disparo(self.jugador.listaDisparo)
                    self.cantidad_enemigos = self.cantidad_enemigos -1
                    self.sumar_puntaje(10)
                    self.cantidad_enemigos_eliminados +=1
                    
                    
                elif disparo.rect.centerx >= W-100:
                    disparo.eliminar_disparo(self.jugador.listaDisparo)
            enemigo.actualizar(PANTALLA,950,self.plataformas)
        
            if enemigo.esta_muerto: 
                enemigo.matar_enemigo(self._slave,self.enemigos)

    
    def gestionar_coins(self):
        """Gestiona el comportamiento de las monedas del juego
        """
        for coin in self.coins:
            coin.animar_item(PANTALLA)
            if  self.cheq_col(self.jugador.lados["main"],coin.rect):
                
                self.sonido_coin.play()
                self.sumar_puntaje(10)
                coin.eliminar_item(self.coins)
    
            
            
    def cheq_col(self,sujeto,objeto):
        """Chequea la colision entre dos rectangulos

        Args:
            sujeto (rect): el rectangulo de un objeto del juego como el personaje
            objeto (rect): el rectangulo de un objeto del juego como un item

        Returns:
            bool_: retorna True si hay colision
        """
        colision =False
        if sujeto.colliderect(objeto):
            colision = True
            return colision
    def chequear_vidas(self):
        """chequea la cantidad de vidas que tiene el jugador en la partida y segun el numero las muestra en la pantalla
        """
        if self.jugador.cantidad_vidas ==3:
            try:
                self.vidas[0].animar(self._slave)
                self.vidas[1].animar(self._slave)
                self.vidas[2].animar(self._slave)
            except IndexError:
                pass
        elif self.jugador.cantidad_vidas== 2:
            try:
                self.vidas[0].animar(self._slave)
                self.vidas[1].animar(self._slave)
            except IndexError:
                pass
        elif self.jugador.cantidad_vidas ==1:
            try:
                self.vidas[0].animar(self._slave)  
            except IndexError:
                pass

        
        
    def colision_item(self):
        """chequea la colision entre el jugador y el item
        """
        for item in self.items:

            item.animar_item(PANTALLA)
            if self.cheq_col(self.jugador.lados["main"],item.rect) and item.otorga_puntaje :
                self.sonido_item.play()
                self.puntaje += 20
                
                item.quitar_puntaje()
                item.invisibilizar(self.items)
                item.coleccionar_item()
    
    def chequear_coleccion_item(self):
        """determina el comportamiento de recoleccion para cada item
        """
        for item in self.items:
            if item.coleccionado:
                if item.etiqueta =="vida" and self.jugador.cantidad_vidas <3:
                    self.jugador.cantidad_vidas +=1
                    item.coleccionado = False
                elif item.etiqueta == "arma":
                    item.es_visible =False
                    self.jugador.puede_disparar =True
                elif item.etiqueta =="combustible":
                    self.jugador.gravedad = 1.5
                    item.coleccionado =False
                elif item.etiqueta =="switch_apagado":
                    
                    item.es_visible =False
                    for item in self.items:
                        if item.etiqueta =="puerta_abierta":
                            
                            item.es_visible =True
                        elif item.etiqueta =="switch_prendido":
                            item.es_visible=True
                            
                        elif item.etiqueta =="puerta_cerrada":
                            item.es_visible =False
    def leer_inputs(self):
        """Lee los inputs del juego
        """
        keys = pygame.key.get_pressed()
        movimiento = False
        disparo = False
        
        if keys[pygame.K_RIGHT] and (self.jugador.lados["main"].right < (1000 - 10)):   
            self.jugador.que_hace = "camina_derecha"
            self.flag_disparo = True
            movimiento = True
        elif keys[pygame.K_LEFT] and (self.jugador.lados["main"].left > 10):
            self.jugador.que_hace = "camina_izquierda"
            self.flag_disparo = True
            movimiento = True
            if self.jugador.esta_saltando:
                self.jugador.esta_saltando_izquierda = True
        elif keys[pygame.K_DOWN]:
            self.jugador.que_hace = "agachado"
            movimiento = True
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
            movimiento = True

        if self.jugador.puede_disparar and keys[pygame.K_SPACE]:
            disparo = True
            
            
            self.flag_disparo=True
            self.jugador.disparar()
            self.sonido_disparo.play()
            if self.jugador.que_hace in ["quieto", "camina_derecha", "salta"]:
                self.jugador.que_hace = "atacando_derecha"
            else:
                self.jugador.que_hace = "atacando_izquierda"

        if not movimiento and not disparo:
            self.jugador.que_hace = "quieto"
            
   
        
        
        
        
        