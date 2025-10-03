from PyQt5.QtWidgets import QApplication # type: ignore
from interfaz import interfazUsuario
aplicacion = QApplication([])
uiUsuario = interfazUsuario()
uiUsuario.show()
aplicacion.exec_()
