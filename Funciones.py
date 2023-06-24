import pygame
from Constantes import *
from Instrucciones import *
import re

def puntaje(pantalla,fondo,fuente,diccionario):
    flag = True
    reloj = pygame.time.Clock()
    fps = 60
    fuente = pygame.font.SysFont("Gotham", 35)
    fuente2 = pygame.font.SysFont("Gotham", 45)
    
    while flag:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                flag = False
        fondo.mover_fondo()
        fondo.dibujar(pantalla)
        titulo = "Puntaje mas alto"
        texto_titulo = fuente2.render(titulo,True,COLOR_BLANCO)
        frase1 = ("Nombre:{0}").format(diccionario["Nombre"])
        texto1 = fuente.render(frase1, True, COLOR_BLANCO)
        frase2 = ("Puntaje:{0}").format(diccionario["Puntaje"])
        texto2 = fuente.render(frase2, True, COLOR_BLANCO)
        pantalla.blit(texto_titulo, (180, 50))
        pantalla.blit(texto1, (210, 120))
        pantalla.blit(texto2, (210, 160))
        pygame.display.flip()
        reloj.tick(fps)

def instrucciones(pantalla, fondo, fuente):
    flag = True
    reloj = pygame.time.Clock()
    fps = 60
    posicion_y = 50
    fuente = pygame.font.SysFont("Gotham", 25)
    lineas = manual.split("\n")
    while flag:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                flag = False
        fondo.mover_fondo()
        fondo.dibujar(pantalla)
        posicion_y = 50
        for linea in lineas:
            instruccion = fuente.render(linea, True, COLOR_BLANCO)
            pantalla.blit(instruccion, (10, posicion_y))
            posicion_y += 30
        pygame.display.flip()
        reloj.tick(fps)

def inicio(flag, pantalla, fondo, fps,reloj):
    fuente = pygame.font.SysFont("Comic Sans MS", 35)
    texto = ["Jugar", "Puntaje", "Instrucciones"]
    titulo = "Galaxy Impact"
    rect_mouse = pygame.Rect(0, 0, 10, 10)
    texto_rects = []
    while flag:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag = False
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if rect_mouse.colliderect(texto_rects[0]):
                        flag = False
                    if rect_mouse.colliderect(texto_rects[1]):
                        diccionario = leer_archivo("Puntaje_Mas_Alto.csv")
                        puntaje(pantalla,fondo,fuente,diccionario)
                    if rect_mouse.colliderect(texto_rects[2]):
                        instrucciones(pantalla, fondo, fuente)
        fondo.mover_fondo()
        fondo.dibujar(pantalla)
        x, y = pygame.mouse.get_pos()
        rect_mouse.x = x
        rect_mouse.y = y
        y_texto = pantalla.get_height() // 1.3 - len(texto) * 15 - 6
        for palabra in texto:
            tituloX = fuente.render(titulo, True, COLOR_BLANCO)
            text = fuente.render(palabra, True, COLOR_BLANCO)
            rect = text.get_rect()
            texto_rects.append(rect)
            rect.center = (pantalla.get_width() // 2, y_texto)
            pantalla.blit(text, rect)
            pantalla.blit(tituloX, (180, 150))
            y_texto += 50
        pygame.display.flip()
        reloj.tick(fps)
    return flag

def colicionar(lista_disparos_nave,lista_enemigos,pantalla,nave,audio):
    for disparo in lista_disparos_nave:
        if not disparo.dibujar(pantalla):
            lista_disparos_nave.remove(disparo)
        else:
            for enemigo in lista_enemigos:
                if disparo.rect.colliderect(enemigo.rect):
                    lista_enemigos.remove(enemigo)
                    audio.play()
                    nave.puntaje += 35
                    return nave.puntaje
                
def guardar_archivo(nombre_archivo:str,contenido_a_guardar:str)->bool:
    if(type(nombre_archivo) == str and type(contenido_a_guardar) == str):
        with open(nombre_archivo,'w+') as archivo:
            archivo.write(contenido_a_guardar)
            mensaje = ("Se creo el archivo: {0}").format(nombre_archivo)
            print(mensaje)
            retorno = True
    else:
        mensaje = ("‘Error al crear el archivo:{0}").format(nombre_archivo)
        print(mensaje)
        retorno = False
    return retorno

def leer_archivo(nombre_archivo):
    diccionario = {}
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
        datos = re.split(',', texto)  
        diccionario["Nombre"] = datos[0]
        diccionario["Puntaje"] = int(datos[1])
    return diccionario

def game_over(pantalla, fondo, nave, fps,reloj):
    ingreso = ""
    fuente1 = pygame.font.SysFont("Gotham", 30)
    fuente2 = pygame.font.SysFont("Gotham", 55)
    texto1 = fuente1.render("Tu Puntuacion: {0}".format(nave.puntaje), True, (255, 255, 255))
    texto2 = fuente2.render("Game over", True, (255, 255, 255))
    texto3 = fuente2.render(ingreso, True, (255, 255, 255))
    text_nombre = fuente1.render("Nombre:", True, (255, 255, 255))
    flag = False
    
    while not flag:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                else:
                    ingreso += evento.unicode
                if evento.key == pygame.K_RETURN:
                    flag = True

        fondo.mover_fondo()
        fondo.dibujar(pantalla)
        texto3 = fuente1.render(ingreso, True, COLOR_BLANCO)
        pantalla.blit(texto1, (fondo.rect.centerx - 90, fondo.rect.centery + 100))
        pantalla.blit(texto2, (fondo.rect.centerx - 100, fondo.rect.centery - 90))
        pantalla.blit(text_nombre, (fondo.rect.centerx - 200, fondo.rect.centery + 120))
        pantalla.blit(texto3, (fondo.rect.centerx - 90, fondo.rect.centery + 120))
        pygame.display.flip()
        reloj.tick(fps)

    puntaje = ("{0},{1}").format(ingreso.strip(), nave.puntaje)
    diccionario = leer_archivo("Puntaje_Mas_Alto.csv")
    if nave.puntaje > diccionario["Puntaje"]:
        guardar_archivo("Puntaje_Mas_Alto.csv", puntaje)

    return flag 


