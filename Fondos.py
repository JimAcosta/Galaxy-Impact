import pygame
from Constantes import *

class Fondo:
    def __init__(self):
        self.imagen_original = pygame.image.load("./Imagenes/Fondo.png")
        self.imagen = pygame.transform.scale(self.imagen_original, (ANCHO_VENTANA, ALTO_VENTANA))
        self.rect = self.imagen.get_rect()
        self.y = 0
        self.centerx = self.rect.width // 2
        self.centery = self.rect.height // 2
        

    def mover_fondo(self):
        self.y += 1  
        if self.y >= self.rect.height:
            self.y = 0

    def dibujar(self,pantalla):
        pantalla.blit(self.imagen, (0, self.y))
        pantalla.blit(self.imagen, (0, self.y - self.rect.height))
