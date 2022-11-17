from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtWidgets import QMenuBar, QMenu, QFileDialog, QMessageBox, QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont

from Lab_2_5 import Iterator_1

import sys
import os

class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self) -> None:

        self.resize(1200, 800)
        self.center()

        text = "Нажмите, чтобы выбрать нужную папку с ИСХОДНЫМ датасетом"
        self.dir_btn = QPushButton(text, self)
        self.dir_btn.setStyleSheet("font-size: 20px")
        self.hbox = QVBoxLayout()
        self.hbox.addWidget(self.dir_btn)
        self.setLayout(self.hbox)

        self.dir_btn.clicked.connect(self.input_path)

        self.setWindowTitle('Лабораторная работа №3')

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def input_path(self) -> None:

        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self)
        if self.folderpath == "":
            return

        if self.folderpath[-7:] != "dataset":
            self.exception()
            return
        
        dir_cont = os.listdir(self.folderpath)
        if "cat" not in dir_cont or "dog" not in dir_cont:
            self.exception()
            return

        self.general_menu()

    def general_menu(self) -> None:

        self.dir_btn.deleteLater()

        self.it_cat = Iterator_1(self.folderpath, "cat")
        self.it_dog = Iterator_1(self.folderpath, "dog")

        self.lbl = QLabel(self)
        self.next_cat()

        next_cat_btn = QPushButton("Следующий кот")
        next_dog_btn = QPushButton("Следующая собака")
        next_cat_btn.setStyleSheet("font-size: 20px")
        next_dog_btn.setStyleSheet("font-size: 20px")

        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(next_cat_btn)
        self.hbox.addWidget(next_dog_btn)
        self.setLayout(self.hbox)

        next_cat_btn.clicked.connect(self.next_cat)
        next_dog_btn.clicked.connect(self.next_dog)

    def next_cat(self) -> None:

        self.lbl.setPixmap(QPixmap(next(self.it_cat)))
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)

    def next_dog(self) -> None:

        self.lbl.setPixmap(QPixmap(next(self.it_dog)))
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)

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