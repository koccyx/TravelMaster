import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HI')

        self.button = QPushButton('Seee this')

        self.button.setFixedSize(100, 40)

        self.resize(300, 400)

        self.button.move(100, 30)

        self.setCentralWidget(self.button)





