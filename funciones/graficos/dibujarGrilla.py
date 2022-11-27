import pygame
from config.configuracion import COLOR_BLANCO


# Dibuja la grilla donde van las letras
def dibujarGrilla(screen, cant_letras):
    screen_rect = screen.get_rect()
    center = screen_rect.center

    cuadradoTam = 50

    posX = center[0] - (cuadradoTam * cant_letras) // 2
    posY = center[1] - 160

    posGrilla = []

    for y in range(0, 5):
        for x in range(0, cant_letras):
            posRectX = (x * cuadradoTam) + posX
            posRectY = (y * cuadradoTam) + posY

            rect = pygame.Rect(posRectX, posRectY, cuadradoTam, cuadradoTam)
            pygame.draw.rect(screen, COLOR_BLANCO, rect, 1)
            posGrilla.append(rect.center)
    return posGrilla
