# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime
import sys
import csv
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 785)
        MainWindow.setStyleSheet("font: 14pt \"Sans serif\";\n"
"background-color: rgb(144,164,174);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Cal1 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.Cal1.setGeometry(QtCore.QRect(110, 10, 451, 191))
        self.Cal1.setObjectName("Cal1")
        self.Cal1.clicked[QtCore.QDate].connect(self.showDate1)
        self.Cal2 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.Cal2.setGeometry(QtCore.QRect(110, 230, 448, 191))
        self.Cal2.setObjectName("calendarWidget_2")
        self.Cal2.clicked[QtCore.QDate].connect(self.showDate2)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(700, 30, 231, 71))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(690, 230, 231, 91))
        self.label2.setObjectName("label2")
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(110, 450, 451, 51))
        self.uploadButton.setObjectName("uploadButton")
        self.uploadButton.clicked.connect(lambda:self.openFileNameDialog())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def openFileNameDialog(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        ext = fileName.split('.')
        if ext[1] == "csv":
            self.readData(fileName)
        else:
            print("NOT A CSV FILE")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.uploadButton.setText(_translate("MainWindow", "Upload Prediction FIle"))
    def showDate1(self, date):
        self.label1.setText(date.toString())
    def showDate2(self, date):
        self.label2.setText(date.toString())
    def readData(self,filename1):
        filename  = filename1
        fields = []
        rows = []
        startDate = self.Cal1.selectedDate().toString("MM-dd-yyyy")
        endDate = self.Cal2.selectedDate().toString("MM-dd-yyyy")
        sdate = datetime.strptime(startDate,"%m-%d-%Y").date()
        edate = datetime.strptime(endDate,"%m-%d-%Y").date()
        print(sdate)
        print(type(sdate))
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
        sum = 0
        for row in rows:
            getDat = row[0]
            gdate = datetime.strptime(getDat,'%m-%d-%Y').date()
            if gdate>=sdate and gdate<=edate:
                print(row)
        self.close()
        exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
