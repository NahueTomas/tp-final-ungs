import pygame_menu


def menuRanking(menu):
    menu.add.button('Volver', pygame_menu.events.RESET)
    menu.add.button('Salir', pygame_menu.events.EXIT)


def play_game(inputs, game):
    letras = inputs['letras'][0][1]
    tematica = inputs['tematicas'][0][1]
    game(letras, tematica)
