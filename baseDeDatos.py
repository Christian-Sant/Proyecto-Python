import sqlite3
from utilidades import idAzarUsuario
def baseDeDatos():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    conexion.execute("PRAGMA foreign_keys = ON;") 
    cursor = conexion.cursor()

    cursor.execute("""
        ID_Usuario VARCHAR(12),
        Usuario VARCHAR(20),
        Correo VARCHAR(100),
        Contraseña VARCHAR(100),
        CONSTRAINT PK_IDUSUARIO PRIMARY KEY (ID_Usuario)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Incidencias (
        ID_Usuario VARCHAR(12),
        ID_Incidencia VARCHAR(12),
        Titulo VARCHAR(40),
        Descripcion VARCHAR(200),
        Gravedad VARCHAR(10),
        Fecha DATETIME NOT NULL,
        Estado VARCHAR(7),
        CONSTRAINT PK_IDINCIDENCIAS PRIMARY KEY (ID_Incidencia),
        CONSTRAINT CHK_GRAVEDAD CHECK (Gravedad IN ('Baja', 'Media', 'Alta', 'Grave', 'Muy Grave')),
        CONSTRAINT CHK_ESTADO CHECK (Estado IN ('ABIERTO', 'CERRADO')),
        CONSTRAINT FK_INCIDENCIA FOREIGN KEY (ID_Usuario) REFERENCES Usuarios (ID_Usuario) ON UPDATE CASCADE
    )
    """)
    conexion.commit()
    conexion.close()

def vistaIdUsuario():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    consulta = ("Select ID_Usuario from Usuarios")
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def insertarUsuario(correo, usuario, password):
    
    consulta = (
        "INSERT INTO USUARIOS (id_usuario,usuario, correo, Contraseña) VALUES ('"
        + idAzarUsuario() + "', '"
        + usuario + "', '"
        + correo + "', '"
        + password + "')"
    )
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
