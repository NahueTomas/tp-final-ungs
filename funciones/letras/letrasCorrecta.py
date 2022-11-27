# Devuelve las letras que son correctas
def letrasCorrecta(palabraCorrecta, palabra):
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    correctas = []

    for i in range(len(palabraMin)):  # correctas
        if palabraMin[i] == palabraCorrectaMin[i]:
            correctas.append(True)
        else:
            correctas.append(False)
    return correctas
