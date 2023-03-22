import sys
import socket
import datetime

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, \
    QFileDialog
from PyQt6.QtGui import QIcon, QFont, QColor, QTextCursor
from PyQt6.QtCore import Qt

from src.ISC_protocol import IscProtocol


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_gui()

        # Socket connection
        host = "153.109.124.198"
        port = 6000  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((host, port))  # connect to the server
        print('---------------------------\n| Connected to the server |\n---------------------------')

    def init_gui(self):

        # Colors
        window_color = 'background-color: lightgrey;'
        msg_box_color = 'background-color: grey;'
        type_box_color = 'background-color: grey;'

        # Set up the main window
        self.setWindowTitle('Chat App')
        self.setStyleSheet(window_color)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('res/icon.png'))

        # Set up the layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.setLayout(vbox)

        # Add a label for the app name
        app_name = QLabel('Yep')
        app_name_font = QFont('Arial', 24)
        app_name.setFont(app_name_font)
        app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(app_name)

        # Add a text box for messages
        self.msg_box = QTextEdit()
        msg_box_font = QFont('Arial', 14)
        self.msg_box.setFont(msg_box_font)
        self.msg_box.setReadOnly(True)
        self.msg_box.setTextColor(QColor(0, 128, 0))
        vbox.addWidget(self.msg_box)
        self.msg_box.setStyleSheet(msg_box_color)

        # Add a text box for typing messages
        self.type_box = QLineEdit()
        type_box_font = QFont('Arial', 14)
        self.type_box.setFont(type_box_font)
        self.type_box.returnPressed.connect(self.send_message)
        hbox.addWidget(self.type_box)
        self.type_box.setStyleSheet(type_box_color)

        # Add a "send" button
        self.send_button = QPushButton(QIcon('res/send.png'), '')
        self.send_button.setStyleSheet('background-color: lightgrey; border: none;')
        self.send_button.clicked.connect(self.send_message)
        hbox.addWidget(self.send_button)

        # Add a "open file" button
        self.open_file_button = QPushButton(QIcon('res/sendimg.png'), '')
        self.open_file_button.setStyleSheet('background-color: lightgrey; border: none;')
        self.open_file_button.clicked.connect(self.send_image)
        hbox.addWidget(self.open_file_button)

        # Add the horizontal layout to the vertical layout
        vbox.addLayout(hbox)

        # Show the window
        self.show()

    def send_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open image', 'c:\\', "Image files (*.png *.gif)")

    def send_message(self):
        # Get actual time
        time = datetime.datetime.now().strftime("%d-%m-%Y (%H:%M:%S)")

        # Get the message from the type box
        message = self.type_box.text()

        # Sends message
        encoded_message = IscProtocol.enc_msg(message)  # encodes message with "ISCP"
        self.client_socket.send(encoded_message)    # send message

        # Add the message to the message box
        message_font = QFont('Arial', 14)
        message_color = QColor(255, 255, 255)
        self.msg_box.setTextColor(message_color)
        self.msg_box.setFont(message_font)
        if message == '':
            pass
        else:
            self.msg_box.append(f'{time} - You : {message}')

        # Clear the type box once a message is sent
        self.type_box.clear()

        # Move the cursor to the end of the message box
        self.msg_box.moveCursor(QTextCursor.MoveOperation.End)

        # Response message
        response = IscProtocol.dec_msg(self.client_socket.recv(1024))
        response_font = QFont('Arial', 14)
        response_color = QColor(50, 200, 50)

        self.msg_box.setTextColor(response_color)
        self.msg_box.setFont(response_font)

        if response == message:
            self.msg_box.append('Same')
        else:
            self.msg_box.append(f'{time} - Someone: {response}')

        # Move the cursor to the end of the message box
        self.msg_box.moveCursor(QTextCursor.MoveOperation.End)


def open_open_program():
    app = QApplication(sys.argv)
    chat_app = GUI()
    sys.exit(app.exec())


if __name__ == '__main__':
    open_open_program()
