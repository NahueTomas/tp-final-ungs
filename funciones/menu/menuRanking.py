import pygame_menu

from funciones.archivos.traerMejores import traerMejores


def menuRanking(menu):
    exit = False

    ranking = traerMejores()
    mejores = []
    for person in range(3):
        mejores.append(ranking[person])

    if (len(mejores) > 0):
        for index in range(len(mejores)):
            print(mejores[index])
            menu.add.label(str(mejores[index][1]) +
                           'ptos  - ' + str(mejores[index][0]))

    menu.add.label('')
    menu.add.label('')
    menu.add.label('')
    menu.add.button('Volver', lambda: close_menu(exit))
    menu.add.button('Salir', pygame_menu.events.EXIT)

    if (exit == True):
        return


def play_game(inputs, game):
    letras = inputs['letras'][0][1]
    tematica = inputs['tematicas'][0][1]
    game(letras, tematica)


def close_menu(exit):
    exit = True
    return
