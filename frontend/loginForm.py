import sys
import os
from PyQt6.QtWidgets import  QWidget, QLineEdit
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from backend.user import User
from backend.userBase import UserBase
from userPanel import UserMenu
from changePassword import ChangePassword
from forgotPassword import ForgotPassword





class LoginFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/LoginForm.ui', self)
        self.setWindowTitle('Вход')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.inputButton.clicked.connect(self.__checkLogin)
        self.forgotPasswordButton.clicked.connect(self.__forgotPasswordButtonClicked)
        self.changePasswordButton.clicked.connect(self.__changePasswordButtonClicked)
        self.backButton.clicked.connect(self.__goBack)

    def __goBack(self):
        from registretionOrLogin import RegistrationOrLogin
        self.backWidget = RegistrationOrLogin()
        self.backWidget.show()
        self.close()

    def __changePasswordButtonClicked(self):
        self.changePasswordWidget = ChangePassword()
        self.changePasswordWidget.show()

    def __forgotPasswordButtonClicked(self):
        self.forgotPasswordWidget = ForgotPassword()
        self.forgotPasswordWidget.show()

    def __openUserPanel(self, user):
        self.userPanel = UserMenu(user)
        self.userPanel.show()
        self.close()

    def __checkLogin(self):

        tempBase = UserBase()

        for user in tempBase.showBaseDict():
            if str(user['login']) == str(self.loginInput.text()) and str(user['Пароль']) == str(self.passwordInput.text()):
                self.errorLabel1.setText('Отлично')
                self.errorLabel2.setText('')
                for tempUser in tempBase.objecBase:
                    if str(tempUser.login) == str(user['login']) and str(tempUser.password) == str(user['Пароль']):
                        self.__openUserPanel(tempUser)
                return
            elif str(user['login']) == str(self.loginInput.text()) and str(user['Пароль']) != str(self.passwordInput.text()):
                self.errorLabel1.setText('Вы ввели')
                self.errorLabel2.setText('неправильный пароль')
                return
            else:
                self.errorLabel1.setText('Нет пользователя')
                self.errorLabel2.setText('с таким именем')




