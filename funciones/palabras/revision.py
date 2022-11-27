# Devuelve un True si la palabra que ingreso el usuario es correcta
def revision(palabraCorrecta, palabra):
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()

    if palabraCorrectaMin == palabraMin:
        return True
    else:
        return False
