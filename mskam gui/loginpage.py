# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setStyleSheet("font: 14pt \"Sans serif\";\n"
"background-color: rgb(144,164,174);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 100, 191, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 171, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sans serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.SIGN_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.SIGN_BUTTON.setGeometry(QtCore.QRect(190, 220, 191, 27))
        self.SIGN_BUTTON.setObjectName("SIGN_BUTTON")
        self.SIGN_BUTTON.clicked.connect(lambda:self.btnCheck())
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 201, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 50, 181, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.confirmpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmpassword.setGeometry(QtCore.QRect(280, 170, 181, 27))
        self.confirmpassword.setObjectName("confirmpassword")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 130, 181, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 90, 181, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 31))
        self.menubar.setObjectName("menubar")
        self.menuMSKAM = QtWidgets.QMenu(self.menubar)
        self.menuMSKAM.setObjectName("menuMSKAM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMSKAM.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def btnCheck(self):
        name = self.lineEdit_3.text()
        print(name)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(name)
        msg.setWindowTitle("MessageBox demo")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CONTACT NUMBER"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))
        self.label_3.setText(_translate("MainWindow", "COMPANY NAME"))
        self.label_4.setText(_translate("MainWindow", "SIGN UP"))
        self.SIGN_BUTTON.setText(_translate("MainWindow", "SIGN-UP!"))
        self.label_5.setText(_translate("MainWindow", "CONFIRM PASSWORD"))
        self.menuMSKAM.setTitle(_translate("MainWindow", "ABOUT"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
