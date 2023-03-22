import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from GUI import GUI, open_open_program
from TCP_client import client_program

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = GUI()

    # timer which repate function `display_time` every 1000ms (1s)
    timer = QTimer()
    timer.timeout.connect(client_program())  # execute `display_time`
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    timer2 = QTimer()
    timer2.timeout.connect(open_open_program())  # execute `display_time`
    timer2.setInterval(5000)  # 1000ms = 1s
    timer2.start()

    sys.exit(app.exec())
