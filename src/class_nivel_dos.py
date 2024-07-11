from class_nivel import *
from class_enemigo import *
from funciones import *
from class_personaje import*
from class_vida import *
from pygame.locals import *
from modo import *
from class_plataforma import *
from class_plataformas_grandes import *
import pygame
def generar_pisos(imagen,coordenadas,lista_plataformas,lista_plataformas_dos):
    """Construye instancias de la clase plataforma 

    Args:
        imagen (pygame.image): imagen de las plataformas
        coordenadas (list): lista de coordenadas 
        lista_plataformas (list): lista de plataftormas donde se agregan las plataformas
        lista_plataformas_dos (list): lista de plataformas
    """
    for i in range(len(coordenadas)):
        for coordenada in coordenadas:
            x = coordenada[0]
            y = coordenada[1]
            plataforma= Plataforma(imagen,5,(x, y),100)
            lista_plataformas.append(plataforma)
            lista_plataformas_dos.append(plataforma)

def generar_vidas(lista_vidas,imagen,lista_coordenadas,tamanio):
    """construye instancias de la clase vida

    Args:
        lista_vidas (list): lista donde se agregan los objetos vida
        imagen (pygame.image): imagen de la vida 
        lista_coordenadas (list): _description_
        tamaño (list): lista de tamaños
    """
    for i in range(4):
        for coordenada in lista_coordenadas:
            vida = Vida(imagen,coordenada[0],coordenada[1],True)
            lista_vidas.append(vida)
def generar_coins(etiqueta,imagen,lista_coins,lista_coordenadas):
    """Construye instancias de la clase coin

    Args:
        etiqueta (str): un nombre para ponerle 
        imagen (_type_): _description_
        lista_coins (list): lista de monedas a agregar
        lista_coordenadas (list): lista de coordenadas
    """
    for i in range(4):
        for coordenada in lista_coordenadas:
            coin = Item(etiqueta,imagen,coordenada[0],coordenada[1],True,False, (20,20))
            lista_coins.append(coin)       
def generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final):
    """Construye instancias de la clase enemigo

    Args:
        lista_enemigos (list): lista donde se agregan los enemigos
        lista_posicion_inicial (list): lista de tuplas de posición inicial
        lista_posicion_final (list): lista de tuplas de posiciones finales
    """
        
    for i in range(len(lista_posicion_inicial)):
        enemigo = Enemigo(diccionario_animaciones,lista_posicion_inicial[i],lista_posicion_final[i],2)
        lista_enemigos.append(enemigo)


class nivel_dos_(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        W =pantalla.get_width()
        H = pantalla.get_height()
        ##FONDO###
        fondo = pygame.image.load("space_one.png")
        fondo = pygame.transform.scale(fondo, (W,H))
        
        ##PERSONAJE###
        musica = pygame.mixer.music.load("musica_nivel_uno.wav")
        #reproducir_musica("musica_nivel_uno.wav")
        posicion_inicial = (H//2-200,W//2) 
        ###Plataformas###
        coordenadas_piso = [(0,550),(98,550),(490,550),(588,550),(686,550),(784,550),(882,550),(98,340), (196,340),(294,340), (392,340),(490,340),(588,340),(686,340),(784,340),(882,340),(12,410),(12,470),(0,200),(98,200), (196,200),(294,200), (392,200),(490,200),(588,200),(686,200),(784,200), (895,268),(13,100),(196,100),(294,71), (392,71),(490,71),(588,71),(686,71),(784,71), (895,71),(899,71),(899,71),(136,129)]
        
        #################################################################################################
        
        
        ##ENEMIGOS###
        lista_posicion_inicial= [(730, 500),(842,290),(590,290),(700, 500),(842,150),(590,150)]
        lista_posicion_final=[(498,510),(590,330),(350,330),(498,510),(590,330),(350,330)]
        lista_enemigos = []
        generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final)
        lista_coordenadas=[(870,12),(920,12),(965,12)]
        
        ######LISTA ENEMIGOS QUE APARECEN DESPUES##########
        lista_posicion_inicial= [(848, 500),(842,150),(590,150)]
        lista_posicion_final=[(79,510),(590,330),(350,330)]
        lista_enemigos_switch = []
        generar_lista_enemigos(lista_enemigos_switch,lista_posicion_inicial,lista_posicion_final)
        lista_coordenadas=[(870,12),(920,12),(965,12)]
        ##################################################
        

        display = pygame.display.set_mode((W,H))
        #PROYECTIL
        #demo_proyectil= Proyectil (player.lados["main"].top, player.lad)
        #lados_proyectil = obtener_rectangulo(demo_proyectil.rect)
        #Enemigos

        #PISO CON CLASES:
        piso = Plataforma("nivel_dos/plataforma_space.png",0,(0,550), 1000)
        



       # Esto devuelve un diccionario de lados que voy a recorrene en el loop para dibujarlos si yo quiero acceder solo a un lado debería poner lados_piso["bottom"] y si le agrego lados_piso["bottom"].top es la parte de arriba del bottom
        

        #Esta es la lista para las imagenes
        plataformas_clases_dos = []
        #El problema ahora es que tengo que hacer lo mismo con los pisos grandes
        #Esta es la lista para los rect
        plataformas_clases = []
        generar_pisos("nivel_dos/plataforma_space.png", coordenadas_piso,plataformas_clases_dos,plataformas_clases)
        
        #PISO
        #enemigo_uno= Enemigo("enemigo1.png", (622,527),(413,527),3)
        #enemigos = [enemigo_uno]

        #en sprites van a estar tdoos los elementos del juego

        #En enemigos van a ir todos los sprites de enemigos
        #plataforma
        
        # Calcula el ancho disponible para las plataformas (restando el espacio entre ellas)
        
        # Calcula las coordenadas x de cada plataforma

        #ENEMIGOS

        item_vida = Item("vida","vida.png", 500,50,True,False,(30,30))
        item_combustible= Item("combustible","item_combustible.png", W-50,50,True,False,(30,30))
        item_weapon = Item("arma","weapon.png",49,386,True,False,(30,30))
        item_puerta_cerrada = Item("puerta_cerrada","nivel_dos/puerta_cerrada.png",900,500,True,False,(100,100))
        item_puerta_abierta = Item("puerta_abierta","nivel_dos/puerta_abierta.png",900,500,False,False,(100,100))
        item_switch_prendido= Item("switch_prendido","nivel_dos/switch_encendido.png",468,310,False,False,(70,70))
        item_switch_apagado = Item("switch_apagado","nivel_dos/switch_apagade.png",468,310,True,False,(70,70))
        lista_items = [item_combustible,item_vida, item_weapon,item_puerta_abierta,item_puerta_cerrada,item_switch_prendido,item_switch_apagado]
        lista_vidas = []
        generar_vidas(lista_vidas,"vidas.png",lista_coordenadas,(30,30))
        coordenadas_coins=[(145,285),(250,285),(339,285),(443,285),(528,285),(635,285),(741,285),(836,285),(718,151),(630,148),(540,144),(444,149),(336,149)]
        lista_coins = []
        lista_asteroides = []
        generar_coins("coin","coin_sprite.png",lista_coins,coordenadas_coins)
        jugador = Personaje (3,(50,50), diccionario_animaciones, posicion_inicial,10,lista_vidas)
       
        super().__init__(fondo,display,jugador,piso, plataformas_clases,plataformas_clases_dos,lista_items,lista_enemigos, lista_vidas, lista_coins,"musica_nivel_uno.wav")
