import sqlite3
def baseDeDatos():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    conexion.execute("PRAGMA foreign_keys = ON;") 
    cursor = conexion.cursor()

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

def vistaCorreo():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("Select correo from Usuarios")
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def vistaCorreoYPassword():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("Select Correo,Contraseña from Usuarios")
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

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
