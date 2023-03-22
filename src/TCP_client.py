import socket
import sys

from PyQt6.QtWidgets import QApplication

from ISC_protocol import IscProtocol


def client_program():
    host = "153.109.124.198"
    port = 6000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print('---------------------------\n| Connected to the server |\n---------------------------')

    message = input(' -> ')  # take input

    while message.lower().strip() != 'bye':
        encoded_message = IscProtocol.enc_msg(message)  # encodes message with "ISCP"
        client_socket.send(encoded_message)  # send message
        data = IscProtocol.dec_msg(client_socket.recv(1024))  # decodes response with "ISCP"

        print('Received from server: ' + data)  # show in terminal

        message = input(' -> ')  # take input again

    client_socket.close()  # close the connection

    if message == 'bye':
        print('--------------------------------\n| Disconnected from the server |\n--------------------------------')


if __name__ == '__main__':
    client_program()

# print(IscProtocol.message("Hello"))
