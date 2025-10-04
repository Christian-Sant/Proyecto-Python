import sqlite3

def baseDeDatos():
    conexion = sqlite3.connect("IncidenciasInformaticas.db") 
    conexion.execute("PRAGMA foreign_keys = ON;") 
    cursor = conexion.cursor()

    # Crear una tabla de ejemplo
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Incidencias (
        ID_Incidencia VARCHAR(12),
        Titulo VARCHAR(40),
        Descripcion VARCHAR(200),
        Gravedad VARCHAR(10),
        Fecha DATETIME NOT NULL,
        Estado VARCHAR(7),
        CONSTRAINT PK_IDINCIDENCIAS PRIMARY KEY (ID_Incidencia),
        CONSTRAINT CHK_GRAVEDAD CHECK (Gravedad IN ('Baja', 'Media', 'Alta', 'Grave', 'Muy Grave')),
        CONSTRAINT CHK_ESTADO CHECK (Estado IN ('ABIERTO', 'CERRADO'))
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        ID_Usuario VARCHAR(12),
        Usuario VARCHAR(20),
        Correo VARCHAR(100),
        Contraseña VARCHAR(100),
        ID_Incidencia VARCHAR(12),
        CONSTRAINT PK_IDUSUARIO PRIMARY KEY (ID_Usuario),
        CONSTRAINT FK_INCIDENCIA FOREIGN KEY (ID_Incidencia)
        REFERENCES Incidencias (ID_Incidencia)
            ON UPDATE CASCADE
    )
    """)
    conexion.commit()
    conexion.close()
