import sys
from PyQt6.QtWidgets import QApplication
from GUI import ChatApp
from TCP_client import client_program


def main():
    client_program()
    ChatApp()


if __name__ == '__main__':
    main()
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    sys.exit(app.exec())
