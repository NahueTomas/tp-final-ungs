import loginUsuario


# Creacion de Usuario con Archivos (sin objetos)
def creacionUsuario(usuario, contraseña):
    archivo = open("usuario.txt", "a")
    # Utilizo la funcion loginUsuario para saber si el usuario ya existe
    validarUsuario = loginUsuario(usuario, contraseña)
    if (not (validarUsuario)):  # Si es False creo el registro del nuevo usuario
        archivo.write(usuario + " " + contraseña + "\n")
        print("no existo")
    else:
        print("ya existo")
    archivo.close()
    return validarUsuario  # Si es false se creo el usuario caso contrario no hago nada
