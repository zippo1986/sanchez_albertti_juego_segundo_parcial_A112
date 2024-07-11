import pygame
import sys
W,H = 1000, 600
FPS =20
screen_size = (W,H)
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(screen_size)
SPEED_ENEMY = 10
MAX_ENEMY = 10
SIZE_ENEMY = (50,50)
#font = pygame.font.SysFont(None, 20)
######CONFIGURACIONES######
##################################################

def obtener_rectangulo(principal)->dict:
   """Obtiene los rectangulos de un rectangulo principal

   Args:
       principal (.Rect): Rectangulo del cual se quieren obtener los rectangulos internos

   Returns:
       diccionario de rectangulos
   """
   diccionario = {}
   diccionario["main"] = principal
   diccionario["bottom"] = pygame.Rect(principal.left+17, principal.bottom -5, principal.width-31, 5)
   diccionario["right"] = pygame.Rect(principal.right -2, principal.top+2, 5, principal.height-40)
   diccionario["left"] = pygame.Rect(principal.left+2, principal.top+2,5,principal.height-40)
   diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
   return diccionario

def girar_imagenes(lista_original,flip_x, flip_y):
   """gira las imagenes

   Args:
       lista_original (list): lista de diccionarios de animaciones
       flip_x (_type_): _description_
       flip_y (_type_): _description_

   Returns:
       list: Lista de imagenes giradas
   """
   lista_girada=[]
   for imagen in lista_original:

      lista_girada.append(pygame.transform.flip(imagen, flip_x , flip_y))
   return lista_girada

def reescalar_imagen(lista_imagenes, width, height):
   """Reescala las imagenes al tamaño pasado por parametro

   Args:
       lista_imagenes (list): lista de imagenes
       width (int): ancho deseado de la imagen
       height (_int): alto deseado de la imagen
   """
   for i in range(len(lista_imagenes)):

      lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (width,height))
      
      



###################################################

personaje_quieto = [pygame.image.load("epsilon_eagle/quieto/0.png"),
                    pygame.image.load ("epsilon_eagle/quieto/1.png"),
                    pygame.image.load ("epsilon_eagle/quieto/2.png"),
                    pygame.image.load ("epsilon_eagle/quieto/3.png"),
                    pygame.image.load ("epsilon_eagle/quieto/4.png"),
                    ]

personaje_camina_derecha = [pygame.image.load("epsilon_eagle/corre/3.png"),
                       pygame.image.load("epsilon_eagle/corre/4.png"),
                       pygame.image.load("epsilon_eagle/corre/5.png"), 
                       pygame.image.load("epsilon_eagle/corre/6.png"), 
                       ]
personaje_dispara_derecha = [pygame.image.load("epsilon_eagle/corre/3.png"),
                       pygame.image.load("epsilon_eagle/corre/4.png"),
                       pygame.image.load ("epsilon_eagle/ataque/1.png"),
                       pygame.image.load("epsilon_eagle/corre/5.png"), 
                       pygame.image.load("epsilon_eagle/corre/6.png"), 
                       ]
personaje_atacando = [
                       pygame.image.load ("epsilon_eagle/ataque/1.png")
                       
                    ]
personaje_salta = [pygame.image.load("epsilon_eagle/salta/0.png"),
                       pygame.image.load ("epsilon_eagle/salta/0.png"), 
                       pygame.image.load("epsilon_eagle/salta/0.png"),
                       pygame.image.load("epsilon_eagle/salta/1.png"), 
                       pygame.image.load("epsilon_eagle/salta/1.png"),
                       pygame.image.load("epsilon_eagle/salta/2.png"),
                       pygame.image.load("epsilon_eagle/salta/2.png"),
                       pygame.image.load("epsilon_eagle/salta/2.png")

                    ]
personaje_agachado = [pygame.image.load("epsilon_eagle/agachado/3.png"),
                       pygame.image.load ("epsilon_eagle/agachado/4.png"), 
                       pygame.image.load("epsilon_eagle/agachado/5.png")
                    ]
enemigo_camina_izq = [pygame.image.load("enemigo_uno/corre_izq/0.png"),
                      pygame.image.load("enemigo_uno/corre_izq/1.png"),
                      pygame.image.load("enemigo_uno/corre_izq/2.png"),
                      pygame.image.load("enemigo_uno/corre_izq/3.png")
                      ]
personaje_muere= [
                      pygame.image.load("epsilon_eagle/muerto/0.png"),
                      pygame.image.load("epsilon_eagle/muerto/1.png")
                
]
enemigo_muere =[
                pygame.image.load("enemigo_muerte/muerto_cero.png"),
                pygame.image.load("enemigo_muerte/muerto_uno.png"),
                pygame.image.load("enemigo_muerte/muerto_uno.png"),
                pygame.image.load("enemigo_muerte/muerto_uno.png")
                
]

boss_quieto = [
    pygame.image.load("boss_final/demon_idle/0.png"),
    pygame.image.load("boss_final/demon_idle/1.png"),
    pygame.image.load("boss_final/demon_idle/2.png"),
    pygame.image.load("boss_final/demon_idle/3.png"),
    pygame.image.load("boss_final/demon_idle/4.png"),
    pygame.image.load("boss_final/demon_idle/5.png")


]

boss_caminar= [
   pygame.image.load("boss_final/demon_walk/0.png"),
   pygame.image.load("boss_final/demon_walk/1.png"),
   pygame.image.load("boss_final/demon_walk/2.png"),
   pygame.image.load("boss_final/demon_walk/3.png"),
   pygame.image.load("boss_final/demon_walk/4.png"),
   pygame.image.load("boss_final/demon_walk/5.png"),
   pygame.image.load("boss_final/demon_walk/6.png"),
   pygame.image.load("boss_final/demon_walk/7.png"),
   pygame.image.load("boss_final/demon_walk/8.png"),
   pygame.image.load("boss_final/demon_walk/9.png"),
   pygame.image.load("boss_final/demon_walk/10.png"),
   pygame.image.load("boss_final/demon_walk/11.png")

]

boss_ataque_uno=[
   pygame.image.load("boss_final/demon_cleave/0.png"),
   pygame.image.load("boss_final/demon_cleave/1.png"),
   pygame.image.load("boss_final/demon_cleave/2.png"),
   pygame.image.load("boss_final/demon_cleave/3.png"),
   pygame.image.load("boss_final/demon_cleave/4.png"),
   pygame.image.load("boss_final/demon_cleave/5.png"),
   pygame.image.load("boss_final/demon_cleave/6.png"),
   pygame.image.load("boss_final/demon_cleave/7.png"),
   pygame.image.load("boss_final/demon_cleave/8.png"),
   pygame.image.load("boss_final/demon_cleave/9.png"),
   pygame.image.load("boss_final/demon_cleave/10.png"),
   pygame.image.load("boss_final/demon_cleave/11.png"),
   pygame.image.load("boss_final/demon_cleave/12.png"),
   pygame.image.load("boss_final/demon_cleave/13.png"),

]

boss_muerto = [
    
   pygame.image.load("boss_final/demon_death/0.png"),
   pygame.image.load("boss_final/demon_death/1.png"),
   pygame.image.load("boss_final/demon_death/2.png"),
   pygame.image.load("boss_final/demon_death/3.png"),
   pygame.image.load("boss_final/demon_death/4.png"),
   pygame.image.load("boss_final/demon_death/5.png"),
   pygame.image.load("boss_final/demon_death/6.png"),
   pygame.image.load("boss_final/demon_death/7.png"),
   pygame.image.load("boss_final/demon_death/8.png"),
   pygame.image.load("boss_final/demon_death/9.png"),
   pygame.image.load("boss_final/demon_death/10.png"),
   pygame.image.load("boss_final/demon_death/11.png"),
   pygame.image.load("boss_final/demon_death/12.png"),
   pygame.image.load("boss_final/demon_death/13.png"),
   pygame.image.load("boss_final/demon_death/14.png"),
   pygame.image.load("boss_final/demon_death/15.png"),
   pygame.image.load("boss_final/demon_death/16.png"),
   pygame.image.load("boss_final/demon_death/17.png"),
   pygame.image.load("boss_final/demon_death/18.png"),
   pygame.image.load("boss_final/demon_death/19.png"),
   pygame.image.load("boss_final/demon_death/20.png"),


]
boss_golpeado= [pygame.image.load("boss_final/demon_take_hit/0.png"),
   pygame.image.load("boss_final/demon_take_hit/1.png"),
   pygame.image.load("boss_final/demon_take_hit/2.png"),
   pygame.image.load("boss_final/demon_take_hit/3.png"),
   pygame.image.load("boss_final/demon_take_hit/4.png"),
   


    
]
boss_ataque_dos=[pygame.image.load("boss_final/demon_ataque_dos/0.png"),
   pygame.image.load("boss_final/demon_ataque_dos/1.png"),
   pygame.image.load("boss_final/demon_ataque_dos/2.png"),
   
    
]

enemigo_camina_der= girar_imagenes(enemigo_camina_izq,True,False)

boss_caminar_derecha = girar_imagenes(boss_caminar, True,False)
personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha,True,False)
personaje_ataca_izquierda = girar_imagenes(personaje_dispara_derecha,True,False)
personaje_salta_izquierda = girar_imagenes(personaje_salta,True,False)

diccionario_animaciones={}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones ["camina_derecha"] = personaje_camina_derecha
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["ataca_derecha"] = personaje_dispara_derecha
diccionario_animaciones["ataca_izquierda"]= personaje_ataca_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["salta_izquierda"]= personaje_salta_izquierda
diccionario_animaciones["atacando"] = personaje_atacando
diccionario_animaciones["agachado"] = personaje_agachado
diccionario_animaciones["enemigo_izq"]= enemigo_camina_izq
diccionario_animaciones["enemigo_der"]= enemigo_camina_der
diccionario_animaciones["muere"] = personaje_muere
diccionario_animaciones["enemigo_muere"] = enemigo_muere

diccionario_boss = {}
diccionario_boss["boss_quieto"] = boss_quieto
diccionario_boss["boss_ataque_uno"] = boss_ataque_uno
diccionario_boss["boss_caminar"] =boss_caminar
diccionario_boss["boss_hit"] = boss_golpeado
diccionario_boss["boss_derecha"] = boss_caminar_derecha
diccionario_boss["boss_ataque_dos"] = boss_ataque_dos

