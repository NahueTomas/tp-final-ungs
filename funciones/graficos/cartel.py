import pygame
from config.configuracion import COLOR_CORRECTA, COLOR_INCORRECTA, COLOR_CARTEL, TAMANNO_LETRA_GRANDE


# CREACION DEL CARTEL FINAL
def cartel(screen, titulo, colorFont, colorCartel, fontSize):
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), fontSize)
    screen_rect = screen.get_rect()
    center = screen_rect.center
    posY = center[0] - 200
    posX = center[1] - 200
    rect = pygame.Rect(posY, posX, 400, 250)
    centerCartel = rect.center
    pygame.draw.rect(screen, colorCartel, rect, 0)
    mensajeG = defaultFontGrande.render(titulo, 1, colorFont)
    width = mensajeG.get_width()
    height = mensajeG.get_height()
    screen.blit(
        mensajeG, (centerCartel[0] - (width // 2), centerCartel[1] - (height // 2)))


# Cartel GANAR
def cartelGanar(screen):
    cartel(screen, "GANASTE!!!", COLOR_CORRECTA,
           COLOR_CARTEL, TAMANNO_LETRA_GRANDE)


# Cartel PERDER
def cartelPerder(screen, palabraCorrecta):
    cartel(screen, "PERDISTE!! la palabra es : " +
           palabraCorrecta, COLOR_INCORRECTA, COLOR_CARTEL, TAMANNO_LETRA_GRANDE)
