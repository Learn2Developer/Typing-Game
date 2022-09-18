# Typing speed game
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import *
from Game_Done import Ui_DoneWindow
import sys
import time
import random
from Word_List import word_list


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 475)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sentence_label = QtWidgets.QLabel(self.centralwidget)
        self.sentence_label.setGeometry(QtCore.QRect(10, 110, 741, 71))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.sentence_label.setFont(font)
        self.sentence_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sentence_label.setObjectName("sentence_label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(12, 200, 741, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.submit)

        self.lcdNumber_WPM = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_WPM.setGeometry(QtCore.QRect(210, 302, 64, 31))
        self.lcdNumber_WPM.setObjectName("lcdNumber_WPM")

        self.lcdNumber_Accuracy = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_Accuracy.setGeometry(QtCore.QRect(500, 302, 64, 31))
        self.lcdNumber_Accuracy.setObjectName("lcdNumber_Accuracy")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 310, 31, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 310, 62, 17))
        self.label_2.setObjectName("label_2")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(307, 60, 131, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def __init__(self):
        self.count = 1
        self.tic = time.perf_counter()
        self.sentence_rand()
        self.wpm_total = 0
        self.wpm_sum = 0
        self.accuracy_total = 0
        self.accuracy_sum = 0

    def sentence_rand(self):
        self.sentence_rand_words = random.sample(word_list, 10)
        self.sentence_rand_together = " ".join(self.sentence_rand_words)

    def submit(self):
        while self.count <= 4:
            self.toc = time.perf_counter()
            self.total_time = self.toc - self.tic
            print(self.total_time)

            self.user_typing = self.lineEdit.text()
            self.user_words = self.user_typing.split()
            self.lineEdit.setText("")

            self.not_in_sentence = set(self.sentence_rand_words).difference(
                set(self.user_words)
            )

            self.correct_percent = (
                (len(self.sentence_rand_words) - len(self.not_in_sentence))
                / len(self.sentence_rand_words)
            ) * 100

            print("correct percent = " + str(self.correct_percent))
            self.accuracy_sum += self.correct_percent

            print("accuracy before division = " + str(self.accuracy_total))
            self.accuracy_total = self.accuracy_sum / self.count

            print("accuracy after division = " + str(self.accuracy_total))
            self.lcdNumber_Accuracy.display(int(self.accuracy_total))

            self.wpm = (
                (len(self.sentence_rand_words) - len(self.not_in_sentence))
                / self.total_time
            ) * 60

            print("WPM for this round = " + str(self.wpm))
            self.wpm_sum += self.wpm

            print("WPM total before division = " + str(self.wpm_total))
            self.wpm_total = self.wpm_sum / self.count

            print("WPM after division = " + str(self.wpm_total))

            self.lcdNumber_WPM.display(int(self.wpm_total))

            self.sentence_rand()
            self.sentence_label.setText(self.sentence_rand_together)
            self.user_typing = ""
            self.progressBar.setValue((self.count) * 20)
            self.count += 1
            print("count is " + str(self.count))
            self.tic = time.perf_counter()
            break

        else:

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_DoneWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.accuracy_total_label.setText(
                "Your average Accuracy was: " + str(int(self.accuracy_total)) + "%"
            )

            self.ui.wpm_total_label.setText(
                "Your average Speed was: " + str(int(self.wpm_total)) + " wpm"
            )
            MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sentence_label.setText(
            _translate("MainWindow", self.sentence_rand_together)
        )
        self.label.setText(_translate("MainWindow", "WPM"))
        self.label_2.setText(_translate("MainWindow", "Accuracy"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
