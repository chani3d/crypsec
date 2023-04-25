import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QMessageBox
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from string import ascii_lowercase, ascii_uppercase

class MessageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the UI elements
        self.encrypt_label = QLabel('Encrypt')
        self.decrypt_label = QLabel('Decrypt')
        self.encrypt_text = QTextEdit()
        self.decrypt_text = QTextEdit()
        self.caesar_shift = QLineEdit()
        self.vigenere_key = QLineEdit()
        self.rsa_key = QLineEdit()
        self.caesar_button = QPushButton('Caesar Cipher')
        self.vigenere_button = QPushButton('Shift Vigenere')
        self.rsa_button = QPushButton('RSA')

        # Set the layout
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.encrypt_label)
        vbox1.addWidget(self.encrypt_text)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('Caesar Shift:'))
        hbox1.addWidget(self.caesar_shift)
        vbox1.addLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('Vigenere Key:'))
        hbox2.addWidget(self.vigenere_key)
        vbox1.addLayout(hbox2)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel('RSA Key:'))
        hbox3.addWidget(self.rsa_key)
        vbox1.addLayout(hbox3)
        vbox1.addWidget(self.caesar_button)
        vbox1.addWidget(self.vigenere_button)
        vbox1.addWidget(self.rsa_button)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.decrypt_label)
        vbox2.addWidget(self.decrypt_text)
        hbox4 = QHBoxLayout()
        hbox4.addLayout(vbox1)
        hbox4.addLayout(vbox2)
        self.setLayout(hbox4)

        # Connect the buttons to their respective functions
        self.caesar_button.clicked.connect(self.caesar_cipher)
        self.vigenere_button.clicked.connect(self.vigenere_cipher)
        self.rsa_button.clicked.connect(self.rsa_cipher)

        # Set the window properties
        self.setWindowTitle('Message Encryption')
        self.setGeometry(300, 300, 600, 400)
        self.show()

    def caesar_cipher(self):
        message = self.encrypt_text.toPlainText()
        shift = int(self.caesar_shift.text())
        encrypted_message = ''
        for char in message:
            if char in ascii_lowercase:
                encrypted_message += ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]
            elif char in ascii_uppercase:
                encrypted_message += ascii_uppercase[(ascii_uppercase.index(char) + shift) % 26]
            else:
                encrypted_message += char
        self.decrypt_text.setPlainText(encrypted_message)

    def vigenere_cipher(self):
        message = self.encrypt_text.toPlainText()
        key = self.vigenere_key.text()
        key_len = len(key)
        key_ints

