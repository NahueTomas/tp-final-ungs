import pygame

from config.configuracion import TAMANNO_LETRA, TAMANNO_LETRA_GRANDE, ALTO, ANCHO, COLOR_TEXTO, COLOR_TIEMPO_FINAL, COLOR_CORRECTA, COLOR_INCORRECTA, COLOR_CASI

from funciones.letras.letrasCorrecta import letrasCorrecta
from funciones.letras.letrasIncorrecta import letrasIncorrecta
from funciones.letras.letrasCasi import letrasCasi
from funciones.graficos.dibujarGrilla import dibujarGrilla


# Dibuja los gráficos principales
def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, palabraCorrecta):
    defaultFont = pygame.font.Font(
        pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande = pygame.font.Font(
        pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    # Linea Horizontal
    pygame.draw.line(screen, (255, 255, 255),
                     (0, ALTO-70), (ANCHO, ALTO-70), 5)

    # muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    # muestra el puntaje
    screen.blit(defaultFont.render(
        "Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    # muestra los segundos y puede cambiar de color con el tiempo

    if (segundos < 15):
        ren = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)

    else:
        ren = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
        screen.blit(ren, (10, 10))

    # Dibuja la grilla y devuelve una lista con las posiciones de cada cuadrado
    posGrilla = dibujarGrilla(screen)
    dibujarGrilla(screen)
    contador = 0

    # muestra las palabras anteriores, las que se fueron arriesgando
    for palabra in listaDePalabrasUsuario:
        # Obtenemos las letras correctas de la palabra
        correctas = letrasCorrecta(palabraCorrecta, palabra)
        # Obtenemos las letras correctas de una palabra casi correcta
        casi = letrasCasi(palabraCorrecta, palabra)
        # Obtenemos las letras incorrectas de una palabra incorrecta
        incorrecta = letrasIncorrecta(
            palabraCorrecta, palabra, casi, correctas)

        # Dibujamos y pintamos las letras que son correctas de una palabra correcta
        for posLetra in range(len(palabra)):
            if correctas[posLetra] == True:
                letra = defaultFontGrande.render(
                    palabra[posLetra], 1, COLOR_CORRECTA)
            # Dibujamos y pintamos las letras que son correctas de una palabra casi correcta
            elif casi[posLetra] == True:
                letra = defaultFontGrande.render(
                    palabra[posLetra], 1, COLOR_CASI)
            # Dibujamos y pintamos las letras que son incorrectas de una palabra incorrecta
            elif incorrecta[posLetra] == True:
                letra = defaultFontGrande.render(
                    palabra[posLetra], 1, COLOR_INCORRECTA)
            center = posGrilla[contador]
            posX = center[0] - letra.get_width() // 2
            posY = center[1] - letra.get_height() // 2
            screen.blit(letra, (posX, posY))
            contador = contador + 1
