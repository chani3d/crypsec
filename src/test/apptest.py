
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QMessageBox
from random import randint
from math import gcd

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
        self.rsa_public_key = QLineEdit()
        self.rsa_private_key = QLineEdit()
        self.caesar_button = QPushButton('Caesar Cipher')
        self.vigenere_button = QPushButton('Shift Vigenere')
        self.rsa_generate_button = QPushButton('Generate Keys')
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
        hbox3.addWidget(QLabel('RSA Public Key:'))
        hbox3.addWidget(self.rsa_public_key)
        vbox1.addLayout(hbox3)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(QLabel('RSA Private Key:'))
        hbox4.addWidget(self.rsa_private_key)
        vbox1.addLayout(hbox4)
        vbox1.addWidget(self.rsa_generate_button)
        vbox1.addWidget(self.rsa_button)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.decrypt_label)
        vbox2.addWidget(self.decrypt_text)
        hbox5 = QHBoxLayout()
        hbox5.addLayout(vbox1)
        hbox5.addLayout(vbox2)
        self.setLayout(hbox5)

        # Connect the buttons to their respective functions
        self.caesar_button.clicked.connect(self.caesar_cipher)
        self.vigenere_button.clicked.connect(self.vigenere_cipher)
        self.rsa_generate_button.clicked.connect(self.generate_rsa_keys)
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
            if char.isalpha():
                if char.islower():
                    encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_message += char
        self.decrypt_text.setPlainText(encrypted_message)

    def vigenere_cipher(self):
        pass

