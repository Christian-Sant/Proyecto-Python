import csv
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QMessageBox, QWidget, QLabel, QPushButton, QTextEdit, QComboBox, QDateEdit,QTableWidget,QToolButton,QMenu,QCheckBox,QWidgetAction,QTableWidgetItem # type: ignore
from PyQt5.QtGui import QFont #type: ignore
from PyQt5.QtCore import QDate #type: ignore
from baseDeDatos import insertarUsuario, insertarIncidencia, vistasIncidencias,actualizarIncidencia, obtener_incidencias,eliminarIncidencia,abrirIncidencia,cerrarIncidencia,vistaCorreoYPassword,vistaCorreo
from utilidades import idAzarIncidencia
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle #type: ignore
from reportlab.lib import colors #type: ignore
from reportlab.lib.pagesizes import letter, landscape #type: ignore
from ia import predecir
from grafico import generar_graficas
from notificacion import Toast
class interfazUsuario(QWidget) :



    #---------------------INICIO---------------------#
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        #---------------------Llamada Iniciar Sesion---------------------#
        self.iniciarSesion()
        #-----------------------------FIN------------------------------
    #---------------------FIN---------------------#



    #---------------------Metodo del apartado Iniciar Sesion---------------------#
    def iniciarSesion(self):

        #---------------------Label Iniciar Sesion---------------------#
        self.txtIniciarSesion = QLabel("Iniciar Sesion", self)
        self.txtIniciarSesion.move(90, 80)
        font = QFont("Arial", 14, QFont.Bold)
        font.setUnderline(True)
        self.txtIniciarSesion.setFont(font)
        #-----------------------------FIN------------------------------#

        #---------------------Label Correo en el Apartado Iniciar Sesion---------------------#
        self.txtCorreoIS = QLabel("Correo: ", self)
        self.txtCorreoIS.move(40, 118)
        self.txtCorreoIS.setFont(QFont("Arial", 12, QFont.Bold)) 
        #-----------------------------FIN------------------------------#


        #---------------------Label Contraseña en el Apartado Iniciar Sesion---------------------#
        self.txtPassword = QLabel("Contraseña: ", self)
        self.txtPassword.move(40, 173)
        self.txtPassword.setFont(QFont("Arial", 12, QFont.Bold)) 
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir el Correo en el Apartado Iniciar Sesion---------------------#
        self.CorreoIS = QLineEdit(self) 
        self.CorreoIS.move(40,135)
        self.CorreoIS.resize(220, 20)
        self.CorreoIS.setFont(QFont("Arial", 12))
        self.CorreoIS.editingFinished.connect(self.validarCorreoInicio)
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir la contraseña en el Apartado Iniciar Sesion---------------------#
        self.password = QLineEdit(self)
        self.password.move(40,190)
        self.password.resize(220, 20)
        self.password.setFont(QFont("Arial", 12))
        self.password.setEchoMode(QLineEdit.Password)
        #-----------------------------FIN------------------------------#


        #---------------------El boton de Iniciar Sesion en el Apartado Iniciar Sesion---------------------#
        self.iniciarSesionBoton = QPushButton("Iniciar Sesión", self)
        self.iniciarSesionBoton.resize(120,30)
        self.iniciarSesionBoton.setFont(QFont("Arial", 12, QFont.Bold))
        self.iniciarSesionBoton.move(140,215)
        self.iniciarSesionBoton.clicked.connect(self.verificarCorreoYPassword) # Los click intentar mantenerlos siempre al lado porque si no, da errores
        #-----------------------------FIN------------------------------#


        #---------------------El boton de Registrar en el Apartado Iniciar Sesion---------------------#
        self.registrarse = QPushButton("Registrar", self)
        self.registrarse.resize(90,30)
        self.registrarse.setFont(QFont("Arial", 12, QFont.Bold))
        self.registrarse.move(40,215)
        self.registrarse.clicked.connect(self.registrar) #Se llama al metodo registrar
        #-----------------------------FIN------------------------------#
    #-----------------------------FIN------------------------------#



    #---------------------Metodo para validar correo---------------------#
    def validarCorreoInicio(self):
        texto = self.CorreoIS.text().strip()

        if not texto:
            return  

        if '@' not in texto:
            texto = texto.replace("gmail.com", "")
            texto = texto + "@gmail.com"

        else:
            nombre = texto.split("@")[0]
            texto = nombre + "@gmail.com"

        self.CorreoIS.setText(texto)
    #-----------------------------FIN------------------------------#



    #---------------------Metodo para validar correo---------------------#
    def validarCorreo(self):
        texto = self.correoRegistro.text().strip()

        if not texto:
            return  
       
        if '@' not in texto:
            texto = texto.replace("gmail.com", "")
            texto = texto + "@gmail.com"

        else:
            nombre = texto.split("@")[0]
            texto = nombre + "@gmail.com"

        self.correoRegistro.setText(texto)
    #-----------------------------FIN------------------------------#



    #---------------------Metodo del apartado Registrar---------------------#
    def registrar(self):

        #---------------------Se oculta toda la interfaz del apartado Iniciar Sesion---------------------#
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesionBoton.hide()
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
        font = QFont("Arial", 14, QFont.Bold)
        font.setUnderline(True)
        self.txtRegistrarse.setFont(font)
        self.txtRegistrarse.show() 
        #-----------------------------FIN------------------------------#


        #---------------------Label Correo en el Apartado Registrar---------------------#
        self.txtCorreo = QLabel("Correo: ", self)
        self.txtCorreo.move(40, 60)
        self.txtCorreo.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtCorreo.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir el Correo en el Apartado Registrar---------------------#
        self.correoRegistro = QLineEdit(self) 
        self.correoRegistro.move(40,80)
        self.correoRegistro.resize(220, 20)
        self.correoRegistro.setFont(QFont("Arial", 12))
        self.correoRegistro.editingFinished.connect(self.validarCorreo)
        self.correoRegistro.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Contraseña en el Apartado Registrar---------------------#
        self.txtPasswordRegistro = QLabel("Contraseña: ", self)
        self.txtPasswordRegistro.move(40, 120)
        self.txtPasswordRegistro.setFont(QFont("Arial", 12, QFont.Bold)) 
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
        self.txtConfirmarPasswordRegistro.setFont(QFont("Arial", 12, QFont.Bold)) 
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
        self.registrarse2.setFont(QFont("Arial", 12, QFont.Bold))
        self.registrarse2.move(190,255)
        self.registrarse2.show()
        self.registrarse2.clicked.connect(self.verificarCorreo)# Llamamos el metodo verificarCorreo
        #-----------------------------FIN------------------------------#

        #---------------------El boton de Registrarse en el Apartado Registrar---------------------#
        self.volver = QPushButton("Volver", self)
        self.volver.resize(60,30)
        self.volver.setFont(QFont("Arial", 12, QFont.Bold))
        self.volver.move(10,255)
        self.volver.show()
        self.volver.clicked.connect(self.volverInicioSesion)# Llamamos el metodo verificarCorreo
        #-----------------------------FIN------------------------------#
    #-----------------------------FIN------------------------------#



    #---------------------Metodo para ocultar registrar y mostrar el inicio de sesion---------------------#
    def volverInicioSesion(self):
        self.txtRegistrarse.hide()
        self.txtCorreo.hide()
        self.correoRegistro.hide()
        self.txtPasswordRegistro.hide()
        self.passwordRegistro.hide()
        self.registrarse2.hide()
        self.txtConfirmarPasswordRegistro.hide()
        self.confirmarPasswordRegistro.hide()
        self.setWindowTitle("Inicio de Sesión")
        self.txtIniciarSesion.show()
        self.CorreoIS.show()
        self.password.show()
        self.txtCorreoIS.show()
        self.txtPassword.show()
        self.iniciarSesionBoton.show()
        self.registrarse.show()
        self.CorreoIS.clear()
        self.password.clear()
        self.volver.hide()
    #-----------------------------FIN------------------------------#



    #---------------------Metodo para ocultar vista y mostrar el inicio de sesion---------------------#
    def volverInicioSesionVista(self):
        self.grafico.hide()
        self.cerrarSesion.hide()
        self.tabla.hide()
        self.filtro.hide()
        self.txtTituloIncidencias.hide()
        self.botonCerrar.hide()
        self.botonAbrir.hide()
        self.botonEliminar.hide()
        self.botonDescargarCSV.hide()
        self.botonDescargarPDF.hide()
        self.txtIniciarSesion.show()
        self.CorreoIS.show()
        self.password.show()
        self.txtCorreoIS.show()
        self.txtPassword.show()
        self.setGeometry(200,200,300,300)
        self.move(800,400)
        self.iniciarSesionBoton.show()
        self.registrarse.show()
        self.setWindowTitle("Inicio de Sesión")
        self.CorreoIS.clear()
        self.password.clear()
    #-----------------------------FIN------------------------------#



    #---------------------Metodo para la creacion de Usuario, se usara en el metodo validarYCrearUsuario---------------------#
    def crearUsuario(self):
        correo = self.correoRegistro.text().strip()
        password = self.passwordRegistro.text().strip()
        insertarUsuario(correo, password)

        #---------------------Se oculta toda la interfaz del apartado Registro---------------------#
        self.volver.hide()
        self.txtRegistrarse.hide()
        self.txtCorreo.hide()
        self.setWindowTitle("Inicio de Sesión")
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
        self.iniciarSesionBoton.show()
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
        correosPassword = dict(vistaCorreoYPassword())#Se hace un diccionario, en el cual el correo es la clave mientras que la contraseña es el valor del clave.
        correo = self.CorreoIS.text().strip()
        password = self.password.text().strip()
        if correo in correosPassword:
            if correosPassword[correo] == password:
                self.correoIniciado = correo
                self.vista()
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



    #---------------------Apartado para la Creacion de Incidencias---------------------#
    def incidencias(self):
        #---------------------Especificar titulo de la ventana, moldear la geometria y moverla. Tambien esconder el apartado de Inicio de Sesion---------------------#
        self.setWindowTitle("Incidencias")
        self.setGeometry(200,200,350,330)
        self.move(800,400)
        self.txtTituloIncidencias.hide()
        self.tabla.hide()
        self.botonCerrar.hide()
        self.botonAbrir.hide()
        self.botonEliminar.hide()
        self.botonDescargarCSV.hide()
        self.botonDescargarPDF.hide()
        self.filtro.hide()
        self.editarIncidencias.hide()
        self.grafico.hide()
        self.crearIncidencias.hide()
        self.cerrarSesion.hide()
        self.menu.hide()
        #-----------------------------FIN------------------------------#



        #---------------------Label Titulo en el Apartado Incidencias---------------------#
        self.txtTitulo = QLabel("Titulo: ", self)
        self.txtTitulo.move(10, 50)
        self.txtTitulo.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtTitulo.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label CREAR INCIDENCIA---------------------#
        self.txtCREARINCIDENCIA = QLabel("CREAR INCIDENCIA", self)
        self.txtCREARINCIDENCIA.move(90, 5)
        font = QFont("Arial", 14, QFont.Bold)
        font.setUnderline(True)
        self.txtCREARINCIDENCIA.setFont(font)
        self.txtCREARINCIDENCIA.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir el Titulo en el Apartado Incidencias---------------------#
        self.escribirTitulo = QLineEdit(self) 
        self.escribirTitulo.move(70,50)
        self.escribirTitulo.resize(220, 20)
        self.escribirTitulo.setFont(QFont("Arial", 12))
        self.escribirTitulo.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Descripcion en el Apartado Incidencias---------------------#
        self.txtDescripcion = QLabel("Descripción: ", self)
        self.txtDescripcion.move(10, 80)
        self.txtDescripcion.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtDescripcion.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir la Descripcion en el Apartado Incidencias---------------------#
        self.escribirDescripcion = QTextEdit(self) 
        self.escribirDescripcion.move(110,80)
        self.escribirDescripcion.resize(220, 80)
        self.escribirDescripcion.setFont(QFont("Arial", 12))
        self.escribirDescripcion.textChanged.connect(self.actualizarPrediccion)
        self.escribirDescripcion.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Gravedad en el Apartado Incidencias---------------------#
        self.txtGravedad = QLabel("Gravedad: ", self)
        self.txtGravedad.move(10, 175)
        self.txtGravedad.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtGravedad.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para seleccionar la Gravedad en el Apartado Incidencias---------------------#
        self.seleccionarGravedad = QComboBox(self) 
        self.seleccionarGravedad.move(95,170)
        self.seleccionarGravedad.resize(100, 30)
        self.seleccionarGravedad.setFont(QFont("Arial", 12))
        self.seleccionarGravedad.addItems(["Baja", "Media", "Alta", "Grave", "Muy Grave"])
        self.seleccionarGravedad.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Fecha en el Apartado Incidencias---------------------#
        self.txtFecha = QLabel("Fecha: ", self)
        self.txtFecha.move(10, 215)
        self.txtFecha.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtFecha.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para seleccionar la fecha en el Apartado Incidencias---------------------#
        self.seleccionarFecha = QDateEdit(self) 
        self.seleccionarFecha.move(70,210)
        self.seleccionarFecha.resize(110, 30)
        self.seleccionarFecha.setFont(QFont("Arial", 12))
        self.seleccionarFecha.setCalendarPopup(True)
        self.seleccionarFecha.setDate(QDate.currentDate())
        self.seleccionarFecha.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Categoria en el Apartado Incidencias---------------------#
        self.txtCategoria = QLabel("Categoria: ", self)
        self.txtCategoria.move(10, 255)
        self.txtCategoria.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtCategoria.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para seleccionar la Categoria en el Apartado Incidencias---------------------#
        self.seleccionarCategoria = QComboBox(self) 
        self.seleccionarCategoria.move(95,250)
        self.seleccionarCategoria.resize(120, 30)
        self.seleccionarCategoria.setFont(QFont("Arial", 12))
        self.seleccionarCategoria.addItems(["HARDWARE", "SOFTWARE"])
        self.seleccionarCategoria.show()
        #-----------------------------FIN------------------------------#


        #---------------------El boton de Confirmacion para la creacion de la Incidencia---------------------#
        self.confirmarIncidencia = QPushButton("Confirmar", self)
        self.confirmarIncidencia.resize(100,30)
        self.confirmarIncidencia.setFont(QFont("Arial", 12, QFont.Bold))
        self.confirmarIncidencia.move(235,290)
        self.confirmarIncidencia.show()
        self.confirmarIncidencia.clicked.connect(self.crearIncidencia)
        #-----------------------------FIN------------------------------#

        self.cancelarIncidencia = QPushButton("Cancelar", self)
        self.cancelarIncidencia.resize(100,30)
        self.cancelarIncidencia.setFont(QFont("Arial", 12, QFont.Bold))
        self.cancelarIncidencia.move(10,290)
        self.cancelarIncidencia.show()
        self.cancelarIncidencia.clicked.connect(self.mostrarVista)
    #-----------------------------FIN------------------------------#   



    #---------------------Metodo para recopilar toda la informacion necesaria para la creacion de una incidencia---------------------#
    def crearIncidencia(self):
        id = idAzarIncidencia()
        titulo = self.escribirTitulo.text().strip()
        descripcion = self.escribirDescripcion.toPlainText().strip()
        gravedad = self.seleccionarGravedad.currentText().strip()
        fecha = self.seleccionarFecha.date().toString("yyyy-MM-dd")
        categoria = self.seleccionarCategoria.currentText().strip()
        if titulo != "" and descripcion != "":
            insertarIncidencia(self.correoIniciado,id, titulo, descripcion, gravedad, fecha, categoria)
            self.mostrarVista()
            toast = Toast("Incidencia Creada", parent=self)
            toast.show()  # Refresca tabla

        #---------------------Damos un mensaje de error si le falta el titulo---------------------# 
        elif titulo == "" and descripcion != "":
            mensajeErrorTitulo = QMessageBox()
            mensajeErrorTitulo.setIcon(QMessageBox.Warning)
            mensajeErrorTitulo.setWindowTitle("Error")
            mensajeErrorTitulo.setText("Te falta el titulo")
            mensajeErrorTitulo.exec_()
        #-----------------------------FIN------------------------------# 


        #---------------------Damos un mensaje de error si le falta la descripcion---------------------# 
        elif titulo != "" and descripcion == "":
            mensajeErrorDescripcion = QMessageBox()
            mensajeErrorDescripcion.setIcon(QMessageBox.Warning)
            mensajeErrorDescripcion.setWindowTitle("Error")
            mensajeErrorDescripcion.setText("Te falta la descripción")
            mensajeErrorDescripcion.exec_()
        #-----------------------------FIN------------------------------# 


        #---------------------Damos un mensaje de error si le falta el titulo y la descripcion--------------------#     
        else:
            mensajeErrorTituloDescripcion = QMessageBox()
            mensajeErrorTituloDescripcion.setIcon(QMessageBox.Warning)
            mensajeErrorTituloDescripcion.setWindowTitle("Error")
            mensajeErrorTituloDescripcion.setText("Te falta la titulo y la descripción")
            mensajeErrorTituloDescripcion.exec_()
        #-----------------------------FIN------------------------------# 
    #-----------------------------FIN------------------------------#         



    #---------------------Metodo para mostrar el apartado de vistas---------------------#    
    def mostrarVista(self):

        #---------------------Ocultamos el apartado de Creacion de Incidencias y mostramos la vista---------------------#  
        self.txtTitulo.hide()
        self.txtCREARINCIDENCIA.hide()
        self.escribirTitulo.hide()
        self.txtDescripcion.hide()
        self.escribirDescripcion.hide()
        self.txtGravedad.hide()
        self.seleccionarGravedad.hide()
        self.cancelarIncidencia.hide()
        self.txtFecha.hide()
        self.seleccionarFecha.hide()
        self.txtCategoria.hide()
        self.seleccionarCategoria.hide()
        self.confirmarIncidencia.hide()
        self.botonDescargarCSV.show()
        self.botonDescargarPDF.show()
        self.botonCerrar.show()
        self.botonAbrir.show()
        self.botonEliminar.show()
        self.editarIncidencias.show()
        self.grafico.show()
        self.txtTituloIncidencias.show()
        self.crearIncidencias.show()
        self.cerrarSesion.show()
        self.filtrototal()
        self.tabla.show()
        self.filtro.show()
        self.setWindowTitle("Visualización")
        self.setGeometry(200, 200, 737, 540)
        self.move(600, 300)
        #-----------------------------FIN------------------------------# 
    #-----------------------------FIN------------------------------#     



    #---------------------Ocultamos el apartado de Edicion de Incidencias y mostramos la vista---------------------#  
    def mostrarVistaEdit(self):
        self.setGeometry(200, 200, 737, 540)
        self.move(600, 300)
        self.txtTituloEdit.hide()
        self.txtCREARINCIDENCIAEdit.hide()
        self.escribirTituloEdit.hide()
        self.txtDescripcionEdit.hide()
        self.escribirDescripcionEdit.hide()
        self.txtGravedadEdit.hide()
        self.seleccionarGravedadEdit.hide()
        self.txtFechaEdit.hide()
        self.seleccionarFechaEdit.hide()
        self.txtCategoriaEdit.hide()
        self.seleccionarCategoriaEdit.hide()
        self.confirmarIncidenciaEdit.hide()
        self.cancelarIncidenciaEdit.hide()
        self.editarIncidencias.show()
        self.botonDescargarCSV.show()
        self.botonDescargarPDF.show()
        self.grafico.show()
        self.botonCerrar.show()
        self.botonAbrir.show()
        self.botonEliminar.show()
        self.crearIncidencias.show()
        self.txtTituloIncidencias.show()
        self.cerrarSesion.show()
        self.filtrototal()
        self.tabla.show()
        self.filtro.show()
        self.setWindowTitle("Visualización")
    #-----------------------------FIN------------------------------#     



    #-----------------------------Apartado para el visual de las Incidencias------------------------------# 
    def vista(self):
        self.setWindowTitle("Visualización")
        self.setGeometry(200, 200, 737, 540)
        self.move(600, 300)

        #-----------------------------Ocultamos el apartado de Inicio de Sesion------------------------------# 
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesionBoton.hide()
        self.registrarse.hide()
        #-----------------------------FIN------------------------------# 
        

        #-----------------------------El boton para acceder al apartado de Creacion de Incidencia------------------------------# 
        self.editarIncidencias = QPushButton("Editar", self)
        self.editarIncidencias.resize(140, 30)
        self.editarIncidencias.setFont(QFont("Arial", 12))
        self.editarIncidencias.move(202, 500)
        self.editarIncidencias.show()
        self.editarIncidencias.clicked.connect(self.editar)
        #-----------------------------FIN------------------------------# 


        #---------------------Label Categoria en el Apartado Incidencias---------------------#
        self.txtTituloIncidencias = QLabel("INCIDENCIAS", self)
        self.txtTituloIncidencias.move(295, 10)
        font = QFont("Arial", 16, QFont.Bold)
        font.setUnderline(True)
        self.txtTituloIncidencias.setFont(font) 
        self.txtTituloIncidencias.show()
        #-----------------------------FIN------------------------------#

        #-----------------------------El boton para eliminar una fila en el apartado Vista------------------------------# 
        self.botonEliminar = QPushButton("Eliminar", self)
        self.botonEliminar.resize(140, 30)
        self.botonEliminar.setFont(QFont("Arial", 12))
        self.botonEliminar.move(202, 58)
        self.botonEliminar.show()
        self.botonEliminar.clicked.connect(self.eliminar_incidencia)
        #-----------------------------FIN------------------------------# 

        #-----------------------------El boton para Abrir una incidencia en el apartado Vista------------------------------# 
        self.botonAbrir = QPushButton("Abrir", self)
        self.botonAbrir.resize(140, 30)
        self.botonAbrir.setFont(QFont("Arial", 12))
        self.botonAbrir.move(394, 58)
        self.botonAbrir.show()
        self.botonAbrir.clicked.connect(self.abrir_incidencia)
        #-----------------------------FIN------------------------------#

        #-----------------------------El boton para Cerrar una incidencia en el apartado Vista------------------------------# 
        self.botonCerrar = QPushButton("Cerrar", self)
        self.botonCerrar.resize(140, 30)
        self.botonCerrar.setFont(QFont("Arial", 12))
        self.botonCerrar.move(587, 58)
        self.botonCerrar.show()
        self.botonCerrar.clicked.connect(self.cerrar_incidencia)
        #-----------------------------FIN------------------------------#


        #-----------------------------El boton para acceder al apartado de Creacion de Incidencia------------------------------# 
        self.grafico = QPushButton("Grafico", self)
        self.grafico.resize(140, 30)
        self.grafico.setFont(QFont("Arial", 12))
        self.grafico.move(394, 500)
        self.grafico.show()
        self.grafico.clicked.connect(self.mostrar_grafico)
        #-----------------------------FIN------------------------------# 

        #-----------------------------El boton para acceder al apartado de Creacion de Incidencia------------------------------# 
        self.crearIncidencias = QPushButton("Crear incidencia", self)
        self.crearIncidencias.resize(140, 30)
        self.crearIncidencias.setFont(QFont("Arial", 12))
        self.crearIncidencias.move(587, 500)
        self.crearIncidencias.show()
        self.crearIncidencias.clicked.connect(self.incidencias)
        #-----------------------------FIN------------------------------# 


        #-----------------------------El boton para acceder al apartado de Creacion de Incidencia------------------------------# 
        self.cerrarSesion = QPushButton("Cerrar Sesion", self)
        self.cerrarSesion.resize(140, 30)
        self.cerrarSesion.setFont(QFont("Arial", 12))
        self.cerrarSesion.move(10, 500)
        self.cerrarSesion.show()
        self.cerrarSesion.clicked.connect(self.volverInicioSesionVista)
        #-----------------------------FIN------------------------------# 


        #-----------------------------Creacion de la tabla para poder visualizar los datos de las incidencias------------------------------# 
        self.tabla = QTableWidget(self)
        self.tabla.setGeometry(10, 90, 717, 400)
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels(["ID", "Titulo", "Descripcion", "Gravedad", "Fecha","Estado","Categoria"])
        self.tabla.show()
        resultado = vistasIncidencias(self.correoIniciado)
        self.cargar_tabla(resultado)
        #-----------------------------FIN------------------------------# 


        #-----------------------------Creacion del boton para descargar el PDF------------------------------# 
        self.botonDescargarPDF = QPushButton("PDF", self)
        self.botonDescargarPDF.clicked.connect(self.descargar_pdf)
        self.botonDescargarPDF.move(675,5)
        self.botonDescargarPDF.setFont(QFont("Arial", 12))
        self.botonDescargarPDF.resize(50, 20)
        self.botonDescargarPDF.show()

        self.botonDescargarCSV = QPushButton("CSV", self)
        self.botonDescargarCSV.clicked.connect(self.descargar_csv)
        self.botonDescargarCSV.move(625,5)
        self.botonDescargarCSV.setFont(QFont("Arial", 12))
        self.botonDescargarCSV.resize(50, 20)
        self.botonDescargarCSV.show()
        #-----------------------------FIN------------------------------# 


        #-----------------------------Creacion del boton para poder seleccionar el filtrado------------------------------# 
        self.filtro = QToolButton(self)
        self.filtro.setText("FILTRAR")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.setGeometry(10, 10, 130, 30)
        self.filtro.move(10,58)
        self.filtro.setPopupMode(QToolButton.InstantPopup)
        #-----------------------------FIN------------------------------# 

        #-----------------------------Creacion del menu de filtros------------------------------# 
        self.menu = QMenu(self)

        #-----------------------------Checkbox de Software------------------------------#
        self.checkboxSoftware = QCheckBox("SOFTWARE")
        self.checkboxSoftware.stateChanged.connect(self.filtrototal)
        evento1 = QWidgetAction(self.menu)
        evento1.setDefaultWidget(self.checkboxSoftware)
        self.menu.addAction(evento1)
        #-----------------------------FIN------------------------------#

        #-----------------------------Checkbox de Hardware------------------------------#
        self.checkboxHardware = QCheckBox("HARDWARE")
        self.checkboxHardware.stateChanged.connect(self.filtrototal)
        evento2 = QWidgetAction(self.menu)
        evento2.setDefaultWidget(self.checkboxHardware)
        self.menu.addAction(evento2)
        #-----------------------------FIN------------------------------#

        self.menu.addSeparator()#Añadimos un separador


        #-----------------------------Checkbox de Abierto------------------------------#
        self.checkboxAbierto = QCheckBox("ABIERTO")
        self.checkboxAbierto.stateChanged.connect(self.filtrototal)
        evento3 = QWidgetAction(self.menu)
        evento3.setDefaultWidget(self.checkboxAbierto)
        self.menu.addAction(evento3)
        #-----------------------------FIN------------------------------#

        #-----------------------------Checkbox de Cerrado------------------------------#
        self.checkboxCerrado = QCheckBox("CERRADO")
        self.checkboxCerrado.stateChanged.connect(self.filtrototal)
        evento4 = QWidgetAction(self.menu)
        evento4.setDefaultWidget(self.checkboxCerrado)
        self.menu.addAction(evento4)
        #-----------------------------FIN------------------------------#

        self.menu.addSeparator()#Añadimos un separador

        #-----------------------------Checkbox de Baja------------------------------#
        self.checkboxBaja = QCheckBox("Baja")
        evento5 = QWidgetAction(self.menu)
        evento5.setDefaultWidget(self.checkboxBaja)
        self.menu.addAction(evento5)
        #-----------------------------FIN------------------------------#

        #-----------------------------Checkbox de Media------------------------------#
        self.checkboxMedia = QCheckBox("Media")
        self.checkboxMedia.stateChanged.connect(self.filtrototal)
        evento6 = QWidgetAction(self.menu)
        evento6.setDefaultWidget(self.checkboxMedia)
        self.menu.addAction(evento6)
        #-----------------------------FIN------------------------------#

        #-----------------------------Checkbox de Alta------------------------------#
        self.checkboxAlta = QCheckBox("Alta")
        self.checkboxAlta.stateChanged.connect(self.filtrototal)
        evento7 = QWidgetAction(self.menu)
        evento7.setDefaultWidget(self.checkboxAlta)
        self.menu.addAction(evento7)
        #-----------------------------FIN------------------------------#

        #-----------------------------Checkbox de Grave------------------------------#
        self.checkboxGrave = QCheckBox("Grave")
        self.checkboxGrave.stateChanged.connect(self.filtrototal)
        evento8 = QWidgetAction(self.menu)
        evento8.setDefaultWidget(self.checkboxGrave)
        self.menu.addAction(evento8)
        #-----------------------------FIN------------------------------#

        #-----------------------------Checkbox de Muy Grave------------------------------#
        self.checkboxMuyGrave = QCheckBox("Muy Grave")
        self.checkboxMuyGrave.stateChanged.connect(self.filtrototal)
        evento9 = QWidgetAction(self.menu)
        evento9.setDefaultWidget(self.checkboxMuyGrave)
        self.menu.addAction(evento9)
        #-----------------------------FIN------------------------------#

        self.menu.addSeparator()#Añadimos un separador


        hoy = QDate.currentDate()#Fecha actual

        primer_dia = QDate(hoy.year(), hoy.month(), 1)#Primer dia del mes

        ultimo_dia = primer_dia.addMonths(1).addDays(-1)#Ultimo dia del mes

        #-----------------------------Fecha inicial------------------------------#
        self.fechaInicioEdit = QDateEdit(self)
        self.fechaInicioEdit.setCalendarPopup(True)
        self.fechaInicioEdit.setDate(primer_dia)
        actionFechaInicioEdit = QWidgetAction(self.menu)
        actionFechaInicioEdit.setDefaultWidget(self.fechaInicioEdit)
        self.menu.addAction(actionFechaInicioEdit)
        #-----------------------------FIN------------------------------#

        #-----------------------------Fecha final------------------------------#
        self.fechaFinEdit = QDateEdit(self)
        self.fechaFinEdit.setCalendarPopup(True)
        self.fechaFinEdit.setDate(ultimo_dia)  # Último día del mes
        actionFechaFinEdit = QWidgetAction(self.menu)
        actionFechaFinEdit.setDefaultWidget(self.fechaFinEdit)
        self.menu.addAction(actionFechaFinEdit)
        self.fechaInicioEdit.dateChanged.connect(self.filtrototal)
        self.fechaFinEdit.dateChanged.connect(self.filtrototal)
        #-----------------------------FIN------------------------------#

        #-----------------------------Asignamos el menu al boton de filtro------------------------------#
        self.filtro.setMenu(self.menu)
        self.filtro.show()
    #-----------------------------FIN------------------------------#



    #-----------------------------Metodo para actualizar la tabla cada vez que se filtra------------------------------#
    def filtrototal(self):
        #-----------------------------Array para almacenar que categorias estan seleccionadas------------------------------#
        categorias = []
        if self.checkboxSoftware.isChecked():
            categorias.append("SOFTWARE")
        if self.checkboxHardware.isChecked():
            categorias.append("HARDWARE")
        #-----------------------------FIN------------------------------#
        
        #-----------------------------Array para almacenar los estados seleccionados------------------------------#
        estados = []
        if self.checkboxAbierto.isChecked():
            estados.append("ABIERTO")
        if self.checkboxCerrado.isChecked():
            estados.append("CERRADO")
        #-----------------------------FIN------------------------------#
       
        #-----------------------------Array para almacenar las gravedades seleccionadas------------------------------#
        gravedades = []
        if self.checkboxBaja.isChecked():
            gravedades.append("Baja")
        if self.checkboxMedia.isChecked():
            gravedades.append("Media")
        if self.checkboxAlta.isChecked():
            gravedades.append("Alta")
        if self.checkboxGrave.isChecked():
            gravedades.append("Grave")
        if self.checkboxMuyGrave.isChecked():
            gravedades.append("Muy Grave")
        #-----------------------------FIN------------------------------#

        #-----------------------------Transformamos el filtro de la fecha inicial y fecha final a string para que lo recoja la base de datos------------------------------#
        fecha_inicio = self.fechaInicioEdit.date().toString("yyyy-MM-dd")
        fecha_fin = self.fechaFinEdit.date().toString("yyyy-MM-dd")
        #-----------------------------FIN------------------------------#

        resultados = obtener_incidencias(self.correoIniciado, categorias, estados, gravedades,fecha_inicio,fecha_fin)#Llamamos el metodo de la base de datos para filtrar
        self.cargar_tabla(resultados)#Actualizamos la tabla
    #-----------------------------FIN------------------------------#



    #-----------------------------Metodo para descargar la tabla en CSV------------------------------#
    def descargar_csv(self):
    
      
        ruta_csv, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "Archivos CSV (*.csv)")  # Poner el nombre del documento
        if not ruta_csv:
            return 
        
        # Extraer datos de la tabla
        filas = self.tabla.rowCount()
        columnas = self.tabla.columnCount()

      
        with open(ruta_csv, mode='w', newline='', encoding='utf-8') as archivo: # Abrir archivo CSV
            writer = csv.writer(archivo)

            encabezados = [self.tabla.horizontalHeaderItem(col).text() if self.tabla.horizontalHeaderItem(col) else f"Col {col+1}" for col in range(columnas)]# Encabezados
            writer.writerow(encabezados)

           
            for fila in range(filas): # Filas
                fila_datos = []
                for col in range(columnas):
                    item = self.tabla.item(fila, col)
                    fila_datos.append(item.text() if item else "")
                writer.writerow(fila_datos)

        toast = Toast("CSV descargado correctamente", parent=self) #Notificacion
        toast.show()
    #-----------------------------FIN------------------------------#



    #-----------------------------Metodo para descargar la tabla en PDF------------------------------#
    def descargar_pdf(self):
        
        ruta_pdf, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "", "Archivos PDF (*.pdf)") # Poner el nombre del documento
        if not ruta_pdf:
            return 

        # Extraer datos de la tabla
        filas = self.tabla.rowCount()
        columnas = self.tabla.columnCount()
        datos = []

        
        encabezados = [self.tabla.horizontalHeaderItem(col).text() if self.tabla.horizontalHeaderItem(col) else f"Col {col+1}" for col in range(columnas)]# Encabezados
        datos.append(encabezados)

       
        for fila in range(filas): # Filas
            fila_datos = []
            for col in range(columnas):
                item = self.tabla.item(fila, col)
                fila_datos.append(item.text() if item else "")
            datos.append(fila_datos)

        # Crear PDF
        pdf = SimpleDocTemplate(ruta_pdf, pagesize=landscape(letter))
        tabla_pdf = Table(datos)

        # Estilo de la tabla
        estilo = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ])
        tabla_pdf.setStyle(estilo)

        # Generar documento
        pdf.build([tabla_pdf])

        toast = Toast("PDF descargado correctamente", parent=self) # Notificacion
        toast.show()  
    #-----------------------------FIN------------------------------#



    #-----------------------------Metodo para cargar la tabla------------------------------#
    def cargar_tabla(self, datos):
        self.tabla.clearContents()
        self.tabla.setRowCount(len(datos))
        for fila_idx, fila_data in enumerate(datos):
            for col_idx, valor in enumerate(fila_data):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila_idx, col_idx, item)
     #-----------------------------FIN------------------------------#
                
     #-----------------------------Metodo para editar la incidencia seleccionada------------------------------#
    def editar(self):
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Atención", "Selecciona una incidencia para editar")
            return
        #-----------------------------Recogida de datos de la incincia seleccionada------------------------------#
        self.id_incidencia = self.tabla.item(fila, 0).text()  
        titulo = self.tabla.item(fila, 1).text()        
        descripcion = self.tabla.item(fila, 2).text()   
        gravedad = self.tabla.item(fila, 3).text()   
        fecha = self.tabla.item(fila, 4).text()       
        categoria = self.tabla.item(fila, 6).text() 
        #-----------------------------FIN------------------------------#

        #---------------------Especificar titulo de la ventana, moldear la geometria y moverla. Tambien esconder el apartado de Inicio de Sesion---------------------#
        self.setWindowTitle("Editar Incidencia")
        self.setGeometry(200,200,350,330)
        self.move(800,400)
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesionBoton.hide()
        self.txtTituloIncidencias.hide()
        self.registrarse.hide()
        self.tabla.hide()
        self.botonCerrar.hide()
        self.botonAbrir.hide()
        self.botonEliminar.hide()
        self.filtro.hide()
        self.editarIncidencias.hide()
        self.grafico.hide()
        self.crearIncidencias.hide()
        self.cerrarSesion.hide()
        self.menu.hide()
        #-----------------------------FIN------------------------------#



        #---------------------Label Titulo--------------------#
        self.txtTituloEdit = QLabel("Titulo: ", self)
        self.txtTituloEdit.move(10, 50)
        self.txtTituloEdit.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtTituloEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label EDITAR INCIDENCIA---------------------#
        self.txtCREARINCIDENCIAEdit = QLabel("EDITAR INCIDENCIA", self)
        self.txtCREARINCIDENCIAEdit.move(85, 5)
        font = QFont("Arial", 14, QFont.Bold)
        font.setUnderline(True)
        self.txtCREARINCIDENCIAEdit.setFont(font)
        self.txtCREARINCIDENCIAEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir el Titulo---------------------#
        self.escribirTituloEdit = QLineEdit(self) 
        self.escribirTituloEdit.move(70,50)
        self.escribirTituloEdit.resize(220, 20)
        self.escribirTituloEdit.setFont(QFont("Arial", 12))
        self.escribirTituloEdit.show()
        self.escribirTituloEdit.setText(titulo)
        #-----------------------------FIN------------------------------#


        #---------------------Label de la nueva Descripcion---------------------#
        self.txtDescripcionEdit = QLabel("Descripción: ", self)
        self.txtDescripcionEdit.move(10, 80)
        self.txtDescripcionEdit.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtDescripcionEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para escribir la nueva Descripcion---------------------#
        self.escribirDescripcionEdit = QTextEdit(self) 
        self.escribirDescripcionEdit.move(110,80)
        self.escribirDescripcionEdit.resize(220, 80)
        self.escribirDescripcionEdit.setFont(QFont("Arial", 12))
        self.escribirDescripcionEdit.setPlainText(descripcion)
        self.escribirDescripcionEdit.textChanged.connect(self.actualizarPrediccionEdit)
        self.escribirDescripcionEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Label Gravedad---------------------#
        self.txtGravedadEdit = QLabel("Gravedad: ", self)
        self.txtGravedadEdit.move(10, 175)
        self.txtGravedadEdit.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtGravedadEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para seleccionar la Gravedad---------------------#
        self.seleccionarGravedadEdit = QComboBox(self) 
        self.seleccionarGravedadEdit.move(95,170)
        self.seleccionarGravedadEdit.resize(100, 30)
        self.seleccionarGravedadEdit.setFont(QFont("Arial", 12))
        self.seleccionarGravedadEdit.addItems(["Baja", "Media", "Alta", "Grave", "Muy Grave"])
        self.seleccionarGravedadEdit.show()
        self.seleccionarGravedadEdit.setCurrentText(gravedad)
        #-----------------------------FIN------------------------------#


        #---------------------Label Fecha---------------------#
        self.txtFechaEdit = QLabel("Fecha: ", self)
        self.txtFechaEdit.move(10, 215)
        self.txtFechaEdit.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtFechaEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para seleccionar la fecha---------------------#
        fecha_obj = QDate.fromString(fecha, "yyyy-MM-dd")
        self.seleccionarFechaEdit = QDateEdit(self) 
        self.seleccionarFechaEdit.move(70,210)
        self.seleccionarFechaEdit.resize(110, 30)
        self.seleccionarFechaEdit.setFont(QFont("Arial", 12))
        self.seleccionarFechaEdit.setCalendarPopup(True)
        self.seleccionarFechaEdit.setDate(QDate.currentDate())
        self.seleccionarFechaEdit.show()
        self.seleccionarFechaEdit.setDate(fecha_obj)
        #-----------------------------FIN------------------------------#


        #---------------------Label Categoria---------------------#
        self.txtCategoriaEdit = QLabel("Categoria: ", self)
        self.txtCategoriaEdit.move(10, 255)
        self.txtCategoriaEdit.setFont(QFont("Arial", 12, QFont.Bold)) 
        self.txtCategoriaEdit.show()
        #-----------------------------FIN------------------------------#


        #---------------------Apartado para seleccionar la Categoria---------------------#
        self.seleccionarCategoriaEdit = QComboBox(self) 
        self.seleccionarCategoriaEdit.move(95,250)
        self.seleccionarCategoriaEdit.resize(120, 30)
        self.seleccionarCategoriaEdit.setFont(QFont("Arial", 12))
        self.seleccionarCategoriaEdit.addItems(["HARDWARE", "SOFTWARE"])
        self.seleccionarCategoriaEdit.show()
        self.seleccionarCategoriaEdit.setCurrentText(categoria)
        #-----------------------------FIN------------------------------#

        #---------------------El boton de Confirmacion para editar la incidencia---------------------#
        self.confirmarIncidenciaEdit = QPushButton("Confirmar", self)
        self.confirmarIncidenciaEdit.resize(100,30)
        self.confirmarIncidenciaEdit.setFont(QFont("Arial", 12, QFont.Bold))
        self.confirmarIncidenciaEdit.move(235,290)
        self.confirmarIncidenciaEdit.show()
        self.confirmarIncidenciaEdit.clicked.connect(self.editarIncidencia)
        #-----------------------------FIN------------------------------#

        #---------------------El boton para cancelar la edicion de la incidencia---------------------#
        self.cancelarIncidenciaEdit = QPushButton("Cancelar", self)
        self.cancelarIncidenciaEdit.resize(100,30)
        self.cancelarIncidenciaEdit.setFont(QFont("Arial", 12, QFont.Bold))
        self.cancelarIncidenciaEdit.move(10,290)
        self.cancelarIncidenciaEdit.show()
        self.cancelarIncidenciaEdit.clicked.connect(self.mostrarVistaEdit)
        #-----------------------------FIN------------------------------#
    #-----------------------------FIN------------------------------#



    #-----------------------------Metodo para que se edite la incidencia despues de Confirmar------------------------------#
    def editarIncidencia(self):
        tituloReemplazo = self.escribirTituloEdit.text().strip()
        descripcionReemplazo = self.escribirDescripcionEdit.toPlainText().strip()
        gravedadReemplazo = self.seleccionarGravedadEdit.currentText().strip()
        fechaReemplazo = self.seleccionarFechaEdit.date().toString("yyyy-MM-dd")
        categoriaReemplazo = self.seleccionarCategoriaEdit.currentText().strip()
        if tituloReemplazo != "" and descripcionReemplazo != "":
            actualizarIncidencia(self.id_incidencia,tituloReemplazo,descripcionReemplazo,gravedadReemplazo,fechaReemplazo,categoriaReemplazo)
            self.mostrarVistaEdit()
            toast = Toast("Incidencia Editada", parent=self)
            toast.show()  # Refresca tabla

        #---------------------Damos un mensaje de error si le falta el titulo---------------------# 
        elif tituloReemplazo == "" and descripcionReemplazo != "":
            mensajeErrorTitulo = QMessageBox()
            mensajeErrorTitulo.setIcon(QMessageBox.Warning)
            mensajeErrorTitulo.setWindowTitle("Error")
            mensajeErrorTitulo.setText("Te falta el titulo")
            mensajeErrorTitulo.exec_()
        #-----------------------------FIN------------------------------# 


        #---------------------Damos un mensaje de error si le falta la descripcion---------------------# 
        elif tituloReemplazo != "" and descripcionReemplazo == "":
            mensajeErrorDescripcion = QMessageBox()
            mensajeErrorDescripcion.setIcon(QMessageBox.Warning)
            mensajeErrorDescripcion.setWindowTitle("Error")
            mensajeErrorDescripcion.setText("Te falta la descripción")
            mensajeErrorDescripcion.exec_()
        #-----------------------------FIN------------------------------# 


        #---------------------Damos un mensaje de error si le falta el titulo y la descripcion--------------------#     
        else:
            mensajeErrorTituloDescripcion = QMessageBox()
            mensajeErrorTituloDescripcion.setIcon(QMessageBox.Warning)
            mensajeErrorTituloDescripcion.setWindowTitle("Error")
            mensajeErrorTituloDescripcion.setText("Te falta la titulo y la descripción")
            mensajeErrorTituloDescripcion.exec_()
        #-----------------------------FIN------------------------------# 
    #-----------------------------FIN------------------------------#         
    


    #-----------------------------Metodo de IA para seleccion automatica de Categoria y Gravedad------------------------------#    
    def actualizarPrediccion(self):
        
        descripcion = self.escribirDescripcion.toPlainText().strip() #Obtener la descripcion que se esta escribiendo ahora mismo
        if descripcion == "":
            return


        categoria, gravedad = predecir(descripcion)  # Usar la IA

        if categoria:
            
            cambioCategoria = self.seleccionarCategoria.findText(categoria) #Indicar el valor que debe tener
            if cambioCategoria != -1:
                self.seleccionarCategoria.setCurrentIndex(cambioCategoria)

        if gravedad:
           
            cambioGravedad = self.seleccionarGravedad.findText(gravedad)#Indicar el valor que debe tener
            if cambioGravedad != -1:
                self.seleccionarGravedad.setCurrentIndex(cambioGravedad)
    #-----------------------------FIN------------------------------#    



    #-----------------------------Metodo de IA para seleccion automatica de Categoria y Gravedad en la edicion de la Incidencia------------------------------#    
    def actualizarPrediccionEdit(self):
        
        descripcion = self.escribirDescripcionEdit.toPlainText().strip() #Obtener la descripcion que se esta escribiendo ahora mismo
        if descripcion == "":
            return


        categoria, gravedad = predecir(descripcion)  # Usar la IA

        if categoria:
            
            cambioCategoria = self.seleccionarCategoriaEdit.findText(categoria) #Indicar el valor que debe tener
            if cambioCategoria != -1:
                self.seleccionarCategoriaEdit.setCurrentIndex(cambioCategoria)

        if gravedad:
           
            cambioGravedad = self.seleccionarGravedadEdit.findText(gravedad)#Indicar el valor que debe tener
            if cambioGravedad != -1:
                self.seleccionarGravedadEdit.setCurrentIndex(cambioGravedad)
    #-----------------------------FIN------------------------------#  



    #-----------------------------Metodo para eliminar Incidencia------------------------------#  
    def eliminar_incidencia(self):
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Atención", "Selecciona una incidencia")
            return
        
        self.id_incidencia = self.tabla.item(fila, 0).text() 

        if self.id_incidencia:
            respuesta = QMessageBox.question(
                self,
                "Confirmar eliminación",
                f"¿Estás seguro de eliminar la incidencia con ID {self.id_incidencia}?",
                QMessageBox.Yes | QMessageBox.No
            )
            if respuesta == QMessageBox.Yes:
                eliminarIncidencia(self.id_incidencia)  
                self.filtrototal()
                toast = Toast("Incidencia Eliminada", parent=self) #Notificacion
                toast.show()
    #-----------------------------FIN------------------------------#  



    #-----------------------------Metodo para Abrir una Incidencia------------------------------#  
    def abrir_incidencia(self):
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Atención", "Selecciona una incidencia")
            return
        
        self.id_incidencia = self.tabla.item(fila, 0).text()  

        if self.id_incidencia:
            abrirIncidencia(self.id_incidencia)  
            self.filtrototal()
            toast = Toast("Incidencia Abierta", parent=self) #Notificacion
            toast.show()  
    #-----------------------------FIN------------------------------#



    #-----------------------------Metodo para Cerrar una Incidencia------------------------------#  
    def cerrar_incidencia(self):
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Atención", "Selecciona una incidencia")
            return
        
        self.id_incidencia = self.tabla.item(fila, 0).text()  

        if self.id_incidencia:
            cerrarIncidencia(self.id_incidencia)  
            self.filtrototal()
            toast = Toast("Incidencia Cerrada", parent=self) #Notificacion
            toast.show()  
    #-----------------------------FIN------------------------------#



     #-----------------------------Metodo para tener el grafico------------------------------# 
    def mostrar_grafico(self):
        generar_graficas(self.correoIniciado)
    #-----------------------------FIN------------------------------#


        
    