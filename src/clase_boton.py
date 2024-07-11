import pygame
pygame.font.init()
class Boton:
    def __init__(self, etiqueta, imagen: str, posicion: list, ancho, alto, texto, color_texto,es_visible):
        self.etiqueta = etiqueta
        self.imagen = None
        self.es_visible = es_visible
        if imagen:
            self.imagen = pygame.image.load(imagen)
        self.rect = pygame.Rect(posicion[0], posicion[1], ancho, alto)
        self.texto = texto
        self.color_texto = color_texto
        self.fuente = pygame.font.Font(None, 36)

    def dibujar_boton(self, pantalla):
        if self.imagen:
            imagen_redimensionada = pygame.transform.scale(self.imagen, (self.rect.width, self.rect.height))
            pantalla.blit(imagen_redimensionada, self.rect.topleft)
        else:
            pygame.draw.rect(pantalla, (255, 255, 255), self.rect)
        
        texto_renderizado = self.fuente.render(self.texto, True, self.color_texto)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)
        pantalla.blit(texto_renderizado, texto_rect)

    def es_presionado(self, evento):
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                return True
        return False