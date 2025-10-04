from PyQt5.QtWidgets import QApplication # type: ignore
from interfaz import interfazUsuario
from baseDeDatos import baseDeDatos
baseDeDatos()
aplicacion = QApplication([])
uiUsuario = interfazUsuario()
uiUsuario.show()
aplicacion.exec_()
