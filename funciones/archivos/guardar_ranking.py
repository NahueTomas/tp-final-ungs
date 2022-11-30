def guardar_ranking(nombre, puntos):
    linea = str(nombre) + "-" + str(puntos) + '\n'

    with open('assets/txt/ranking.txt') as f:
        text = f.read()

    with open('assets/txt/ranking.txt', 'w') as f:
        f.write(text + linea)
