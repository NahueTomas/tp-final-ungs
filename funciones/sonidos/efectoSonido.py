# Devuelve un sonido dependiendo del índice que le pasemos
def efectoSonido(num_sonido):
    listaSonidos = ['assets/audio/intro.wav', 'assets/audio/error.wav', 'assets/audio/ganar.wav',
                    'assets/audio/mTensa1.wav', 'assets/audio/mTensa2.wav', 'assets/audio/menu.wav']
    return listaSonidos[num_sonido]
