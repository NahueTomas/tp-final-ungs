import pygame_menu
from funciones.menu.menuRanking import menuRanking
from funciones.games.normalMode import normalMode


def menuInicial(menu):
    menu.add.selector('Dificultad: ', [
                      ('Fácil', 5),  ('Normal', 6), ('Dificil', 8)], selector_id='letras')

    menu.add.selector('Temática: ', [
        ('Random', ''),  ('Animales', 'animales'), ('Vestimenta', 'vestimenta'), ('Comida', 'comida')], selector_id='tematicas')

    menu.add.button('Jugar Normal', lambda: play_game(
        menu.get_input_data(), normalMode))

    menu.add.button('Jugar por tiempo', normalMode)

    menu.add.button('Ranking', lambda: cambiar_menu(menu))

    menu.add.button('Salir', pygame_menu.events.EXIT)


def play_game(inputs, game):
    letras = inputs['letras'][0][1]
    tematica = inputs['tematicas'][0][1]
    game(letras, tematica)


def cambiar_menu(menu):
    menu.clear()
    menuRanking(menu)
