from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QWidget, QLabel, QPushButton # type: ignore
from PyQt5.QtGui import QFont #type: ignore
from baseDeDatos import insertarUsuario
class interfazUsuario(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        ############################################### Titulo de Inicio de Sesion
        self.txtIniciarSesion = QLabel("Iniciar Sesion", self)
        self.txtIniciarSesion.move(100, 80)
        self.txtIniciarSesion.setFont(QFont("Arial", 12, QFont.Bold))
        ###############################################
        self.txtCorreoIS = QLabel("Correo: ", self)
        self.txtCorreoIS.move(40, 118)
        self.txtCorreoIS.setFont(QFont("Arial", 12)) 
        ###############################################
        self.txtPassword = QLabel("Contraseña: ", self)
        self.txtPassword.move(40, 173)
        self.txtPassword.setFont(QFont("Arial", 12)) 
        ############################################### 
        self.CorreoIS = QLineEdit(self) 
        self.CorreoIS.move(40,135)
        self.CorreoIS.resize(220, 20)
        self.CorreoIS.setFont(QFont("Arial", 12))
        ###############################################
        self.password = QLineEdit(self)
        self.password.move(40,190)
        self.password.resize(220, 20)
        self.password.setFont(QFont("Arial", 12))
        self.password.setEchoMode(QLineEdit.Password)
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
        ##############################################
        self.registrarse.clicked.connect(self.registrar)
        ##############################################
    def registrar(self):
        ###############################################
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesion.hide()
        self.registrarse.hide()
        ###############################################
        self.setWindowTitle("Registrarse")
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        ############################################### 
        self.txtRegistrarse = QLabel("Registrarse", self)
        self.txtRegistrarse.move(100, 30)
        self.txtRegistrarse.setFont(QFont("Arial", 12, QFont.Bold))
        self.txtRegistrarse.show() 
        ###############################################
        self.txtCorreo = QLabel("Correo: ", self)
        self.txtCorreo.move(40, 60)
        self.txtCorreo.setFont(QFont("Arial", 12)) 
        self.txtCorreo.show()
        ###############################################
        self.correoRegistro = QLineEdit(self) 
        self.correoRegistro.move(40,80)
        self.correoRegistro.resize(220, 20)
        self.correoRegistro.setFont(QFont("Arial", 12))
        self.correoRegistro.show()
        ###############################################
        self.txtPasswordRegistro = QLabel("Contraseña: ", self)
        self.txtPasswordRegistro.move(40, 120)
        self.txtPasswordRegistro.setFont(QFont("Arial", 12)) 
        self.txtPasswordRegistro.show()
        ###############################################
        self.passwordRegistro = QLineEdit(self)
        self.passwordRegistro.move(40,140)
        self.passwordRegistro.resize(220, 20)
        self.passwordRegistro.setFont(QFont("Arial", 12))
        self.passwordRegistro.setEchoMode(QLineEdit.Password)
        self.passwordRegistro.show()
        ###############################################
        self.registrarse2 = QPushButton("Registrarse", self)
        self.registrarse2.resize(100,30)
        self.registrarse2.setFont(QFont("Arial", 12))
        self.registrarse2.move(100,255)
        self.registrarse2.show()
        ##############################################
        self.txtConfirmarPasswordRegistro = QLabel("Repite la Contraseña: ", self)
        self.txtConfirmarPasswordRegistro.move(40, 173)
        self.txtConfirmarPasswordRegistro.setFont(QFont("Arial", 12)) 
        self.txtConfirmarPasswordRegistro.show()
        ##############################################
        self.confirmarPasswordRegistro = QLineEdit(self) 
        self.confirmarPasswordRegistro.move(40,193)
        self.confirmarPasswordRegistro.resize(220, 20)
        self.confirmarPasswordRegistro.setFont(QFont("Arial", 12))
        self.confirmarPasswordRegistro.setEchoMode(QLineEdit.Password)
        self.confirmarPasswordRegistro.show()
        self.registrarse2.clicked.connect(self.verificarCorreo)
        ##############################################
    def crearUsuario(self):
        correo = self.correoRegistro.text()
        password = self.passwordRegistro.text()
        insertarUsuario(correo, password)
        
    def validarYCrearUsuario(self):
        passwordVerificar = self.passwordRegistro.text()
        passwordConfirmar = self.confirmarPasswordRegistro.text()
        if passwordVerificar.strip() != "" and passwordVerificar == passwordConfirmar:
            self.crearUsuario()
        else:
            mensajeErrorPassword = QMessageBox()
            mensajeErrorPassword.setIcon(QMessageBox.Warning)
            mensajeErrorPassword.setWindowTitle("Error")
            mensajeErrorPassword.setText("Las contraseñas no coinciden")
            mensajeErrorPassword.exec_()
    def verificarCorreo(self):
        from baseDeDatos import vistaCorreo
        correos = vistaCorreo()
        pkCorreos = []
        for i in correos:
            pkCorreos.append(i[0])
        if self.correoRegistro.text() in pkCorreos:
            mensajeErrorCorreo = QMessageBox()
            mensajeErrorCorreo.setIcon(QMessageBox.Warning)
            mensajeErrorCorreo.setWindowTitle("Error")
            mensajeErrorCorreo.setText("El correo ya esta registrado")
            mensajeErrorCorreo.exec_()
        else:
            self.validarYCrearUsuario()