# Verifico la existencia del usuario para el inicio de sesion
def loginUsuario(usuario, contraseña):
    archivo = open("usuario.txt", "r")
    usuPassword = usuario + " " + contraseña + "\n"
    usuarioValido = False
    with open(archivo.name, archivo.mode):
        for linea in archivo:  # Recorriendo linea por linea el archivo
            if linea == usuPassword:
                print("Existo")
                usuarioValido = True

    archivo.close()
    return usuarioValido  # Devuelvo True si el usuario ya esta registrado
