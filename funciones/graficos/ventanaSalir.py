import pygame
from config.configuracion import COLOR_BLANCO, COLOR_CARTEL2, TAMANNO_LETRA_GRANDE


def ventanaSalir(screen):
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    screen_rect = screen.get_rect()
    center = screen_rect.center
    posY = center[0] - 100
    posX = center[1] - 100
    rect = pygame.Rect(posY, posX, 200, 125)
    centerCartel = rect.center
    pygame.draw.rect(screen, COLOR_CARTEL2, rect, 1)
    mensajeG = defaultFontGrande.render(
        "¿Desea continuar? Y/N", 1, COLOR_BLANCO)
    width = mensajeG.get_width()
    height = mensajeG.get_height()
    screen.blit(
        mensajeG, (centerCartel[0] - (width // 2), centerCartel[1] - (height // 2)))
