# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(573, 673)
        self.centralwidget = QtWidgets.QWidget(Messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 70, 511, 501))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 600, 391, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 600, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 20, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        Messenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Messenger)
        self.statusbar.setObjectName("statusbar")
        Messenger.setStatusBar(self.statusbar)

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.pushButton.setText(_translate("Messenger", "Send"))
        self.pushButton_2.setText(_translate("Messenger", "Log out"))
