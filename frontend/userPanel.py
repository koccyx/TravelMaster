import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.base import Base
from backend.user import User
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class UserMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/userMenu.ui', self)
        self.setWindowTitle('Меню пользователя')

        for i in range(6):
            self.ticketTable.setColumnWidth(i,130)

        self.base = Base('backend/data/tickets.xlsx')




