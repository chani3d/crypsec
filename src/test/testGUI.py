import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6 import QtWidgets
import datetime
import time


def display_time():

    current_time = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
    label.setText(current_time)

    print('current_time:', current_time)


def long_job():
    for x in range(10):
        print('Job:', x)
        time.sleep(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # some GUI in window
    label = QtWidgets.QLabel('Title')
    window.setCentralWidget(label)
    window.show()

    # timer which repate function `display_time` every 1000ms (1s)
    timer = QTimer()
    timer.timeout.connect(display_time)  # execute `display_time`
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    timer2 = QTimer()
    timer2.timeout.connect(long_job)  # execute `display_time`
    timer2.setInterval(1000)  # 1000ms = 1s
    timer2.start()

    sys.exit(app.exec())