from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QWidget, QLabel, QPushButton, QTextEdit, QComboBox, QDateEdit,QTableWidget,QAction,QToolButton,QMenu,QCheckBox,QWidgetAction,QTableWidgetItem # type: ignore
from PyQt5.QtGui import QFont #type: ignore
from PyQt5.QtCore import QDate #type: ignore
from baseDeDatos import insertarUsuario, insertarIncidencia, vistasIncidencias
from utilidades import idAzarIncidencia
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


    #---------------------Metodo para la creacion de Usuario, se usara en el metodo validarYCrearUsuario---------------------#
    def crearUsuario(self):
        correo = self.correoRegistro.text().strip()
        password = self.passwordRegistro.text().strip()
        insertarUsuario(correo, password)

        #---------------------Se oculta toda la interfaz del apartado Registro---------------------#
        self.volver.hide()
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
        self.txtIniciarSesion.hide()
        self.CorreoIS.hide()
        self.password.hide()
        self.txtCorreoIS.hide()
        self.txtPassword.hide()
        self.iniciarSesionBoton.hide()
        self.registrarse.hide()
        self.crearincidencias.hide()
        self.tabla.hide()
        self.filtro.hide()
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
        self.txtFecha.hide()
        self.seleccionarFecha.hide()
        self.txtCategoria.hide()
        self.seleccionarCategoria.hide()
        self.confirmarIncidencia.hide()
        self.cargar_tabla()
        self.crearincidencias.show()
        self.tabla.show()
        self.filtro.show()
        self.setWindowTitle("Visualización")
        self.setGeometry(200, 200, 737, 540)
        self.move(600, 300)
        #-----------------------------FIN------------------------------# 
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
        self.crearincidencias = QPushButton("Crear incidencia", self)
        self.crearincidencias.resize(170, 30)
        self.crearincidencias.setFont(QFont("Arial", 12))
        self.crearincidencias.move(557, 500)
        self.crearincidencias.show()
        self.crearincidencias.clicked.connect(self.incidencias)
        #-----------------------------FIN------------------------------# 


        #-----------------------------Creacion de la tabla para poder visualizar los datos de las incidencias------------------------------# 
        self.tabla = QTableWidget(self)
        self.tabla.setGeometry(10, 90, 717, 400)
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels(["ID", "Titulo", "Descripcion", "Gravedad", "Fecha", "Categoria", "Estado"])
        self.tabla.show()
        self.cargar_tabla()
        #-----------------------------FIN------------------------------# 

       

        #-----------------------------Creacion del boton para poder seleccionar el filtrado------------------------------# 
        self.filtro = QToolButton(self)
        self.filtro.setText("FILTRAR")
        self.filtro.setFont(QFont("Arial", 12))
        self.filtro.setGeometry(10, 10, 100, 25)
        self.filtro.move(10,62)
        self.filtro.setPopupMode(QToolButton.InstantPopup)
        #-----------------------------FIN------------------------------# 


        #-----------------------------Creacion del menu con checkbox------------------------------# 
        menu = QMenu(self)

        # Sección de categorías
        for texto in ["SOFTWARE", "HARDWARE"]:
            chk = QCheckBox(texto)
            action = QWidgetAction(menu)
            action.setDefaultWidget(chk)
            menu.addAction(action)

        menu.addSeparator()

        # Sección de estados
        for texto in ["ABIERTO", "CERRADO"]:
            chk = QCheckBox(texto)
            action = QWidgetAction(menu)
            action.setDefaultWidget(chk)
            menu.addAction(action)

        self.filtro.setMenu(menu)
        self.filtro.show()
        #-----------------------------FIN------------------------------#

        # Función para manejar cambios en los checkboxes
    #-----------------------------FIN------------------------------#


    def cargar_tabla(self):
        datos = vistasIncidencias(self.correoIniciado)  # Trae los datos de la base
        self.tabla.clearContents()    # Limpia contenido previo
        self.tabla.setRowCount(len(datos))  # Ajusta filas al número de registros

        for fila_idx, fila_data in enumerate(datos):
            for col_idx, valor in enumerate(fila_data):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila_idx, col_idx, item)



        
    