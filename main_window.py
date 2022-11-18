import sys
import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QWidget,
                             QFileDialog, QMessageBox, QDesktopWidget, QVBoxLayout)
from PyQt5.QtGui import QPixmap

from Lab_2_5 import Iterator_1
from Lab_2_1 import create_csv
from Lab_2_2 import copy_dataset


class Window(QWidget):

    def __init__(self) -> None:
        '''Constructor'''
        super().__init__()

        self.start_menu()

    def start_menu(self) -> None:
        '''The program asks you to select a folder with the source dataset'''
        self.center()

        text = "Нажмите, чтобы выбрать нужную папку с ИСХОДНЫМ датасетом"
        self.dir_btn = QPushButton(text, self)
        self.dir_btn.setStyleSheet("font-size: 20px")
        self.hbox = QVBoxLayout()
        self.hbox.addWidget(self.dir_btn)
        self.setLayout(self.hbox)

        self.dir_btn.clicked.connect(self.input_path)

        self.setWindowTitle('Лабораторная работа №3')

    def center(self) -> None:
        '''Window centering'''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def input_path(self) -> None:
        '''Checking the selected folder'''
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self)
        text = "Вы выбрали не ту папку. Выберите папку с исходным датасетом"
        if self.folderpath == "":
            return

        if self.folderpath[-7:] != "dataset":
            self.exception(text)
            return
        
        dir_cont = os.listdir(self.folderpath)
        if "cat" not in dir_cont or "dog" not in dir_cont:
            self.exception(text)
            return

        self.general_menu()

    def general_menu(self) -> None:
        '''Main menu'''
        self.dir_btn.deleteLater()

        self.it_cat = Iterator_1(self.folderpath, "cat")
        self.it_dog = Iterator_1(self.folderpath, "dog")

        self.lbl = QLabel(self)
        self.next_cat()

        next_cat_btn = QPushButton("Следующий кот")
        next_dog_btn = QPushButton("Следующая собака")
        next_cat_btn.setStyleSheet("font-size: 20px")
        next_dog_btn.setStyleSheet("font-size: 20px")

        gen_text = "Создать папку и файл-аннотацию к ней"
        text_btn_task_2 = " (фото имеет имя: класс_номер)"
        text_btn_task_3 = " (фото имеет имя: рандомное число от 0 до 10000)"
        btn_task_1 = QPushButton("Создать файл-аннотацию этого датасета")
        btn_task_2 = QPushButton(gen_text + text_btn_task_2)
        btn_task_3 = QPushButton(gen_text + text_btn_task_3)

        self.hbox.addWidget(btn_task_1)
        self.hbox.addWidget(btn_task_2)
        self.hbox.addWidget(btn_task_3)
        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(next_cat_btn)
        self.hbox.addWidget(next_dog_btn)
        self.setLayout(self.hbox)

        btn_task_1.clicked.connect(self.do_task_1)
        btn_task_2.clicked.connect(self.do_task_2)
        #btn_task_3.clicked.connect(self.do_task_3)
        next_cat_btn.clicked.connect(self.next_cat)
        next_dog_btn.clicked.connect(self.next_dog)

    def next_cat(self) -> None:
        '''Taking the next picture from the "cat" folder'''
        try:
            self.lbl.setPixmap(QPixmap(next(self.it_cat)))
            self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        except:
            self.exception("Всё, картинок с котами больше нет )=")

    def next_dog(self) -> None:
        '''Taking the next picture from the "dog" folder'''
        try:
            self.lbl.setPixmap(QPixmap(next(self.it_dog)))
            self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        except:
            self.exception("Всё, картинок с собаками больше нет )=")

    def do_task_1(self) -> None:
        '''Completion of point 1 from laboratory No. 2'''
        path = QFileDialog.getSaveFileName(self, "" , "annotation" , "CSV (*.csv)")[0]
        if path == "":
            return
        create_csv(path, self.folderpath, "cat")
        create_csv(path, self.folderpath, "dog")

    def do_task_2(self) -> None:
        '''Completion of point 2 from laboratory No. 2'''
        path = QFileDialog.getExistingDirectory(self)
        if path == "":
            return
        copy_dataset(self.folderpath, path, "cat")
        copy_dataset(self.folderpath, path, "dog")
        csv = os.path.join(path, "annotation.csv")
        create_csv(csv, path, "")

    def exception(self, text: str) -> None:
        '''Warning window'''
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(text)
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