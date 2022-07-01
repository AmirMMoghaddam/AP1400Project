from logging.config import listen
import os
from textwrap import indent
from time import time
import PyQt5
import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
from FinalMaker import *
from genartor import *
import random
import copy

# اینجا باید اینو باز کنیم ببینیم طرف چی انتخاب کرده بعد ببندیم بعدیو باز  کنیم
Form = uic.loadUiType(os.path.join(os.getcwd(), "project.ui"))[0]
# self.pushButton_biginner.connect()
# self.pushButton_medium.connect()
# self.pushButton_hard.connect()
# اینا باید تو کلاس تعریف بشن ولی نمیدونم چجوری برا همین اینجا نوشتم

#Form = uic.loadUiType(os.path.join(os.getcwd(), "proj.ui"))[0]


class IntroWindow(QMainWindow, Form):
    def __init__(self, Puzzle, Sulution):
        super(IntroWindow, self).__init__()
        self.setupUi(self)
        self.puzzle = Puzzle
        self.hintcount = 0
        self.sul = Sulution
        self.untaken = list(range(1, 82))
        self.index = 0
        self.Fill()
        self.hint.clicked.connect(self.sayhint)
        self.quit.clicked.connect(lambda: app.quit())
        self.text_time.setText(f"{time()/1000000}ms")
        #   به جای این که خیلی اشغاله میتونیم از ال سی دی استفاده کنیم به نظرت هرچی بهتره
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLCDNumber.html

        # تو کدت اونجایی که خونه ها تعریف میشن چی باشن اینو ست تکست کن کن
        # self.text_xy.textChanged.connect(self.textchange)
        #self.progressBar.setRange(maximum, minimum)
        # self.progressBar.valueChanged()

      # برای اینکه نشون بده چند درصدش کامل شده اینجا درصد میدی نشون میده

    def Fill(self):
        Palette = QtGui.QPalette()
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    self.index = [i, j]
                    self.untaken.remove(self.indexCoding())
                    getattr(self, "lineEdit_"+str(i)+"_" +
                            str(j)).setText(str(self.puzzle[i][j]))
                    getattr(self, "lineEdit_"+str(i)+"_"+str(j)
                            ).setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setPalette(Palette)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setReadOnly(True)
                else:
                    getattr(self, "lineEdit_"+str(i)+"_"+str(j)).setText('')
                    getattr(self, "lineEdit_"+str(i)+"_"+str(j)
                            ).setFont(QtGui.QFont("Times", weight=QtGui.QFont.Normal))
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.blue)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setPalette(Palette)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setReadOnly(False)

    def indexDecoding(self, numb):
        a = 0
        number = numb
        while number > 9:
            number = number - 9
            a += 1
        return [a, number - 1]

    def indexCoding(self):
        row = self.index[0]
        col = self.index[1]
        return (row*9) + col + 1

    def GetUntakenIndex(self):
        a = random.choice(self.untaken)
        self.index = self.indexDecoding(a)
        self.untaken.remove(a)

    def sayhint(self):
        Palette = QtGui.QPalette()
        if self.hintcount == 3:
            self.showMessageBox
        else:
            self.GetUntakenIndex()
            i = self.index[0]
            j = self.index[1]
            getattr(self, "lineEdit_"+str(i)+"_" + str(j)
                    ).setText(str(self.sul[i][j]))
            getattr(self, "lineEdit_"+str(i)+"_"+str(j)
                    ).setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
            Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.blue)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setPalette(Palette)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setReadOnly(True)
            self.hintcount += 1

    def textchange(self):
        # اینجا باید یه مشت ایف بزنی چک کنه ببینه درسته یا نه
        pass
    # کد رو نوشتی passهارو بردار

    def showMessageBox(self):
        QtGui.QMessageBox.information(self, "You have used Your 3 hints")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    starter = []
    for i in range(0, 9):
        starter.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    b = create(starter)
    print("Created")
    c = copy.deepcopy(b)
    puzz = start(c, 20)
    print("Started")
    w = IntroWindow(puzz, b)
    w.show()
    sys.exit(app.exec_())
