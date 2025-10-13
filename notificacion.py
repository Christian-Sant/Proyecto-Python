from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
#-----------------------------Se crea una clase Toast para poder usarlo para la notificacion local------------------------------#
class Toast(QWidget):
    def __init__(self, mensaje, duracion=3000, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Configurar el Label y su estido
        self.label = QLabel(mensaje, self)
        self.label.setStyleSheet("""
            background-color: rgba(50, 50, 50, 220);
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
        """)
        self.label.setFont(QFont("Arial", 10))
        self.label.adjustSize()

        # Ajustar el tamaño
        self.resize(self.label.width(), self.label.height())

        # Posición arriba a la derecha del padre
        if parent:
            pos_x = parent.geometry().x() + parent.width() - self.width() - 20
            pos_y = parent.geometry().y() + 20
        else:
            screen = self.screen().availableGeometry()
            pos_x = screen.width() - self.width() - 20
            pos_y = 20
        self.move(pos_x, pos_y)

        QTimer.singleShot(duracion, self.close) #Tiempo para que se cierre
#-----------------------------FIN------------------------------#