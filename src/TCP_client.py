import socket
import sys

from PyQt6.QtWidgets import QApplication

from ISC_protocol import IscProtocol


def client_program():

    host = "153.109.124.198"
    port = 6000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        encodedMessage = IscProtocol.encmsg(message)  # using ISC Protocol
        client_socket.send(encodedMessage)  # send message
        data = IscProtocol.decmsg(client_socket.recv(4))  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

# print(IscProtocol.message("Hello"))
