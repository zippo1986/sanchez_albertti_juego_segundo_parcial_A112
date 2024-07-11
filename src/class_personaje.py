import pygame
import sys
import pygame.sprite
from class_proyectil import Proyectil
from configuraciones import *
"""#atributos
    imagen
    rectangulo
    velocidad
    que_hace
    contador_pasos

    metodos:
    caminar
    saltar
"""
class Personaje(pygame.sprite.Sprite):
    def __init__(self,gravedad,tamanio:tuple,animaciones, posicion_inicial:tuple,velocidad,lista_vidas):
        super().__init__()
        #self.superficie = pygame.Surface(tamanio)
        self.ancho = tamanio[0]
        self.alto = tamanio [1]
        #GRAVEDAD
        self.gravedad = gravedad
        #Mientraas mas grande mas fuerte cae
        self.potencia_salto = -20
        self.limite_velocidad_caida=10
        self.esta_saltando = False
        #Animaciones+
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        #self.rect.center = center
        self.reescalar_animaciones()
        self.posicion_inicial = posicion_inicial
        self.velocidad = velocidad
        
        self.listaDisparo = []
        
        #RECTANGULO
        rectangulo =self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        self.bandera_pierde =False
        self.saltos= 2
        
        #MOvimiento
        self.velocidad = velocidad
        self.desplazamiento_y= 10
        
        self.cantidad_vidas = 3
        self.lista_vidas = lista_vidas
        self.es_invulnerable = False

        self.invulnerabilidad_duracion =60
        self.invulnerabilidad_timer = 0
        self.puntaje = 0
        self.moviendose_izquierda = False
        self.intervalo_disparo = 500
        self.ultimo_disparo = 0
        self.flag_disparo = True
        self.puede_disparar = False
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_espera = 1000
        
        self.esta_saltando_izquierda= False
    def mover(self, velocidad):
        """Mueve los rectangulos segun la velocidad

        Args:
            velocidad (int): 
        """
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def chequear_colision_piso(self):
        """chequea la colision con el piiso
        """
        
        if self.lados["bottom"].y >= 600 :
            self.respawn((100,500))
            self.cantidad_vidas -=1
    def aplicar_gravedad(self, pantalla, piso:list):
        """Deetermina el comportamiento ante la aplicacion de gravedad. 
        anima al jugador y aplica gravedad cuando está saltando
        Args:
            pantalla (.Surface): PAntalla
            piso (plataforma): piso del juego

        Returns:
            _type_: _description_
        """
        if self.esta_saltando:
            if self.esta_saltando_izquierda:
                self.animar(pantalla, "salta_izquierda")
            
            else:
            
                self.animar(pantalla, "salta")
        
        
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            
                self.desplazamiento_y += self.gravedad
            
    
        
        tocando_suelo = False
        for plataforma in piso:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.lados["main"].top
                tocando_suelo = True
                break

        if tocando_suelo:
            self.saltos = 2  # Restablecer el contador de saltos al tocar el suelo
        else:
            self.esta_saltando = True
    
    

    def update(self,pantalla, piso,items,enemigos,lista_coins):
        """Args:
            pantalla (.Surface): surface
            piso (plataforma): piso 
            items (list)): item
            enemigos (list): _description_
            lista_coins (list): lista de coins
        """
        self.chequear_colision_piso()
        self.manejo_acciones(pantalla)
        self.detectar_danio(enemigos)
        self.aplicar_gravedad(pantalla, piso)
        
    def cheq_col(self,sujeto,objeto):
        """chequear colision

        Args:
            sujeto (personaje): personaje del juego
            objeto (objeto del juego): objeto del juego

        Returns:
            _type_: _description_
        """
        colision =False
        if sujeto.colliderect(objeto):
            colision = True
            return colision    
    def detectar_danio(self,lista_enemigos):
        """Detecta el daño y si se detecta le resta vida y respawnea al jugador

        Args:
            lista_enemigos (list): lista de enmeigos
        """
        i =0
        for enemigo in lista_enemigos:
            if self.cheq_col(self.lados["main"],enemigo.rectangulo):
                print (self.cantidad_vidas)
                self.respawn((100,550))
                self.morir()
                i +=1
    #def disparar(self,x,y):
     #   miProyectil = Proyectil(x,y)
      #  self.listaDisparo.append(miProyectil)
    def reescalar_animaciones (self):
        """Reescala las animaciones
        """
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], self.ancho,self.alto)
    
    def manejo_acciones(self,pantalla):
        """Manejo de las acciones de la clase

        Args:
            pantalla (.Surface): Pantalla de juego
        """
        match self.que_hace:
            case "camina_derecha":
                self.direccion_proyectil = -1
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad)
            case "camina_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_izquierda")
                self.mover(self.velocidad * - 1)
                
                
            case "ataca_derecha":
                print ("Esta atacandoo")
            case"ataca_izquierda":
                print("ataca:izquierda")
            
            
            case "salta":
                if not self.esta_saltando :
                    #self.animar(pantalla,"salta")
                    self.esta_saltando_izquierda= False
                    self.esta_saltando =True
                    self.desplazamiento_y = self.potencia_salto
            case "salta_izquierda": 
                if not self.esta_saltando:
                    self.esta_saltando = False
                    self.desplazamiento_y = self.potencia_salto
                self.mover(self.velocidad * -1)
                
            case "quieto":
                
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")
            case "atacando":
                if not self.esta_saltando:
                    self.animar(pantalla,"atacando")
            case "agachado":
                if not self.esta_saltando:
                    self.animar(pantalla,"agachado")
            case "muere":
                if not self.esta_saltando:
                    self.animar(pantalla, "muere")
    def animar(self, pantalla, que_animacion):
        """Anima al personaje a partir del atributo que_hace

        Args:
            pantalla (.Surface): Pantalladel juego
            que_animacion (diccionario): diccionario de animaciones
        """
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    def sumar_puntaje(self,puntaje):
        self.puntaje += puntaje
    def respawn(self,posicion_inicial):
        
        """_summary_ 
        Respawnea al jugador
        args:
        Pos inicial (tuple): tupla de posicion inicial
        """   
        

        
        self.rectangulo.x= posicion_inicial[0] 
        self.rectangulo.y = posicion_inicial[1] -100

        
        self.lados = obtener_rectangulo(self.rectangulo)
        
    
    def morir(self):
        """REsta una vida a la cantidad de vidas del jugador
        """
        self.que_hace= "muere"
        self.cantidad_vidas -=1

    def reescalar_animaciones (self):
        """reescala animaciones
        """
        
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], self.ancho,self.alto)
    
    def disparar(self):
        """crea una instancia de la clase proyectil y la agrega a la lista de disparos
        """
        

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.intervalo_disparo:
           
            

            
            x = self.lados["right"].centerx  
            y = self.lados["right"].centery   
            
            miProyectil = Proyectil("imagenes/poder_uno.png",x, y,self.que_hace)


                
            self.listaDisparo.append(miProyectil)
            self.ultimo_disparo = tiempo_actual
