import random
import string
def idAzarIncidencia(): 
    from baseDeDatos import vistaIdIncidencia
    ids = vistaIdIncidencia()
    idsIncidencia = []
    for i in ids:
        idsIncidencia.append(i[0])

    caracteres = string.ascii_letters + string.digits

    while True:
        idIncidencia = ""
        # Generar ID completo de 12 caracteres
        for i in range(12):
            idIncidencia += random.choice(caracteres)

        # Verificar si ya existe en la base de datos
        if idIncidencia in idsIncidencia:
            continue  # Repetir el bucle para generar uno nuevo
        else:
            return idIncidencia