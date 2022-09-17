# Typing speed game
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
import random
from Word_List import word_list


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 530)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sentence_label = QtWidgets.QLabel(self.centralwidget)
        self.sentence_label.setGeometry(QtCore.QRect(10, 100, 621, 71))
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
        self.lineEdit.setGeometry(QtCore.QRect(22, 220, 601, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.submit)

        self.lcdNumber_WPM = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_WPM.setGeometry(QtCore.QRect(150, 412, 64, 31))
        self.lcdNumber_WPM.setObjectName("lcdNumber_WPM")

        self.lcdNumber_Accuracy = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_Accuracy.setGeometry(QtCore.QRect(440, 412, 64, 31))
        self.lcdNumber_Accuracy.setObjectName("lcdNumber_Accuracy")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 420, 31, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 420, 62, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def __init__(self):
        self.count = 0
        self.tic = time.perf_counter()
        self.sentence_rand()
        self.wpm_total = 0
        self.accuracy_total = 0

    def sentence_rand(self):
        self.sentence_rand_words = random.sample(word_list, 10)
        self.sentence_rand_together = " ".join(self.sentence_rand_words)

    def submit(self):
        self.toc = time.perf_counter()
        total_time = self.toc - self.tic

        self.count += 1
        print("count is " + str(self.count))

        self.user_typing = self.lineEdit.text()
        self.user_words = self.user_typing.split()
        self.lineEdit.setText("")

        self.not_in_sentence = set(self.sentence_rand_words).difference(
            set(self.user_words)
        )

        correct_percent = (
            len(self.sentence_rand_words) - len(self.not_in_sentence)
        ) / len(self.sentence_rand_words)
        self.lcdNumber_Accuracy.display(int(correct_percent * 100))

        wpm = (
            (len(self.sentence_rand_words) - len(self.not_in_sentence)) / total_time
        ) * 60
        self.lcdNumber_WPM.display(int(wpm))

        self.sentence_rand()
        self.sentence_label.setText(self.sentence_rand_together)
        self.user_typing = ""
        self.tic = time.perf_counter()

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
