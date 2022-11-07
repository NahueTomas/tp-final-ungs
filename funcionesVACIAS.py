from principal import *
from configuracion import *
import random
import math
# from tkinter import *
# from tkinter import messagebox

def nuevaPalabra(lista):
    azar = random.randrange(len(lista)) # Se guarda una posicion aleatoriamente de una  lista
    return lista[azar] # retorno la lista con su posicion

def lectura(archivo, salida, largo):
    with open(archivo.name,archivo.mode):
        for linea in archivo: # Recorriendo linea por linea el archivo
            if len(linea) == largo+1: #Verifico si las longitudes coinciden
                salida.append(linea[:-1]) # Agrego a la lista
    return salida #retorno lista

def revision(palabraCorrecta, palabra): # Devuelve un True si la palabra que ingreso el usuario es correcta
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    if palabraCorrecta == palabra:
        return True
    else:
        return False

def letrasCorrecta(palabraCorrecta, palabra): # Devuelve las letras que son correctas
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    correctas = []

    for i in range(len(palabraMin)):  #correctas
        if palabraMin[i] == palabraCorrectaMin[i]:
            correctas.append(True)
        else:
            correctas.append(False)
    return correctas

def letrasCasi(palabraCorrecta, palabra): # Devuelve las letras que son correctas de una palabra casi
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    casi = []
    for x in range(len(palabraMin)):
        tieneLetra = False
        for letra in palabraCorrecta:
            if(palabraMin[x] == letra):
                casi.append(True)
                tieneLetra = True
        if(not(tieneLetra)):
            casi.append(False)
    return casi

def letrasIncorrecta(palabraCorrecta, palabra, casi, correctas): # Devuelve las letras que son incorrectas de una palabra
    palabraMin = palabra.lower()
    palabraCorrectaMin = palabraCorrecta.lower()
    incorrectas = []
    for letra in palabraMin: # incorrectas
        if not(letra in correctas or letra in casi):
            incorrectas.append(True)
    return incorrectas

# def DialogsInfo(dialogo): #DialogosTk
#     Tk().wm_withdraw()
#     if dialogo == "gano":
#         messagebox.showinfo("Felicidades","Usted a ganado!")
#     if dialogo == "errorLongitud":
#         messagebox.showwarning("Atencion","Debe ingresar una palabra que corresponda al largo!")
