import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QTabWidget, QTableWidgetItem, QWidget, QTextEdit, QPushButton, QVBoxLayout
from PyQt6 import uic


class AdminMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/adminMenu.ui', self)
        self.setWindowTitle('Меню администратора')
        








