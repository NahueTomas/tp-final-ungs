# Cartel que muestra devuelve los segundos restantes
def contSegundos(segundos, default_font, color_ultimos, color_normal):
    if (int(segundos) < 15):
        ren = default_font.render(
            "Tiempo: " + str(int(segundos)), 1, color_ultimos)
    else:
        ren = default_font.render(
            "Tiempo: " + str(int(segundos)), 1, color_normal)
    return ren
