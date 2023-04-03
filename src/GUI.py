import datetime
import socket

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, \
    QFileDialog, QComboBox
from PyQt6.QtGui import QIcon, QFont, QColor, QTextCursor
from PyQt6.QtCore import Qt, QTimer

from ISC_protocol import IscProtocol
from TCP_client import TCPClient


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.client_socket = socket.socket()
        self.init_gui()
        TCPClient.server_connection(self)
        self.reception_timer()

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
        app_name = QLabel('Yepzhapp')
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

        # Add a "encryption" button
        self.encrypt_button = QPushButton()
        self.encrypt_button.setText('Encrypt')
        self.encrypt_button.clicked.connect(self.encrypt_box)
        vbox.addWidget(self.encrypt_button)

        # Add the horizontal layout to the vertical layout
        vbox.addLayout(hbox)

        # Show the window
        self.show()

    def encrypt_box(self):
        box = QVBoxLayout()
        text = QLabel('Select an encryption method')
        text_font = QFont('Arial', 14)
        text.setFont(text_font)
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        box.addWidget(text)

        encryption_methods = ["Shift", "Vigenere", "RSA"]
        self.encrypt_box = QComboBox()
        self.encrypt_box.addItems(encryption_methods)
        shift_button_font = QFont('Arial', 14)
        self.encrypt_box.show()


    def send_image(self):
        message = QFileDialog.getOpenFileName(self, 'Open image', 'c:\\', "Image files (*.png *.gif)")
        TCPClient.send_message_server(self, message)

    def send_message(self):
        # Get the message from the type box
        message = self.type_box.text()

        # Sends message
        if message == '':
            pass
        else:
            TCPClient.send_message_server(self, message)

            # Add the message to the message box
            message_font = QFont('Arial', 14)
            message_color = QColor(255, 255, 255)
            time = datetime.datetime.now().strftime("%d-%m-%Y (%H:%M:%S)")
            self.msg_box.setTextColor(message_color)
            self.msg_box.setFont(message_font)
            self.msg_box.append(f'{time} - You : {message}')

        # Clear the type box once a message is sent
        self.type_box.clear()

    def response_message(self):
        # Move the cursor to the end of the message box
        self.msg_box.moveCursor(QTextCursor.MoveOperation.End)

        # Response message
        try:
            response = IscProtocol.dec_msg(self.client_socket.recv(1024))

            response_font = QFont('Arial', 14)
            response_color = QColor(50, 200, 50)
            time = datetime.datetime.now().strftime("%d-%m-%Y (%H:%M:%S)")
            self.msg_box.setTextColor(response_color)
            self.msg_box.setFont(response_font)
            self.msg_box.append(f'{time} - Server: {response}')

            # Move the cursor to the end of the message box
            self.msg_box.moveCursor(QTextCursor.MoveOperation.End)
        except socket.timeout:
            pass

    def reception_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.response_message)
        self.timer.start(250)
