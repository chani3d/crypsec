import sys
import random

from PyQt6.QtWidgets import QLineEdit
from PySide6 import QtCore, QtWidgets, QtGui



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Send")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)
        


        self.button.clicked.connect(self.magic)

        #Window title
        self.setWindowTitle("Yoo")





    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
