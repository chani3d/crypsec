import sys
from PyQt6.QtWidgets import QApplication
from GUI import GUI
from TCP_client import client_program


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = GUI()

    sys.exit(app.exec())
    client_program()
