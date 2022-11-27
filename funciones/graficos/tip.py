import pygame
from config.configuracion import COLOR_BLANCO, TAMANNO_LETRA


def tip(message, screen):
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), 12)
    screen_rect = screen.get_rect()
    center = screen_rect.center

    posX = center[0] - 70
    posY = 10

    rect = pygame.Rect(posX, posY, 140, 30)
    centerCartel = rect.center
    pygame.draw.rect(screen, COLOR_BLANCO, rect, 1)
    mensajeG = defaultFontGrande.render(message, 1, COLOR_BLANCO)
    width = mensajeG.get_width()
    height = mensajeG.get_height()
    screen.blit(
        mensajeG, (centerCartel[0] - (width // 2), centerCartel[1] - (height // 2)))
