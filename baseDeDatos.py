import sqlite3
from datetime import datetime
#---------------------Metodo para la creacion de la base de datos---------------------# 
def baseDeDatos():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    conexion.execute("PRAGMA foreign_keys = ON;") 
    cursor = conexion.cursor()

    #---------------------Creacion de la base de datos---------------------# 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        Correo VARCHAR(100),
        Contraseña VARCHAR(100) NOT NULL,
        CONSTRAINT PK_Correo PRIMARY KEY (Correo)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Incidencias (
        Correo VARCHAR(100),
        ID_Incidencia VARCHAR(12),
        Titulo VARCHAR(40),
        Descripcion VARCHAR(400),
        Gravedad VARCHAR(10),
        Fecha DATETIME NOT NULL,
        Estado VARCHAR(7),
        Categoria VARCHAR(8),
        CONSTRAINT PK_IDINCIDENCIAS PRIMARY KEY (ID_Incidencia),
        CONSTRAINT CHK_GRAVEDAD CHECK (Gravedad IN ('Baja', 'Media', 'Alta', 'Grave', 'Muy Grave')),
        CONSTRAINT CHK_ESTADO CHECK (Estado IN ('ABIERTO', 'CERRADO')),
        CONSTRAINT CHK_CATEGORIA CHECK (Categoria IN ('HARDWARE', 'SOFTWARE')),
        CONSTRAINT FK_INCIDENCIA FOREIGN KEY (Correo) REFERENCES Usuarios (Correo) ON UPDATE CASCADE
    )
    """)
    conexion.commit()
    conexion.close()
    #-----------------------------FIN------------------------------#
#-----------------------------FIN------------------------------#



#---------------------Metodo para ver el correo de la tabla usuarios---------------------# 
def vistaCorreo():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("Select correo from Usuarios")
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
#-----------------------------FIN------------------------------#



#---------------------Metodo para ver los IDs de las Incidencias---------------------# 
def vistaIdIncidencia():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("Select ID_Incidencia from Incidencias")
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
#-----------------------------FIN------------------------------#



#---------------------Metodo para hacer la tabla para la visualizar los datos---------------------# 
def vistasIncidencias(correoIniciado):
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("SELECT ID_Incidencia, Titulo, Descripcion, Gravedad, Fecha, Estado, Categoria FROM Incidencias WHERE Correo = ?")
    cursor.execute(consulta, (correoIniciado,))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
#-----------------------------FIN------------------------------#



# -------------------Metodo para filtrar la tabla------------------- #
def obtener_incidencias(correo, categorias, estados, gravedades, fecha_inicio=None, fecha_fin=None):
    consulta = f"SELECT ID_Incidencia, Titulo, Descripcion, Gravedad, Fecha, Estado, Categoria FROM Incidencias WHERE Correo='{correo}'"

    if categorias:
        consulta = consulta + " AND Categoria IN ('" + "','".join(categorias) + "')"
    if estados:
        consulta = consulta + " AND Estado IN ('" + "','".join(estados) + "')"
    if gravedades:
        consulta = consulta + " AND Gravedad IN ('" + "','".join(gravedades) + "')"
    if fecha_inicio and fecha_fin:
        consulta = consulta +  f" AND Fecha BETWEEN '{fecha_inicio}' AND '{fecha_fin}'"

    conexion = sqlite3.connect("IncidenciasInformaticas.db")
    cursor = conexion.cursor()
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
#-----------------------------FIN------------------------------#



#---------------------Metodo para ver el correo y contraseña de la tabla usuarios---------------------# 
def vistaCorreoYPassword():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("Select Correo,Contraseña from Usuarios")
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
#-----------------------------FIN------------------------------#



#---------------------Añadir nuevos usuarios a la base de datos---------------------# 
def insertarUsuario(correo, password):
    consulta = "INSERT INTO USUARIOS (correo, Contraseña) VALUES (?, ?)"
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta, (correo, password))
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#



#---------------------Añadir nuevas incidencias a la base de datos---------------------# 
def insertarIncidencia(correo, iD_Incidencias, titulo, descripcion, gravedad, fecha, categoria):
    consulta = (
        "INSERT INTO INCIDENCIAS "
        "(Correo, ID_Incidencia, Titulo, Descripcion, Gravedad, Fecha, Categoria, Estado) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, 'ABIERTO')"
    )
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta, (correo, iD_Incidencias, titulo, descripcion, gravedad, fecha, categoria))
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#



#---------------------Hacer un update a la incidencia seleccionada---------------------# 
def actualizarIncidencia(id_incidencia, titulo, descripcion, gravedad, fecha, categoria):

    consulta = (
        "UPDATE INCIDENCIAS SET "
        "Titulo = ?, "
        "Descripcion = ?, "
        "Gravedad = ?, "
        "Fecha = ?, "
        "Categoria = ? "
        "WHERE ID_Incidencia = ?"
    )

    conexion = sqlite3.connect("IncidenciasInformaticas.db")
    cursor = conexion.cursor()
    cursor.execute(consulta, (titulo, descripcion, gravedad, fecha, categoria, id_incidencia))
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#



#---------------------Borrar una incidencia en la base de datos---------------------# 
def eliminarIncidencia(id_incidencias):
    consulta = "DELETE FROM INCIDENCIAS WHERE ID_Incidencia LIKE ?"
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta, (id_incidencias,))
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#



#---------------------Cambiar a Abierto el estado de una incidencia en la base de datos---------------------#
def abrirIncidencia(id_incidencia):

    consulta = "UPDATE INCIDENCIAS SET Estado = 'ABIERTO' WHERE ID_Incidencia = ?"
    conexion = sqlite3.connect("IncidenciasInformaticas.db")
    cursor = conexion.cursor()
    cursor.execute(consulta, (id_incidencia,))
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#



#---------------------Cambiar a Cerrado el estado de una incidencia en la base de datos---------------------#
def cerrarIncidencia(id_incidencia):

    consulta = "UPDATE INCIDENCIAS SET Estado = 'CERRADO' WHERE ID_Incidencia = ?"

    conexion = sqlite3.connect("IncidenciasInformaticas.db")
    cursor = conexion.cursor()
    cursor.execute(consulta, (id_incidencia,))
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#



#---------------------Metodo para poder hacer el grafico---------------------#
def obtener_grafico(correo,nombre_db):

    conexion = sqlite3.connect(nombre_db)
    cursor = conexion.cursor()

    cursor.execute("SELECT Categoria, COUNT(*) FROM Incidencias WHERE Correo = ? GROUP BY Categoria", (correo,)) #Se agrupa por categoria
    por_categoria = cursor.fetchall()


    cursor.execute("SELECT Estado, COUNT(*) FROM Incidencias WHERE Correo = ? GROUP BY Estado", (correo,)) #Se agrupa por estado
    por_estado = cursor.fetchall()


    tiempos_resolucion = []
    tiene_fecha_cierre = _col_exists(cursor, "Incidencias", "FechaCierre") #Tiempo de resulucion

    if tiene_fecha_cierre:
        cursor.execute("""
            SELECT Fecha, FechaCierre 
            FROM Incidencias 
            WHERE Correo = ? 
            AND FechaCierre IS NOT NULL
        """, (correo,))
        datos_fechas = cursor.fetchall()

        for fecha_inicio, fecha_cierre in datos_fechas:
            try:
                f_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                f_cierre = datetime.strptime(fecha_cierre, "%Y-%m-%d")
                dias = (f_cierre - f_inicio).days
                tiempos_resolucion.append(dias)
            except Exception:
                continue

    conexion.close()

    return por_categoria, por_estado, tiempos_resolucion
#-----------------------------FIN------------------------------#



#---------------------Para saber si una tabla existe---------------------#
def _col_exists(cursor, tabla, columna):
    cursor.execute(f"PRAGMA table_info({tabla})")
    columnas = [col[1] for col in cursor.fetchall()]
    return columna in columnas
#-----------------------------FIN------------------------------#
