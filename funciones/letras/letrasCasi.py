# Devuelve las letras que son correctas de una palabra casi
def letrasCasi(palabraCorrecta, palabra):
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    casi = []
    for x in range(len(palabraMin)):
        tieneLetra = False
        for letra in palabraCorrectaMin:
            if (palabraMin[x] == letra):
                casi.append(True)
                tieneLetra = True
        if (not (tieneLetra)):
            casi.append(False)
    return casi
