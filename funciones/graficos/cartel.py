import pygame
from pygame.locals import *

from config.configuracion import COLOR_CORRECTA, COLOR_INCORRECTA, COLOR_CARTEL, TAMANNO_LETRA_GRANDE


# CREACION DEL CARTEL FINAL
def cartel(screen, titulo, colorFont, colorCartel, fontSize, subtitle=''):
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), fontSize)
    screen_rect = screen.get_rect()
    center = screen_rect.center
    posX = center[0] - 350
    posY = center[1] - 200
    rect = pygame.Rect(posX, posY, 700, 300)
    centerCartel = rect.center
    pygame.draw.rect(screen, colorCartel, rect, 0)

    mensajeG = defaultFontGrande.render(titulo, 1, colorFont)
    width = mensajeG.get_width()
    screen.blit(
        mensajeG, (centerCartel[0] - (width // 2), centerCartel[1] - 80))
    if (subtitle):
        subtitleG = pygame.font.Font(
            pygame.font.get_default_font(), 20).render(subtitle, 1, colorFont)
        width = subtitleG.get_width()
        screen.blit(
            subtitleG, (centerCartel[0] - (width // 2), centerCartel[1] - 20))

    exitBtn = pygame.draw.rect(screen, 'red', pygame.Rect(80, 340, 80, 40), 0)
    playAgainBtn = pygame.draw.rect(
        screen, 'green', pygame.Rect(600, 340, 80, 40), 0)
    menuBtn = pygame.draw.rect(
        screen, 'orange', pygame.Rect(350, 340, 80, 40), 0)

    ev = pygame.event.get()

    for event in ev:
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if (exitBtn.collidepoint(pos)):
                pygame.quit()
            if (playAgainBtn.collidepoint(pos)):
                return 'reset'
            if (menuBtn.collidepoint(pos)):
                return 'menu'
        if event.type == QUIT:
            pygame.quit()

 # Cartel GANAR


def cartelGanar(screen):
    return cartel(screen, "GANASTE!!!", COLOR_CORRECTA,
                  COLOR_CARTEL, TAMANNO_LETRA_GRANDE)


# Cartel PERDER
def cartelPerder(screen, palabraCorrecta):
    return cartel(screen, "PERDISTE!!",
                  COLOR_INCORRECTA, COLOR_CARTEL, TAMANNO_LETRA_GRANDE, "La palabra correcta era: " + palabraCorrecta.upper())


def cartelTermino(screen, cant_palabras):
    return cartel(screen, 'TERMINO EL TIEMPO!', COLOR_CORRECTA, COLOR_CARTEL, TAMANNO_LETRA_GRANDE, "Acertaste " + cant_palabras + ' palabras :D')
