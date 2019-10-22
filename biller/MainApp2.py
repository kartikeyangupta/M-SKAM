# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainApp2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from datetime import datetime
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.item1 = QtWidgets.QLineEdit(self.centralwidget)
        self.item1.setGeometry(QtCore.QRect(120, 140, 241, 31))
        self.item1.setObjectName("item1")
        self.qty1 = QtWidgets.QLineEdit(self.centralwidget)
        self.qty1.setGeometry(QtCore.QRect(430, 140, 241, 31))
        self.qty1.setObjectName("qty1")
        self.price1 = QtWidgets.QLineEdit(self.centralwidget)
        self.price1.setGeometry(QtCore.QRect(760, 140, 241, 31))
        self.price1.setObjectName("price1")
        self.item2 = QtWidgets.QLineEdit(self.centralwidget)
        self.item2.setGeometry(QtCore.QRect(120, 220, 241, 31))
        self.item2.setObjectName("item2")
        self.qty2 = QtWidgets.QLineEdit(self.centralwidget)
        self.qty2.setGeometry(QtCore.QRect(430, 220, 241, 31))
        self.qty2.setObjectName("qty2")
        self.price2 = QtWidgets.QLineEdit(self.centralwidget)
        self.price2.setGeometry(QtCore.QRect(760, 220, 241, 31))
        self.price2.setObjectName("price2")
        self.item3 = QtWidgets.QLineEdit(self.centralwidget)
        self.item3.setGeometry(QtCore.QRect(120, 310, 241, 31))
        self.item3.setObjectName("item3")
        self.qty3 = QtWidgets.QLineEdit(self.centralwidget)
        self.qty3.setGeometry(QtCore.QRect(430, 310, 241, 31))
        self.qty3.setObjectName("qty3")
        self.price3 = QtWidgets.QLineEdit(self.centralwidget)
        self.price3.setGeometry(QtCore.QRect(760, 310, 241, 31))
        self.price3.setObjectName("price3")
        self.item4 = QtWidgets.QLineEdit(self.centralwidget)
        self.item4.setGeometry(QtCore.QRect(120, 390, 241, 31))
        self.item4.setObjectName("item4")
        self.qty4 = QtWidgets.QLineEdit(self.centralwidget)
        self.qty4.setGeometry(QtCore.QRect(430, 390, 241, 31))
        self.qty4.setObjectName("qty4")



        self.price4 = QtWidgets.QLineEdit(self.centralwidget)
        self.price4.setGeometry(QtCore.QRect(760, 390, 241, 31))
        self.price4.setObjectName("price4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 70, 111, 22))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 80, 111, 22))
        self.label_4.setObjectName("label_4")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(460, 600, 117, 32))
        self.Calculate.setObjectName("Calculate")
        self.Calculate.clicked.connect(lambda:self.calc())
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 70, 111, 22))
        self.label_3.setObjectName("label_3")
        self.Store = QtWidgets.QPushButton(self.centralwidget)
        self.Store.setGeometry(QtCore.QRect(460, 660, 117, 32))
        self.Store.setObjectName("Store")
        self.Store.clicked.connect(lambda:self.store())
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 510, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Total = QtWidgets.QLabel(self.centralwidget)
        self.Total.setGeometry(QtCore.QRect(530, 510, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Total.setFont(font)
        self.Total.setObjectName("Total")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def calc(self):
        row1 = [self.item1.text(),self.qty1.text(),self.price1.text()]
        row2 = [self.item2.text(),self.qty2.text(),self.price2.text()]
        row3 = [self.item3.text(),self.qty3.text(),self.price3.text()]
        row4 = [self.item4.text(),self.qty4.text(),self.price4.text()]
        data = [row1 , row2 , row3 , row4]
        finaldata = []
        amt = 0
        for rows in data:
            if len(rows[0])>0:
                amt = amt + int(rows[2])
        self.Total.setText(str(amt))
    def store(self):
        row1 = [datetime.now().strftime("%Y-%m-%d"),self.item1.text(),self.qty1.text()]
        row2 = [datetime.now().strftime("%Y-%m-%d"),self.item2.text(),self.qty2.text()]
        row4 = [datetime.now().strftime("%Y-%m-%d"),self.item4.text(),self.qty4.text()]
        row3 = [datetime.now().strftime("%Y-%m-%d"),self.item3.text(),self.qty3.text()]
        data = [row1 , row2 , row3 , row4]
        finaldata = []
        amt = 0
        with open('transactions.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            for rows in data:
                if len(rows[1])>0:
                    finaldata.append(rows)
                    amt = amt + int(rows[2])
                    writer.writerow(rows)
        csvFile.close()
        print(finaldata)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Item Name"))
        self.label_4.setText(_translate("MainWindow", "Price"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "Qty."))
        self.Store.setText(_translate("MainWindow", "Store"))
        self.label_2.setText(_translate("MainWindow", "Total"))
        self.Total.setText(_translate("MainWindow", "0.0"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
