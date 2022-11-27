# Devuelve las letras que son incorrectas de una palabra
def letrasIncorrecta(palabraCorrecta, palabra, casi, correctas):
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    incorrectas = []
    for letra in palabraMin:  # incorrectas
        if not (letra in correctas or letra in casi):
            incorrectas.append(True)
    return incorrectas
