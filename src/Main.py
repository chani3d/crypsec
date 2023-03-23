import sys
from PyQt6.QtWidgets import QApplication
from src.GUI import GUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = GUI()
    sys.exit(app.exec())
