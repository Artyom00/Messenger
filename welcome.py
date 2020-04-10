# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Greeting(object):
    def setupUi(self, Greeting):
        Greeting.setObjectName("Greeting")
        Greeting.resize(527, 521)
        self.centralwidget = QtWidgets.QWidget(Greeting)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 0, 431, 171))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 310, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        Greeting.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Greeting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 26))
        self.menubar.setObjectName("menubar")
        Greeting.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Greeting)
        self.statusbar.setObjectName("statusbar")
        Greeting.setStatusBar(self.statusbar)

        self.retranslateUi(Greeting)
        QtCore.QMetaObject.connectSlotsByName(Greeting)

    def retranslateUi(self, Greeting):
        _translate = QtCore.QCoreApplication.translate
        Greeting.setWindowTitle(_translate("Greeting", "Greeting"))
        self.label.setText(_translate("Greeting", "Welcome to Messenger!"))
        self.pushButton_2.setText(_translate("Greeting", "Log in"))
