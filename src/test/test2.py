import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import socket


class ClientThread(QThread):
    new_message = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 10000)
        client_socket.connect(server_address)

        while self.running:
            message = client_socket.recv(1024).decode()
            self.new_message.emit(message)

        client_socket.close()

    def stop(self):
        self.running = False


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat App')
        self.setGeometry(100, 100, 400, 400)

        self.message_history = QTextEdit()
        self.message_history.setReadOnly(True)

        self.message_input = QLineEdit()
        self.message_input.returnPressed.connect(self.send_message)

        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.message_history)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.client_thread = ClientThread()
        self.client_thread.new_message.connect(self.add_message)
        self.client_thread.start()

    @pyqtSlot(str)
    def add_message(self, message):
        self.message_history.append(message)

    def send_message(self):
        message = self.message_input.text()
        if message:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('localhost', 10000)
            client_socket.connect(server_address)
            client_socket.send(message.encode())
            client_socket.close()
            self.message_input.clear()

    def closeEvent(self, event):
        self.client_thread.stop()
        self.client_thread.wait()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec())
