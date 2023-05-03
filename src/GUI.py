import datetime
import socket

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, \
    QFileDialog, QComboBox, QGroupBox, QRadioButton
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

        # Main window
        self.setWindowTitle('Yepzhapp | SJCG - ISC 2023')
        self.setStyleSheet(window_color)
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon('res/icon.png'))

        # Layout
        poppabox = QGridLayout()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        # self.setLayout(vbox)
        self.setLayout(poppabox)

        # Add a label for the app name
        app_name = QLabel('Yepzhapp')
        app_name_font = QFont('Arial', 24)
        app_name.setFont(app_name_font)
        app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(app_name, 0, 0, 1, 5) # Adds the widget at position 0x0 and occupies 1 row and 5 columns

        # Add a text box for messages
        self.msg_box = QTextEdit()
        msg_box_font = QFont('Arial', 14)
        self.msg_box.setFont(msg_box_font)
        self.msg_box.setReadOnly(True)
        self.msg_box.setTextColor(QColor(0, 128, 0))
        vbox.addWidget(self.msg_box)
        poppabox.addLayout(vbox, 1, 0, 50, 1) # Adds the widget at position 1x0 and occupies 15 rows and 1 column
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


        # Add a box for encryption options
        self.encr_box_title = QLabel("Encryption methods")
        encr_box_font = QFont('Arial', 18)
        self.encr_box_title.setFont(encr_box_font)
        self.encr_box_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(self.encr_box_title, 1, 1)

        # Shift 
        self.shift = QGroupBox(str("Shift"))
        self.shift.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(self.shift, 2, 1, 4, 1)

        self.shift_key = QLineEdit(str("Enter a key"))
        poppabox.addWidget(self.shift_key, 3, 1)

        self.shifted = QLineEdit(str("Shifted text"))
        poppabox.addWidget(self.shifted, 4, 1)

        # Connects the boxes in case something has changed
        self.type_box.textChanged.connect(self.shift_update)
        self.shift_key.textChanged.connect(self.shift_update)

        # Vigenere cipher
        self.vgnr = QGroupBox(str("Vigenere cipher"))
        self.vgnr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(self.vgnr, 6, 1, 5, 1)

        self.vgnr_key = QLineEdit(str("Enter a key"))
        poppabox.addWidget(self.vgnr_key, 7, 1)
        
        self.encrypted_vgnr = QLineEdit(str("Encrypted"))
        poppabox.addWidget(self.encrypted_vgnr, 8, 1)

        self.decrypted_vgnr = QLineEdit(str("Decrypted"))
        poppabox.addWidget(self.decrypted_vgnr, 9, 1)

        self.type_box.textChanged.connect(self.vgnr_update)
        self.shift_key.textChanged.connect(self.vgnr_update)

        # RSA
        self.rsa = QGroupBox(str("RSA"))
        self.rsa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(self.rsa, 11, 1, 5, 1)

        # Hash
        self.hash = QGroupBox(str("Hash"))
        self.hash.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(self.hash, 21, 1, 5, 1)

        self.hash_msg_box = QLineEdit()
        poppabox.addWidget(self.hash_msg_box, 22, 1)

        self.type_box.textChanged.connect(self.hash_update)
        
        # Diffie-Hellman
        self.diffie_hellman = QGroupBox(str("Diffie-Hellman"))
        self.diffie_hellman.setAlignment(Qt.AlignmentFlag.AlignCenter)
        poppabox.addWidget(self.diffie_hellman, 23, 1)

        # Add the horizontal layout to the vertical layout
        vbox.addLayout(hbox)

        # Show the window
        self.show()

    def shift_update(self):
        msg = self.type_box.text()
        string_key = self.shift_key.text()

        # Check if the box is only numeric
        if string_key.isnumeric():
            key = int(string_key)
        else:
            key = 0

        text = IscProtocol.shift(msg, key)
        self.shifted.setText(text)
       
    def vgnr_update(self):
        msg = self.type_box.text()
        key = self.vgnr_key.text()

        enc_text = IscProtocol.enc_vgnr(msg, key)
        self.encrypted_vgnr.setText(enc_text)

        dec_text = IscProtocol.dec_vgnr(msg, key)
        self.decrypted_vgnr.setText(dec_text)

    def hash_update(self):
        text = IscProtocol.enc_hash(self.type_box.text())
        self.hash_msg_box.setText(text)

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
