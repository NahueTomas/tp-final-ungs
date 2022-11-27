import os

import pygame
import pygame_menu
from pygame import mixer

from funciones.sonidos.efectoSonido import efectoSonido


# Menu inicio
def menuInicio(ancho, alto, normalMode):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    screen = pygame.display.set_mode((ancho, alto))
    menu = pygame_menu.Menu('La escondida', ancho, alto,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.selector('Dificultad: ', [
                      ('Fácil', 5),  ('Normal', 6), ('Dificil', 8)], selector_id='letras')

    menu.add.selector('Temática: ', [
        ('Random', ''),  ('Animales', 'animales'), ('Vestimenta', 'vestimenta'), ('Comida', 'comida')], selector_id='tematicas')

    menu.add.button('Jugar Normal', lambda: play_game(
        menu.get_input_data(), normalMode))

    menu.add.button('Jugar por tiempo', normalMode)

    menu.add.button('Jugar por intentos', normalMode)

    menu.add.button('Ranking', normalMode)

    menu.add.button('Salir', pygame_menu.events.EXIT)

    # musica
    musica = efectoSonido(5)
    mixer.music.load(musica)
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    menu.mainloop(screen)


def play_game(inputs, game):
    letras = inputs['letras'][0][1]
    tematica = inputs['tematicas'][0][1]
    game(letras, tematica)
