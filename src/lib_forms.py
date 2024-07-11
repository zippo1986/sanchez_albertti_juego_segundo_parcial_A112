
from clase_formulario_ranking import *
from configuraciones import *
from clase_formulario_opciones import *
from class_formulario_inicio import *
from clase_formulario_puntaje import *



formulario_inicio = Formulario_inicio(PANTALLA,"img_form.png", "musica_inicio.mp3")
formulario_opciones = Formulario_opciones(PANTALLA,"img_form.png","musica_inicio.mp3")
formulario_puntaje= FormPuntaje(PANTALLA,"img_form.png","musica_inicio.mp3")
formulario_ranking =  FormularioRanking(PANTALLA, "img_form.png","musica_inicio.mp3")
