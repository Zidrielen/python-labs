from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMenuBar, QMenu, QFileDialog, QMessageBox

import sys
import os
from typing import Optional

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Лабораторная работа №3")
        self.setGeometry(150, 200, 1000, 600)

        self.main_text = QtWidgets.QLabel(self)
        text = "В 'Файл' нажмите 'Открыть', чтобы выбрать папку с исходным датасетом."
        self.main_text.setText(text)
        self.main_text.setStyleSheet("font-size: 20px")
        self.main_text.move(160, 270)
        self.main_text.adjustSize()

        self.createMenuBar()
    
    def createMenuBar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)
        self.menu_bar.addMenu(file_menu)

        file_menu.addAction("Открыть", self.check_dir)

    def check_dir(self) -> None:
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self)
        if folderpath == "":
            return

        if folderpath[-7:] != "dataset":
            self.exception()
            return
        
        dir_cont = os.listdir(folderpath)
        if "cat" not in dir_cont or "dog" not in dir_cont:
            self.exception()
            return


    def exception(self) -> None:
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Вы выбрали не исходный датасет.")
        error.setStyleSheet("font-size: 12px")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.setDefaultButton(QMessageBox.Ok)

        error.exec_()


def application() -> None:
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())