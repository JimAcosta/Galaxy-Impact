import pygame
import random
from Constantes import *
from Disparo_Enemigo import Disparo_Enemigo

class Enemigos:
    def __init__(self):
        self.imagen = pygame.image.load("Imagenes\enemigo.png")
        self.rect = self.imagen.get_rect()
        self.velocidad_x = 5
        self.velocidad_y = 2
        self.lado = random.choice(['izquierda', 'derecha'])
        self.tiempo_caida = 1000
              
    def aparecer(self):
        if self.lado == 'izquierda':
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(0, ((ALTO_VENTANA // 4) * 2))
            self.velocidad_x = random.randint(2, 5)
        elif self.lado == 'derecha':
            self.rect.x = ANCHO_VENTANA
            self.rect.y = random.randint(0, ((ALTO_VENTANA // 4) * 2))
            self.velocidad_x = -random.randint(2, 5)
            

    def actualizar(self):
            self.rect.x += self.velocidad_x
            if self.lado == 'izquierda' and self.rect.right > ANCHO_VENTANA:
                self.aparecer()
            elif self.lado == 'derecha' and self.rect.left < 0:
                self.aparecer()

    def disparar(self):
        disparos_nave = []
        for i in range (0,3):
            disparo = Disparo_Enemigo("Imagenes\laser enemigo.png")
            disparos_nave.append(disparo)
        return disparos_nave
    
    def dibujar(self, pantalla):
            self.actualizar()
            pantalla.blit(self.imagen, self.rect)
            if pygame.time.get_ticks() - self.tiempo_caida >= 1000:
                self.rect.y += self.velocidad_y
                
  

    