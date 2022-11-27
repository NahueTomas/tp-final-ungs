from config.configuracion import TXT_DIR


def lectura(archivo, salida, largo, tematica=''):
    with open(archivo.name, archivo.mode):
        for linea in archivo:  # Recorriendo linea por linea el archivo
            lista_linea = linea.split('-')
            palabra_linea = lista_linea[0]
            tematica_linea = lista_linea[1][:-1]

            # Verifico si las longitudes coinciden y está dentro de la temática
            if (tematica != ''):
                if (len(palabra_linea) == largo and tematica_linea == tematica):
                    salida.append(palabra_linea)  # Agrego a la lista
            else:
                if (len(palabra_linea) == largo):
                    salida.append(palabra_linea)  # Agrego a la lista
    return salida  # retorno lista
