import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6 import QtWidgets
import datetime
import time

from PyQt6.QtWidgets import QApplication

from src.GUI import GUI, open_open_program
from src.TCP_client import client_program

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = GUI()

    # timer which repate function `display_time` every 1000ms (1s)
    timer = QTimer()
    timer.timeout.connect(open_open_program())  # execute `display_time`
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    sys.exit(app.exec())
