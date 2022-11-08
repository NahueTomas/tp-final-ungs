import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,palabraCorrecta):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    # Dibuja la grilla y devuelve una lista con las posiciones de cada cuadrado
    dibujarGrilla(screen)
    posGrilla = dibujarGrilla(screen)
    contador = 0

    # muestra las palabras anteriores, las que se fueron arriesgando
    for palabra in listaDePalabrasUsuario:
        correctas = letrasCorrecta(palabraCorrecta, palabra) # Obtenemos las letras correctas de la palabra
        casi = letrasCasi(palabraCorrecta, palabra) # Obtenemos las letras correctas de una palabra casi correcta
        incorrecta = letrasIncorrecta(palabraCorrecta, palabra, casi, correctas) # Obtenemos las letras incorrectas de una palabra incorrecta

        for posLetra in range(len(palabra)): # Dibujamos y pintamos las letras que son correctas de una palabra correcta
            if correctas[posLetra] == True:
                letra = defaultFontGrande.render(palabra[posLetra], 1, COLOR_CORRECTA)
            elif casi[posLetra] == True: # Dibujamos y pintamos las letras que son correctas de una palabra casi correcta
                letra = defaultFontGrande.render(palabra[posLetra], 1, COLOR_CASI)
            elif incorrecta[posLetra] == True: # Dibujamos y pintamos las letras que son incorrectas de una palabra incorrecta
                letra = defaultFontGrande.render(palabra[posLetra], 1, COLOR_INCORRECTA)
            center = posGrilla[contador]
            posX = center[0] - letra.get_width() // 2
            posY = center[1] - letra.get_height() // 2
            screen.blit(letra, (posX, posY))
            contador = contador + 1

    #muestra el abcdario, falta ponerle color a las letras
    abcdario = ["qwertyuiop", "asdfghjklm", "zxcvbnm"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            color = COLOR_LETRAS
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA

def dibujarGrilla(screen):
    screen_rect = screen.get_rect()
    center = screen_rect.center

    posY = center[0] - 125
    posX = center[1] - 220

    posGrilla =[]
    cuadradoTam = 50

    # 0 - 50 - 100 - 150 - 200
    for x in range(0, 201, cuadradoTam):
        for y in range(0, 201, cuadradoTam):
            rect = pygame.Rect(y + posY, x + posX, cuadradoTam, cuadradoTam)
            pygame.draw.rect(screen, COLOR_BLANCO, rect, 1)
            posGrilla.append(rect.center)
    return posGrilla
