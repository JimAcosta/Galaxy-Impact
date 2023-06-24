import pygame
from Constantes import *

class Disparos():
    def __init__(self, x, y,ruta):
        self.imagen = pygame.transform.scale(pygame.image.load(ruta).convert(), (25, 25))
        self.imagen.set_colorkey(COLOR_NEGRO)
        self.rect = self.imagen.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.velocidad = 20
        self.flag = True
        
    def dibujar(self, pantalla):
        if self.flag == True:
            self.rect.y -= self.velocidad  
            if self.rect.bottom < 0:
                return False  
            pantalla.blit(self.imagen, self.rect)
        return True

