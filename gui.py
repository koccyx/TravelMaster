import sys
from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)
# dlgMain = QMainWindow()
# dlgMain.setWindowTitle('Travel tool')
# dlgMain.show()

# app.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HI')

        self.button = QPushButton('Seee this')

        self.button.setFixedSize(100, 40)

        # self.setFixedSize(500, 400)
        self.resize(300, 400)

        self.button.move(100, 30)

        self.setCentralWidget(self.button)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()







if __name__ == '__main__':
    main()





