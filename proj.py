import os
from time import sleep, time
from tkinter import N
import PyQt5
import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.pyplot import text
from FinalMaker import *
from genartor import *
import random
import copy

# اینجا باید اینو باز کنیم ببینیم طرف چی انتخاب کرده بعد ببندیم بعدیو باز  کنیم
Form = uic.loadUiType(os.path.join(os.getcwd(), "project.ui"))[0]

# اینا باید تو کلاس تعریف بشن ولی نمیدونم چجوری برا همین اینجا نوشتم

FormM = uic.loadUiType(os.path.join(os.getcwd(), "projectmain.ui"))[0]


class MainWindow(QMainWindow, FormM):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_biginner.clicked.connect(Game)
        self.pushButton_medium.clicked.connect(Game)
        self.pushButton_hard.clicked.connect(Game)


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
        self.values = 0
        self.hint.clicked.connect(self.sayhint)
        self.quit.clicked.connect(lambda: app.quit())
        self.checkbutton.clicked.connect(self.CheckAwnser)
        self.clearbutton.clicked.connect(self.Clear)
        self.resetbutton.clicked.connect(self.Reset)
        self.text_time.setText(f"{time()/1000}ms")

        #   به جای این که خیلی اشغاله میتونیم از ال سی دی استفاده کنیم به نظرت هرچی بهتره
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLCDNumber.html

        # تو کدت اونجایی که خونه ها تعریف میشن چی باشن اینو ست تکست کن کن
        # self.text_xy.textChanged.connect(self.textchange)
        # self.progressBar.setRange(maximum, minimum)
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
                    sleep(0.01)
                else:
                    getattr(self, "lineEdit_"+str(i)+"_" +
                            str(j)).setText('')
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
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
            Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setPalette(Palette)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setReadOnly(True)
            self.hintcount += 1

    def Clear(self):
        for i in self.untaken:
            [i, j] = self.indexDecoding(i)
            a = getattr(self, "lineEdit_"+str(i) + "_"+str(j)).clear()

    def Reset(self):
        self.untaken = list(range(1, 82))
        starter = []
        for i in range(0, 9):
            starter.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        b = create(starter)
        print("Created")
        self.sul = b
        c = copy.deepcopy(b)
        self.puzzle = start(c, 20)
        print("Started")
        self.Fill()

    def CheckAwnser(self):
        Palette = QtGui.QPalette()
        for i in self.untaken:
            [i, j] = self.indexDecoding(i)
            a = getattr(self, "lineEdit_"+str(i) + "_"+str(j)).text()
            self.values = [i, j]
            b = int(a)
            if self.checkwSul(i, j, b):
                print(f"checked [ {i} , {j} ]")
                Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setPalette(Palette)
            else:
                Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setPalette(Palette)

    def changed(self):
        for i in self.untaken:
            [i, j] = self.indexDecoding(i)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).clear()
            self.values = [i, j]
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)
                    ).returnPressed.connect(getattr(self.textchange))

    def checkwSul(self, i, j, val):
        if val == self.sul[i][j]:
            return True
        else:
            return False

    def textchange(self):

        Palette = QtGui.QPalette()
        # اینجا باید یه مشت ایف بزنی چک کنه ببینه درسته یا نه
        [i, j] = self.values
        a = getattr(self, "lineEdit_"+str(i) + "_"+str(j)).displayText()
        print(f"[ {i} , {j}]")
        getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setText("0")
        print(str(a))
        self.puzzle[i][j] = a
        if self.check_row(a) and self.check_colum(a) and self.check_box(a):
            Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setPalette(Palette)

    # کد رو نوشتی passهارو بردار

    def check_row(self, val):
        row = self.values[0]
        Row = self.puzzle[row]
        if val in Row:
            return False
        else:
            return True

    def check_colum(self, val):
        col = self.values[1]
        Col = [[row[col] for row in self.puzzle]]
        if val in Col:
            return False
        else:
            return True

    def find_box_start(self, coordinate):
        return coordinate // 3 * 3

    def get_box_coordinates(self, row_number, column_number):
        return self.find_box_start(column_number), self.find_box_start(row_number)

    def get_box(self):
        start_y, start_x = self.get_box_coordinates(
            self.values[0], self.values[1])
        box = []
        for i in range(start_x, 3 + start_x):
            box.extend(self.puzzle[i][start_y:start_y + 3])
        return box

    def check_box(self, val):
        b = self.get_box()
        if val in b:
            print("Box False")
            return False
        else:
            return True

    def valueCheck(self, val):
        pass

    def showMessageBox(self):
        QtGui.QMessageBox.information(self, "You have used Your 3 hints")


def textchange(text):
    # اینجا باید یه مشت ایف بزنی چک کنه ببینه درسته یا نه
    print(text)


def Game():
    starter = []
    for i in range(0, 9):
        starter.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    b = create(starter)
    print("Created")
    c = copy.deepcopy(b)
    puzz = start(c, 20)
    print("Started")
    w = IntroWindow(puzz, b)
    print(b)
    w.show()


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
    print(b)
    w.show()

    sys.exit(app.exec_())
