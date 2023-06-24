import pygame
from Constantes import *

class Disparo_Enemigo():
    def __init__(self, ruta):
        self.imagen = pygame.transform.scale(pygame.image.load(ruta).convert(), (25, 25))
        self.imagen.set_colorkey(COLOR_NEGRO)
        self.rect = self.imagen.get_rect()
        self.velocidad = 0.5
        self.tiempo_inicio = pygame.time.get_ticks()  
        self.tiempo_espera = 1000 
        self.activo = True
        self.disparo_inicializado = False

    def actualizar(self):
        self.rect.y += self.velocidad

    def dibujar(self, nave, pantalla):
        while pygame.time.get_ticks() - self.tiempo_inicio >= self.tiempo_espera:
            if not self.disparo_inicializado:
                self.rect.centerx = nave.rect.centerx
                self.rect.centery = nave.rect.centery
                self.disparo_inicializado = True
            self.rect.y += self.velocidad
            pantalla.blit(self.imagen, self.rect)
            if self.rect.top > ALTO_VENTANA:
                return False
            return True
        
        if pantalla.blit(self.imagen, self.rect):
            return True
        
    def desaparecer(self):
        self.flag = False
