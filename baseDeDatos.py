import sqlite3


#---------------------Metodo de la base de datos---------------------# 
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
        Descripcion VARCHAR(200),
        Gravedad VARCHAR(10),
        Fecha DATETIME NOT NULL,
        Estado VARCHAR(7),
        CONSTRAINT PK_IDINCIDENCIAS PRIMARY KEY (ID_Incidencia),
        CONSTRAINT CHK_GRAVEDAD CHECK (Gravedad IN ('Baja', 'Media', 'Alta', 'Grave', 'Muy Grave')),
        CONSTRAINT CHK_ESTADO CHECK (Estado IN ('ABIERTO', 'CERRADO')),
        CONSTRAINT FK_INCIDENCIA FOREIGN KEY (Correo) REFERENCES Usuarios (Correo) ON UPDATE CASCADE
    )
    """)
    conexion.commit()
    conexion.close()

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
    consulta = (
        "INSERT INTO USUARIOS (correo, Contraseña) VALUES ('"
        + correo + "', '"
        + password + "')"
    )
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#

#---------------------Añadir nuevas incidencias a la base de datos---------------------# 
def insertarIncidencia(iD_Incidencias, titulo, descripcion, gravedad, fecha):
    correo = "1" #Necesitamos una manera de conseguir el correo del usuario que está añadiendo la incidencia
    print("hola")
    consulta = (
    "INSERT INTO INCIDENCIAS (Correo, ID_Incidencias, Titulo, Descripcion, Gravedad, Fecha, Estado) VALUES ('"
    + correo + "', '"
    + iD_Incidencias + "', '"
    + titulo + "', '"
    + descripcion + "', '"
    + gravedad + "', '"
    + fecha + "', 'ABIERTO')"
    )
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#

#---------------------Borrar incidencias a la base de datos---------------------# 
def insertarIncidencia(iD_Incidencias):
    #Necesitamos sacar el id_incidencia de la incidencia seleccionada para eliminar
    consulta = (
    "DELETE FROM INCIDENCIAS WHERE ID_Incidencia LIKE '" 
    + iD_Incidencias
    + "';"
    )
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
#-----------------------------FIN------------------------------#
