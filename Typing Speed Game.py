# Typing speed game
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
import random
from Word_List import word_list


def sentence_rand():
    return random.sample(word_list, 10)


sentence_rand_together = " ".join(sentence_rand())
sentence = sentence_rand_together


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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sentence_label.setText(_translate("MainWindow", sentence_rand_together))
        self.label.setText(_translate("MainWindow", "WPM"))
        self.label_2.setText(_translate("MainWindow", "Accuracy"))

    def submit(self):
        pass

    def user_input():
        print(sentence)
        tic = time.perf_counter()
        user_typing = input("Please type the sentence above. ")
        toc = time.perf_counter()
        total_time = toc - tic

        sentence_words = sentence_rand

        user_words = user_typing.split()

        not_in_sentence = set(sentence_words).difference(set(user_words))

        correct_percent = (len(sentence_words) - len(not_in_sentence)) / len(
            sentence_words
        )
        print("Accuracy: " + str(correct_percent * 100) + "%")
        wpm = ((len(sentence_words) - len(not_in_sentence)) / total_time) * 60
        print("Your WPM is " + str(round(wpm, 0)))


# user_input()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
