import pygame
from config.configuracion import COLOR_BLANCO


# Dibuja la grilla donde van las letras
def dibujarGrilla(screen):
    screen_rect = screen.get_rect()
    center = screen_rect.center

    posY = center[0] - 125
    posX = center[1] - 160

    posGrilla = []
    cuadradoTam = 50

    # 0 - 50 - 100 - 150 - 200
    for x in range(0, 201, cuadradoTam):
        for y in range(0, 201, cuadradoTam):
            rect = pygame.Rect(y + posY, x + posX, cuadradoTam, cuadradoTam)
            pygame.draw.rect(screen, COLOR_BLANCO, rect, 1)
            posGrilla.append(rect.center)
    return posGrilla
