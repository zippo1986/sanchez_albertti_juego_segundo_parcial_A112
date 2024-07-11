
import pygame
import random
from configuraciones import *
from class_proyectil import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, animaciones, posicion_inicial:tuple, posicion_final:tuple, velocidad):
        self.animaciones = animaciones
        #self.reescalar_imagen()
        rectangulo = self.animaciones["enemigo_izq"][0].get_rect()
        self.rectangulo = self.animaciones["enemigo_izq"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.posicion_inicial_x  = posicion_inicial[0]
        self.posicion_inicial_y = posicion_inicial[1]
        self.posicion_final_x = posicion_final[0]
        self.posicion_final_y = posicion_final[1]
        self.velocidad = velocidad
        self.direccion = 1  # 1 para derecha, -1 para izquierda
        self.gravedad = 5
        self.contador_pasos = 0
        self.que_hace = "enemigo_izq"
        self.esta_muerto = False
        self.esta_muriendo = False
        self.ultimo_cambio = pygame.time.get_ticks()
        self.lados = obtener_rectangulo(rectangulo)
        self.on_ground = False
        
        

    def movimiento_lateral(self):
        """determina el movimiento de los enemigos de forma lateral
        """
        self.rectangulo.x += self.velocidad * self.direccion
        if self.rectangulo.x < self.posicion_final_x:  
            self.direccion *= -1  # Cambia la dirección
            self.que_hace= "enemigo_der"
        elif self.rectangulo.x > self.posicion_inicial_x:
            self.que_hace = "enemigo_izq"
            self.direccion *= -1
    
         
    
    def actualizar_movimiento(self, limite_izquierdo, limite_derecho):
        tiempo_actual = pygame.time.get_ticks()

        # Verificar si han pasado 5 segundos (5000 milisegundos)
        if tiempo_actual - self.ultimo_cambio > 5000:
            self.cambiar_direccion()
            
            self.ultimo_cambio = tiempo_actual  # Actualizar el momento del último cambio

        self.rectangulo.x += self.velocidad * self.direccion

        # Cambiar de dirección si alcanza los límites horizontales
        if self.rectangulo.left <= limite_izquierdo or self.rectangulo.right >= limite_derecho:
            self.cambiar_direccion()

    def matar_enemigo(self,pantalla,lista_enemigos):
        tiempo_actual=pygame.time.get_ticks()
        tiempo_espera = 300
        self.animar(pantalla,"enemigo_muere")
        if tiempo_actual > tiempo_espera:
            lista_enemigos.remove(self)
    

    def cambiar_direccion(self):
        self.direccion *= -1
    def avanzar(self):
        self.rectangulo.x += 5
    def animar_con_imagen(self,pantalla):

        pantalla.blit(self.imagen,self.rectangulo)
    def animar(self, pantalla, que_animacion):
        #Tiene que ir bliteando cad a una de las imagenes de la animacion con la que voy a trabajar
        #Ante cada evento(teclass) hay que animar al personaje
        #Necesito (self,pantalla, que_animacion:str - clave del diccionario que voy a sacar del objeto que me dice que animacion hay que ejectuar)
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], (self.rectangulo.x,self.rectangulo.y))
        self.contador_pasos += 1
    def actualizar(self,pantalla,limite_derecho,limite_izquierdo):
        
        if not self.esta_muerto:
            self.movimiento_lateral()
            self.animar(pantalla,self.que_hace)
            
    def disparar(self):
        # Obtener la posición inicial del disparo
        x = self.lados["right"].centerx  # Posición X del centro del personaje
        y = self.lados["right"].centery  # Posición Y del centro del personaje
        
        # Crear un nuevo proyectil en la posición del personaje
        miProyectil = Proyectil("poder_uno.png",x, y)

        # Agregar el proyectil a la lista de proyectiles del personaje
        self.listaDisparo.append(miProyectil)
    def apply_gravity(self):
        maxima_altura = 550
        self.rectangulo.y += self.gravity_speed  # Assuming `self.rect` is the enemy's position and `self.gravity_speed` is the gravity effect.
        if self.rectangulo.y > maxima_altura:  # Replace `some_max_height` with the height limit, like the bottom of the screen or platform height.
            self.rectangulo.y = maxima_altura
            self.on_ground = True
    def check_platform_collision(self, platform):
        
        if self.rectangulo.colliderect(platform.rectangulo):  # Assuming each platform has a `rect` attribute.
            self.rectangulo.bottom = platform.rectangulo.top
            self.on_ground = True

    def make_movement_decision(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.last_decision_time > 5000:  # 5 seconds = 5000 milliseconds
            self.last_decision_time = tiempo_actual
            self.direction = random.choice([-1, 1])  # -1 for left, 1 for right
    def handle_screen_boundaries(self, W):
        if self.rectangulo.left < 0 or self.rectangulo.right > W-50:
            self.direction *= -1  # Change direction if hitting screen boundaries


    
