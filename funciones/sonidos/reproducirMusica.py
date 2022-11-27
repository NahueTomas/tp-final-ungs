from pygame import mixer

from funciones.sonidos.efectoSonido import efectoSonido


# Reproduccion de musica por el segundo
def reproducirMusica(segundos):
    musica = None
    if int(segundos) < 15:  # 135 es 15*9
        musica = efectoSonido(3)

    if not musica is None:
        mixer.music.load(musica)
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)
