import random
import string
def idAzarUsuario():
    from baseDeDatos import vistaIdUsuario
    ids = vistaIdUsuario()
    idsUsuarios = []
    for i in ids:
        idsUsuarios.append(i[0])

    caracteres = string.ascii_letters + string.digits
    while True:
        id_usuario = ""
        for i in range(12):
            id_usuario = id_usuario + random.choice(caracteres)
        if id_usuario in idsUsuarios:
            continue
        else: 
            return id_usuario