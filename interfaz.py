from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QWidget, QLabel, QPushButton, QTextEdit, QComboBox, QDateEdit # type: ignore
from PyQt5.QtGui import QFont #type: ignore
from PyQt5.QtCore import QDate #type: ignore
from baseDeDatos import insertarUsuario, insertarIncidencia
class interfazUsuario(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        #---------------------Label Iniciar Sesion---------------------#
        self.txtIniciarSesion = QLabel("Iniciar Sesion", self)
        self.txtIniciarSesion.move(100, 80)
        self.txtIniciarSesion.setFont(QFont("Arial", 12, QFont.Bold))
        #-----------------------------FIN------------------------------#



        #---------------------Llamada Iniciar Sesion---------------------#
        self.iniciarSesion()
        #-----------------------------FIN------------------------------



     #---------------------Metodo del apartado Iniciar Sesion---------------------#
    def iniciarSesion(self):
        #---------------------Label Correo en el Apartado Iniciar Sesion---------------------#
        self.txtCorreoIS = QLabel("Correo: ", self)
        self.txtCorreoIS.move(40, 118)
        self.txtCorreoIS.setFont(QFont("Arial", 12)) 
        #-----------------------------FIN------------------------------#


        #---------------------Label Contraseña en el Apartado Iniciar Sesion---------------------#
        self.txtPassword = QLabel("Contraseña: ", self)
        self.txtPassword.move(40, 173)
        self.txtPassword.setFont(QFont("Arial", 12)) 
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir el Correo en el Apartado Iniciar Sesion---------------------#
        self.CorreoIS = QLineEdit(self) 
        self.CorreoIS.move(40,135)
        self.CorreoIS.resize(220, 20)
        self.CorreoIS.setFont(QFont("Arial", 12))
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir la contraseña en el Apartado Iniciar Sesion---------------------#
        self.password = QLineEdit(self)
        self.password.move(40,190)
        self.password.resize(220, 20)
        self.password.setFont(QFont("Arial", 12))
        self.password.setEchoMode(QLineEdit.Password)
        #-----------------------------FIN------------------------------#


        #---------------------El boton de Iniciar Sesion en el Apartado Iniciar Sesion---------------------#
        self.iniciarSesion = QPushButton("Iniciar Sesión", self)
        self.iniciarSesion.resize(120,30)
        self.iniciarSesion.setFont(QFont("Arial", 12))
        self.iniciarSesion.move(140,215)
        self.iniciarSesion.clicked.connect(self.verificarCorreoYPassword) # Los click intentar mantenerlos siempre al lado porque si no, da errores
        #-----------------------------FIN------------------------------#


        #---------------------El boton de Registrar en el Apartado Iniciar Sesion---------------------#
        self.registrarse = QPushButton("Registrar", self)
        self.registrarse.resize(90,30)
        self.registrarse.setFont(QFont("Arial", 12))
        self.registrarse.move(40,215)
        self.registrarse.clicked.connect(self.registrar) #Se llama al metodo registrar
        #-----------------------------FIN------------------------------#

    #-----------------------------FIN------------------------------#



    #---------------------Metodo del apartado Registrar---------------------#
    def registrar(self):

        #---------------------Se oculta toda la interfaz del apartado Iniciar Sesion---------------------#
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesion.hide()
        self.registrarse.hide()
        #-----------------------------FIN------------------------------#


        #---------------------Cambiamos la interfaz con la del apartado Registrar---------------------#
        self.setWindowTitle("Registrarse")
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        #-----------------------------FIN------------------------------#


        #---------------------Label Registrase en el Apartado Registrar---------------------#
        self.txtRegistrarse = QLabel("Registrarse", self)
        self.txtRegistrarse.move(100, 30)
        self.txtRegistrarse.setFont(QFont("Arial", 12, QFont.Bold))
        self.txtRegistrarse.show() 
        #-----------------------------FIN------------------------------#


        #---------------------Label Correo en el Apartado Registrar---------------------#
        self.txtCorreo = QLabel("Correo: ", self)
        self.txtCorreo.move(40, 60)
        self.txtCorreo.setFont(QFont("Arial", 12)) 
        self.txtCorreo.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir el Correo en el Apartado Registrar---------------------#
        self.correoRegistro = QLineEdit(self) 
        self.correoRegistro.move(40,80)
        self.correoRegistro.resize(220, 20)
        self.correoRegistro.setFont(QFont("Arial", 12))
        self.correoRegistro.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Contraseña en el Apartado Registrar---------------------#
        self.txtPasswordRegistro = QLabel("Contraseña: ", self)
        self.txtPasswordRegistro.move(40, 120)
        self.txtPasswordRegistro.setFont(QFont("Arial", 12)) 
        self.txtPasswordRegistro.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir la Contraseña en el Apartado Registrar---------------------#
        self.passwordRegistro = QLineEdit(self)
        self.passwordRegistro.move(40,140)
        self.passwordRegistro.resize(220, 20)
        self.passwordRegistro.setFont(QFont("Arial", 12))
        self.passwordRegistro.setEchoMode(QLineEdit.Password)
        self.passwordRegistro.show()
        #-----------------------------FIN------------------------------#

        
        #---------------------Label Repetir Contraseña en el Apartado Registrar---------------------#
        self.txtConfirmarPasswordRegistro = QLabel("Repite la Contraseña: ", self)
        self.txtConfirmarPasswordRegistro.move(40, 173)
        self.txtConfirmarPasswordRegistro.setFont(QFont("Arial", 12)) 
        self.txtConfirmarPasswordRegistro.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir la Contraseña Repetida en el Apartado Registrar---------------------#
        self.confirmarPasswordRegistro = QLineEdit(self) 
        self.confirmarPasswordRegistro.move(40,193)
        self.confirmarPasswordRegistro.resize(220, 20)
        self.confirmarPasswordRegistro.setFont(QFont("Arial", 12))
        self.confirmarPasswordRegistro.setEchoMode(QLineEdit.Password)
        self.confirmarPasswordRegistro.show()
        #-----------------------------FIN------------------------------#


        #---------------------El boton de Registrarse en el Apartado Registrar---------------------#
        self.registrarse2 = QPushButton("Registrarse", self)
        self.registrarse2.resize(100,30)
        self.registrarse2.setFont(QFont("Arial", 12))
        self.registrarse2.move(100,255)
        self.registrarse2.show()
        self.registrarse2.clicked.connect(self.verificarCorreo)# Llamamos el metodo verificarCorreo
    #-----------------------------FIN------------------------------#



    #---------------------Metodo para la creacion de Usuario, se usara en el metodo validarYCrearUsuario---------------------#
    def crearUsuario(self):
        correo = self.correoRegistro.text().strip()
        password = self.passwordRegistro.text().strip()
        insertarUsuario(correo, password)

        #---------------------Se oculta toda la interfaz del apartado Registro---------------------#
        self.txtRegistrarse.hide()
        self.txtCorreo.hide()
        self.correoRegistro.hide()
        self.txtPasswordRegistro.hide()
        self.passwordRegistro.hide()
        self.registrarse2.hide()
        self.txtConfirmarPasswordRegistro.hide()
        self.confirmarPasswordRegistro.hide()
        #-----------------------------FIN------------------------------#


        #---------------------Se muestra toda la interfaz del apartado Iniciar Sesion---------------------#
        self.txtIniciarSesion.show()
        self.CorreoIS.show()
        self.password.show()
        self.txtCorreoIS.show()
        self.txtPassword.show()
        self.iniciarSesion.show()
        self.registrarse.show()
        self.CorreoIS.clear()
        self.password.clear()
        #-----------------------------FIN------------------------------#

    #-----------------------------FIN------------------------------#



    #---------------------Metodo para la Creacion y Validacion del Usuario en el apartado Registrar---------------------#    
    def validarYCrearUsuario(self):
        passwordVerificar = self.passwordRegistro.text().strip()
        passwordConfirmar = self.confirmarPasswordRegistro.text().strip()

        #---------------------Validamos que la contraseña y la contraseña repetida sea igual y se asegura de que no este vacio---------------------#   
        if passwordVerificar.strip() != "" and passwordVerificar == passwordConfirmar:
            self.crearUsuario()#Llamamos el metodo crearUsuario
        #-----------------------------FIN------------------------------#


        #---------------------Damos un mensaje de error si la contraseña esta vacia---------------------# 
        elif passwordVerificar.strip() == "":
            mensajeErrorPassword = QMessageBox()
            mensajeErrorPassword.setIcon(QMessageBox.Warning)
            mensajeErrorPassword.setWindowTitle("Error")
            mensajeErrorPassword.setText("El apartado contraseña esta vacia")
            mensajeErrorPassword.exec_()
        #-----------------------------FIN------------------------------#


        #---------------------Damos un mensaje de error si ve que en el apartado repite contraseña esta vacia---------------------# 
        elif passwordConfirmar.strip() == "":
            mensajeErrorPassword = QMessageBox()
            mensajeErrorPassword.setIcon(QMessageBox.Warning)
            mensajeErrorPassword.setWindowTitle("Error")
            mensajeErrorPassword.setText("Repita la contraseña")
            mensajeErrorPassword.exec_()
        #-----------------------------FIN------------------------------#


        #---------------------Damos un mensaje de error si las contraseñas no coinciden---------------------# 
        else:
            mensajeErrorPassword = QMessageBox()
            mensajeErrorPassword.setIcon(QMessageBox.Warning)
            mensajeErrorPassword.setWindowTitle("Error")
            mensajeErrorPassword.setText("Las contraseñas no coinciden")
            mensajeErrorPassword.exec_()
        #-----------------------------FIN------------------------------#


    #-----------------------------FIN------------------------------#



    #---------------------Metodo para Verificar si el Correo ya esta registrado en el apartado Registrar---------------------#
    def verificarCorreo(self):
        from baseDeDatos import vistaCorreo
        correos = vistaCorreo()#Llamamos al metodo vistaCorreo
        pkCorreos = []
        for i in correos:
            pkCorreos.append(i[0])
        if self.correoRegistro.text().strip() in pkCorreos:
            mensajeErrorCorreo = QMessageBox()
            mensajeErrorCorreo.setIcon(QMessageBox.Warning)
            mensajeErrorCorreo.setWindowTitle("Error")
            mensajeErrorCorreo.setText("El correo ya esta registrado")
            mensajeErrorCorreo.exec_()
        elif self.correoRegistro.text().strip() == "":
            mensajeErrorCorreo2 = QMessageBox()
            mensajeErrorCorreo2.setIcon(QMessageBox.Warning)
            mensajeErrorCorreo2.setWindowTitle("Error")
            mensajeErrorCorreo2.setText("El apartado correo esta vacia")
            mensajeErrorCorreo2.exec_()
        else:
            self.validarYCrearUsuario()#Llamamos el metodo validarYCrearUsuario

    #-----------------------------FIN------------------------------#



    #---------------------Metodo para Verificar si existe la cuenta y que pueda entrar en la App, esto es para el apartado Iniciar Sesion---------------------#
    def verificarCorreoYPassword(self):
        from baseDeDatos import vistaCorreoYPassword
        correosPassword = dict(vistaCorreoYPassword())#Se hace un diccionario, en el cual el correo es la clave mientras que la contraseña es el valor del clave.
        correo = self.CorreoIS.text().strip()
        password = self.password.text().strip()
        if correo in correosPassword:
            if correosPassword[correo] == password:
                #llamar un metodo(def) de Vicente, la interfaz
                self.incidencias()
                print("todo bien")
            else:
                mensajeErrorPassword = QMessageBox()
                mensajeErrorPassword.setIcon(QMessageBox.Warning)
                mensajeErrorPassword.setWindowTitle("Error")
                mensajeErrorPassword.setText("Contraseña Incorrecta")
                mensajeErrorPassword.exec_()
        else:
            mensajeErrorCorreo = QMessageBox()
            mensajeErrorCorreo.setIcon(QMessageBox.Warning)
            mensajeErrorCorreo.setWindowTitle("Error")
            mensajeErrorCorreo.setText("Correo no registrado")
            mensajeErrorCorreo.exec_()

    #-----------------------------FIN------------------------------#

    def incidencias(self):
        self.setWindowTitle("Incidencias")
        self.setGeometry(200,200,500,500)
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesion.hide()
        self.registrarse.hide()
 #-----------------------------FIN------------------------------#


 #---------------------Label Titulo en el Apartado Incidencias---------------------#
        self.txtTitulo = QLabel("Titulo: ", self)
        self.txtTitulo.move(50, 140)
        self.txtTitulo.setFont(QFont("Arial", 12)) 
        self.txtTitulo.show()
#-----------------------------FIN------------------------------#

#---------------------Apartado para escribir el Titulo en el Apartado Incidencias---------------------#
        self.escribirTitulo = QLineEdit(self) 
        self.escribirTitulo.move(150,140)
        self.escribirTitulo.resize(220, 20)
        self.escribirTitulo.setFont(QFont("Arial", 12))
        self.escribirTitulo.show()
        #-----------------------------FIN------------------------------#

#---------------------Label Descripcion en el Apartado Incidencias---------------------#
        self.txtDescripcion = QLabel("Descripción: ", self)
        self.txtDescripcion.move(50, 180)
        self.txtDescripcion.setFont(QFont("Arial", 12)) 
        self.txtDescripcion.show()
        #-----------------------------FIN------------------------------#

        #---------------------Apartado para escribir la Descripcion en el Apartado Incidencias---------------------#
        self.escribirDescripcion = QTextEdit(self) 
        self.escribirDescripcion.move(150,180)
        self.escribirDescripcion.resize(220, 80)
        self.escribirDescripcion.setFont(QFont("Arial", 12))
        self.escribirDescripcion.show()
        #-----------------------------FIN------------------------------#

#---------------------Label Gravedad en el Apartado Incidencias---------------------#
        self.txtGravedad = QLabel("Gravedad: ", self)
        self.txtGravedad.move(50, 280)
        self.txtGravedad.setFont(QFont("Arial", 12)) 
        self.txtGravedad.show()
        #-----------------------------FIN------------------------------#

#---------------------Apartado para seleccionar la Gravedad en el Apartado Incidencias---------------------#
        self.seleccionarGravedad = QComboBox(self) 
        self.seleccionarGravedad.move(150,280)
        self.seleccionarGravedad.resize(100, 30)
        self.seleccionarGravedad.setFont(QFont("Arial", 12))
        self.seleccionarGravedad.addItems(["Baja", "Media", "Alta", "Grave", "Muy Grave"])
        self.seleccionarGravedad.show()
        #-----------------------------FIN------------------------------#

#---------------------Label Fecha en el Apartado Incidencias---------------------#
        self.txtFecha = QLabel("Fecha: ", self)
        self.txtFecha.move(50, 320)
        self.txtFecha.setFont(QFont("Arial", 12)) 
        self.txtFecha.show()
        #-----------------------------FIN------------------------------#

#---------------------Apartado para seleccionar la fecha en el Apartado Incidencias---------------------#
        self.seleccionarFecha = QDateEdit(self) 
        self.seleccionarFecha.move(150,320)
        self.seleccionarFecha.resize(140, 30)
        self.seleccionarFecha.setFont(QFont("Arial", 12))
        self.seleccionarFecha.setCalendarPopup(True)
        self.seleccionarFecha.setDate(QDate.currentDate())
        self.seleccionarFecha.show()
        #-----------------------------FIN------------------------------#

        #---------------------El boton de Registrarse en el Apartado Registrar---------------------#
        self.confirmarIncidencia = QPushButton("Confirmar", self)
        self.confirmarIncidencia.resize(100,30)
        self.confirmarIncidencia.setFont(QFont("Arial", 12))
        self.confirmarIncidencia.move(100,255)
        self.confirmarIncidencia.show()
        self.confirmarIncidencia.clicked.connect(insertarIncidencia)
    #-----------------------------FIN------------------------------#