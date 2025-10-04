from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton # type: ignore
from PyQt5.QtGui import QFont #type: ignore

class interfazUsuario(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        ############################################### Titulo de Inicio de Sesion
        self.txtIniciarSesion = QLabel("Iniciar Sesion", self)
        self.txtIniciarSesion.move(100, 80)
        self.txtIniciarSesion.setFont(QFont("Arial", 12)) 
        ###############################################
        self.txtusuario = QLabel("Usuario: ", self)
        self.txtusuario.move(40, 118)
        self.txtusuario.setFont(QFont("Arial", 12)) 
        ###############################################
        self.txtPassword = QLabel("Contraseña: ", self)
        self.txtPassword.move(40, 173)
        self.txtPassword.setFont(QFont("Arial", 12)) 
        ############################################### 
        self.usuario = QLineEdit(self) 
        self.usuario.move(40,135)
        self.usuario.resize(220, 20)
        self.usuario.setFont(QFont("Arial", 12))
        ###############################################
        self.password = QLineEdit(self)
        self.password.move(40,190)
        self.password.resize(220, 20)
        self.password.setFont(QFont("Arial", 12))
        ###############################################
        self.iniciarSesion = QPushButton("Iniciar Sesión", self)
        self.iniciarSesion.resize(120,30)
        self.iniciarSesion.setFont(QFont("Arial", 12))
        self.iniciarSesion.move(140,215)
        ###############################################
        self.registrarse = QPushButton("Registrar", self)
        self.registrarse.resize(90,30)
        self.registrarse.setFont(QFont("Arial", 12))
        self.registrarse.move(40,215)
