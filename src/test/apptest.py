
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the two text boxes
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLabel(self)

        # Set up the layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.textbox1)
        hbox.addWidget(self.textbox2)
        self.setLayout(hbox)

        # Connect the signal from textbox1 to update textbox2
        self.textbox1.textChanged.connect(self.update_textbox2)

    def update_textbox2(self):
        # Get the text from textbox1 and update textbox2
        text = self.textbox1.text()
        self.textbox2.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
