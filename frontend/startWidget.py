import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from registretionOrLogin import RegistrationOrLogin
from adminPanel import AdminMenu

class myApp(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('frontend/ui/check.ui', self)
        self.setWindowTitle('Вид работы c программой')


        self.userButton.clicked.connect(self.__openRoLWindow)
        self.adminButton.clicked.connect(self.__openAdminPanel)

    def __openRoLWindow(self):
        self.registrationWidget = RegistrationOrLogin()
        self.registrationWidget.show()
        self.close()

    def __openAdminPanel(self):
        self.adminWidget = AdminMenu()
        self.adminWidget.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet("""
    QLineEdit
    {
        background-color: #5b586e;
        border-radius: 10px;
        padding: 5px;
        border: 1px solid #5b586e;
        color: #fff;
    }

    QPushButton
    {
        background-color: #0d6efd;
        border: 1px solid #343155;
        color: #fff;
        padding: 3px 0;
        margin-top: 10px;
        border-radius: 8px;
    }

    QPushButton:hover,
    QPushButton:clicked
    {
        background-color: #0b5ed7;
        border: 1px solid #9ac3fe;
    }

    QTimeEdit
    {
        background-color: #5b586e;
        border-radius: 10px;
        padding: 5px;
        border: 1px solid #5b586e;
        color: #fff;
    }

    QDateEdit
    {
        background-color: #5b586e;
        border-radius: 10px;
        padding: 5px;
        border: 1px solid #5b586e;
        color: #fff;
    }

    QComboBox
    {
        background-color: #5b586e;
        border-radius: 10px;
        padding: 5px;
        border: 1px solid #5b586e;
        color: #fff;
    }
    """)

    newApp = myApp()
    newApp.show()

    sys.exit(app.exec())


