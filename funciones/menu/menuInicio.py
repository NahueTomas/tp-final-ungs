import os

import pygame
import pygame_menu
from pygame import mixer

from funciones.sonidos.efectoSonido import efectoSonido


# Menu inicio
def menuInicio(ancho, alto, main):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    screen = pygame.display.set_mode((ancho, alto))
    menu = pygame_menu.Menu('La escondida', ancho, alto,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.text_input('Jugador: ', default='')
    menu.add.selector(
        'Dificultad :', [('Hard', 1), ('Easy', 2)], onchange=dificultad)
    menu.add.selector('Niveles :', [
                      ('Animales', 1), ('Superheroes', 2), ('Paises', 3)], onchange=dificultad)
    menu.add.button('Jugar', main)
    menu.add.button('Salir', pygame_menu.events.EXIT)

    # musica
    musica = efectoSonido(5)
    mixer.music.load(musica)
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    menu.mainloop(screen)


def dificultad():
    pass
