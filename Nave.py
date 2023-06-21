import pygame
from Constantes import *
from Disparo_Nave import Disparos
class Nave:
    def __init__(self):
        self.imagen = pygame.image.load("Imagenes/nave.png")
        self.rect = self.imagen.get_rect()
        self.puntaje = 0
        self.rect.centerx = ANCHO_VENTANA // 2
        self.rect.bottom = ALTO_VENTANA - 10
        self.puntaje = 0

    def moverse(self):
        teclas = pygame.key.get_pressed()
        velocidad = 5
        posicion_x = 0
        if teclas[pygame.K_a]:
            posicion_x -= 1  
        elif teclas[pygame.K_d]:
            posicion_x += 1  
        if self.rect.right > ANCHO_VENTANA:
            self.rect.right = ANCHO_VENTANA
        if self.rect.left < 0:
            self.rect.left = 0  

        self.rect.x += posicion_x * velocidad

    def disparar_derecha(self):
        bala = Disparos(self.rect.centerx + 23, self.rect.top + 40,"./Imagenes/laser nave.png")
        return bala
    
    def disparar_izquierda(self):
        bala = Disparos(self.rect.centerx - 23, self.rect.top + 40,"./Imagenes/laser nave.png")
        return bala 
    
    def actualizar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

    