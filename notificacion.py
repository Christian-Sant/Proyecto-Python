from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QFont, QPalette, QColor

class Toast(QWidget):
    def __init__(self, mensaje, duracion=3000, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Configurar etiqueta
        self.label = QLabel(mensaje, self)
        self.label.setStyleSheet("""
            background-color: rgba(50, 50, 50, 220);
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
        """)
        self.label.setFont(QFont("Arial", 10))
        self.label.adjustSize()

        # Ajustar tamaño del widget
        self.resize(self.label.width(), self.label.height())

        # Posición: esquina superior derecha del parent o de la pantalla
        if parent:
            pos_x = parent.geometry().x() + parent.width() - self.width() - 20
            pos_y = parent.geometry().y() + 20
        else:
            screen = self.screen().availableGeometry()
            pos_x = screen.width() - self.width() - 20
            pos_y = 20
        self.move(pos_x, pos_y)

        # Timer para cerrar automáticamente
        QTimer.singleShot(duracion, self.close)
