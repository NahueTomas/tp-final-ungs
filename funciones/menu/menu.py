import os

import pygame
import pygame_menu
from pygame import mixer

from funciones.sonidos.efectoSonido import efectoSonido
from funciones.menu.menuInicial import menuInicial


# Menu inicio
def menuInicio(ancho, alto):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    screen = pygame.display.set_mode((ancho, alto))
    menu = pygame_menu.Menu('La escondida', ancho, alto,
                            theme=pygame_menu.themes.THEME_DARK)

    menuInicial(menu)

    # musica
    musica = efectoSonido(5)
    mixer.music.load(musica)
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    menu.mainloop(screen)
