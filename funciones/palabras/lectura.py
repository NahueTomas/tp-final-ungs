from config.configuracion import TXT_DIR


def lectura(archivo, salida, largo):
    with open(archivo.name, archivo.mode):
        for linea in archivo:  # Recorriendo linea por linea el archivo
            if len(linea) == largo+1:  # Verifico si las longitudes coinciden
                salida.append(linea[:-1])  # Agrego a la lista
    return salida  # retorno lista
