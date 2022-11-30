import pygame
from pygame.locals import *

from config.configuracion import COLOR_CORRECTA, COLOR_INCORRECTA, COLOR_CARTEL, TAMANNO_LETRA_GRANDE


# CREACION DEL CARTEL FINAL
def cartel(screen, titulo, colorFont, fontSize, subtitle=''):
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), fontSize)
    screen_rect = screen.get_rect()
    center = screen_rect.center
    posX = center[0] - 350
    posY = center[1] - 200
    cartel = pygame.image.load('assets/img/CARTEL.jpg')
    screen.blit(cartel, (posX, posY))

    mensajeG = defaultFontGrande.render(titulo, 1, colorFont)
    width = mensajeG.get_width()
    screen.blit(mensajeG, (center[0] - width // 2, 120))
    if (subtitle):
        subtitleG = pygame.font.Font(
            pygame.font.get_default_font(), 20).render(subtitle, 1, colorFont)
        width = subtitleG.get_width()
        screen.blit(
            subtitleG, (center[0] - width // 2, 180))

    exitBtn = pygame.image.load('assets/img/BTN-SALIR.jpg')
    screen.blit(exitBtn, (80, 340))
    exitBtnRect = pygame.draw.rect(
        screen, 'white', pygame.Rect(80, 340, 80, 40), 1)

    playAgainBtn = pygame.image.load('assets/img/BTN-JDN.jpg')
    screen.blit(playAgainBtn, (600, 340))
    playAgainBtnRect = pygame.draw.rect(
        screen, 'white', pygame.Rect(600, 340, 80, 40), 1)

    menuBtn = pygame.image.load('assets/img/BTN-MENU.jpg')
    screen.blit(menuBtn, (350, 340))
    menuBtnRect = pygame.draw.rect(
        screen, 'white', pygame.Rect(350, 340, 80, 40), 1)

    ev = pygame.event.get()
    for event in ev:
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if (exitBtnRect.collidepoint(pos)):
                pygame.quit()
            if (playAgainBtnRect.collidepoint(pos)):
                return 'reset'
            if (menuBtnRect.collidepoint(pos)):
                return 'menu'
        if event.type == QUIT:
            pygame.quit()

 # Cartel GANAR


def cartelGanar(screen):
    return cartel(screen, "GANASTE!!!", COLOR_CORRECTA, TAMANNO_LETRA_GRANDE)


# Cartel PERDER
def cartelPerder(screen, palabraCorrecta):
    return cartel(screen, "PERDISTE!!", COLOR_INCORRECTA, TAMANNO_LETRA_GRANDE, "La palabra correcta era: " + palabraCorrecta.upper())


def cartelTermino(screen, cant_palabras):
    return cartel(screen, 'TERMINO EL TIEMPO!', COLOR_CORRECTA, TAMANNO_LETRA_GRANDE, "Acertaste " + cant_palabras + ' palabras :D')
