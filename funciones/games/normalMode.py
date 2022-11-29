#! /usr/bin/env python
import os
import time

import pygame
from pygame.locals import *
from pygame import mixer  # sonido

from config.configuracion import ANCHO, ALTO, TIEMPO_MAX, FPS_inicial, COLOR_FONDO

from funciones.sonidos.efectoSonido import efectoSonido
from funciones.sonidos.reproducirMusica import reproducirMusica
from funciones.teclado.dameLetraApretada import dameLetraApretada
from funciones.palabras.revision import revision
from funciones.palabras.nuevaPalabra import nuevaPalabra
from funciones.palabras.lectura import lectura
from funciones.graficos.dibujar import dibujar
from funciones.graficos.cartel import cartelGanar, cartelPerder


# Funcion principal
def normalMode(cant_letras, tematica):
    while True:
        # Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        # Preparar la ventana
        pygame.display.set_caption("La escondida...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        # tiempo total del juego
        tiempoInicial = time.time()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        # Musica Inicio
        musica = efectoSonido(0)
        mixer.music.load(musica)
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

        puntos = 0
        palabraUsuario = ""
        listaPalabrasDiccionario = []
        ListaDePalabrasUsuario = []
        gano = False
        perdio = False

        archivo = open('assets/txt/lemario.txt', 'r')

        # lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario, cant_letras, tematica)

        # elige una al azar
        palabraCorrecta = nuevaPalabra(listaPalabrasDiccionario)

        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario,
                puntos, segundos, gano, palabraCorrecta)

        print(palabraCorrecta)
        intentos = 5

        while (True):
            if (not (segundos > (fps / 1000) and intentos)):
                perdio = True

            if (not (perdio or gano)):
                # 1 frame cada 1/fps segundos
                tiempoActal = time.time()
                totaltime = (tiempoActal - tiempoInicial)
                segundos = TIEMPO_MAX - totaltime

                # Buscar la tecla apretada del modulo de eventos de pygame
                for e in pygame.event.get():
                    # QUIT es apretar la X en la ventana
                    if e.type == QUIT:
                        pygame.quit()
                        return ()

                    # Ver si fue apretada alguna tecla
                    if e.type == KEYDOWN:
                        letra = dameLetraApretada(e.key)
                        palabraUsuario += letra  # es la palabra que escribe el usuario
                        if e.key == K_BACKSPACE:
                            palabraUsuario = palabraUsuario[0:len(
                                palabraUsuario)-1]
                        if e.key == K_RETURN:
                            if len(palabraUsuario) == cant_letras and palabraUsuario in listaPalabrasDiccionario and palabraUsuario not in ListaDePalabrasUsuario:
                                gano = revision(
                                    palabraCorrecta, palabraUsuario)
                                ListaDePalabrasUsuario.append(palabraUsuario)
                                palabraUsuario = ""

                                if gano:
                                    # Sonido de palabra correcta
                                    ganar = efectoSonido(2)
                                    otro = mixer.Sound(ganar)
                                    otro.play()

                                    puntos += 10
                                else:
                                    # Sonido de palabra incorrecta / casi
                                    error = efectoSonido(1)
                                    otro = mixer.Sound(error)
                                    otro.play()
                                    intentos -= 1

            # Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            # Dibujar de nuevo todo
            dibujar(screen, ListaDePalabrasUsuario, palabraUsuario,
                    puntos, segundos, gano, palabraCorrecta)

            # Reproduccion de Banda sonora
            musica = reproducirMusica(segundos)

            if gano:  # cartel ganar
                res = cartelGanar(screen)
                if (res == 'reset'):
                    break
                elif (res == 'menu'):
                    return

            if perdio:  # cartel perder
                res = cartelPerder(screen, palabraCorrecta)
                if (res == 'reset'):
                    break
                elif (res == 'menu'):
                    return

            pygame.display.flip()

    archivo.close()
