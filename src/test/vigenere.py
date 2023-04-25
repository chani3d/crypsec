

#Shift (implemented in ISC_protocol)

# def shifenc(originalstring, key):
#     cryptedstring = ''
#
#     for element in originalstring:
#         cryptedstring += chr(ord(element) + key)
#     
#     return cryptedstring
#
#
# #Vigenere
#
# def vigenc(originalstring):
#     for element in 
#     pass
#
# def vigdenc():
#     pass
#
# letter = 'Ak'
# orden = (ord(letter))
# print(orden)



import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Grid Example')

        # Create a grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Add widgets to the grid
        label1 = QLabel('0x0')
        grid.addWidget(label1, 0, 0)

        label2 = QLabel('0x1')
        grid.addWidget(label2, 0, 1)

        label3 = QLabel('0x2')
        grid.addWidget(label3, 0, 2)

        label4 = QLabel('0x3')
        grid.addWidget(label4, 0, 3)

        label5 = QLabel('1x0')
        grid.addWidget(label5, 1, 0)

        label6 = QLabel('1x1')
        grid.addWidget(label6, 1, 1)

        label7 = QLabel('1x2')
        grid.addWidget(label7, 1, 2)

        label8 = QLabel('1x3')
        grid.addWidget(label8, 1, 3)

        label9 = QLabel('2x0')
        grid.addWidget(label9, 2, 0)

        label10 = QLabel('2x1')
        grid.addWidget(label10, 2, 1)

        label11 = QLabel('2x2')
        grid.addWidget(label11, 2, 2)

        label12 = QLabel('2x3')
        grid.addWidget(label12, 2, 3)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())



