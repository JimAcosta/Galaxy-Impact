import pygame
from Constantes import *
from Fondos import Fondo
from Nave import Nave
from Naves_enemigas import Enemigos
from Funciones import *

pygame.init()
pygame.mixer.init()
audio_disparo_nave = pygame.mixer.Sound("Audios\laser.wav")
audio_choque_nave = pygame.mixer.Sound("Audios\explosion.wav")
audio_eliminar_enemigo = pygame.mixer.Sound("Audios\golpe.wav")
audio_disparo_nave.set_volume(0.3)
audio_choque_nave.set_volume(0.3)
audio_eliminar_enemigo.set_volume(0.3)
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
reloj = pygame.time.Clock()
fondo = Fondo()
nave = Nave()
enemigos = []
disparos_izquierda = []
disparos_derecha = []
disparos_enemigos = []
font = pygame.font.SysFont("Gotham", 25)
flag_correr = True
flag_inicio = True
flag_perder = False
fps = 40

while flag_correr:
        flag_inicio = inicio(flag_inicio,pantalla,fondo,fps,reloj)
        flag_perder = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  
                    disparos_izquierda.append(nave.disparar_izquierda())
                    audio_disparo_nave.play() 
                elif evento.button == 3:
                    disparos_derecha.append(nave.disparar_derecha())
                    audio_disparo_nave.play()
            
        if nave.puntaje <100:  
            if len(enemigos) < 2:
                enemigo = Enemigos()
                enemigo.aparecer()
                disparos_enemigos = enemigo.disparar()
                enemigos.append(enemigo)

        elif nave.puntaje > 100 and nave.puntaje < 200: 
            if len(enemigos) < 4:
                enemigo = Enemigos()
                enemigo.aparecer()
                disparos_enemigos = enemigo.disparar()
                enemigos.append(enemigo)

        elif nave.puntaje > 200 : 
            if len(enemigos) < 6:
                enemigo = Enemigos()
                enemigo.aparecer()
                disparos_enemigos = enemigo.disparar()
                enemigos.append(enemigo)
                fps += 1
                if fps > 80:
                    fps = 80

        nave.moverse()
        fondo.mover_fondo()
        fondo.dibujar(pantalla)
        nave.actualizar(pantalla)

        for enemigo in enemigos:
            enemigo.dibujar(pantalla)
            enemigo.actualizar()
            for disparo in disparos_enemigos:
                disparo.dibujar(enemigo,pantalla)
            if nave.rect.colliderect(enemigo.rect) or nave.rect.colliderect(disparo.rect):
                audio_choque_nave.play()
                if flag_perder == False:
                    flag_inicio = game_over(pantalla,fondo,nave,fps,reloj)
                    flag_perder = flag_inicio
                    enemigos = []
                    disparos_izquierda = []
                    disparos_derecha = []
                    disparos_enemigos = []
                    nave.puntaje = 0
                    fps = 40

        frase = ("Puntuacion:{0}").format(nave.puntaje)
        text = font.render(frase, True, (200, 0, 0))
        colicionar(disparos_derecha,enemigos,pantalla,nave,audio_eliminar_enemigo)
        colicionar(disparos_izquierda,enemigos,pantalla,nave,audio_eliminar_enemigo)
        
        pantalla.blit(text, (0, 0))
        pygame.display.flip()
        reloj.tick(fps)

pygame.quit()