import random


def nuevaPalabra(lista):
    # Se guarda una posicion aleatoriamente de una  lista
    azar = random.randrange(len(lista))
    return lista[azar]  # retorno la lista con su posicion
