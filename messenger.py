from builtins import super
from datetime import datetime
import requests
from PyQt5 import QtWidgets, QtCore
import welcome
import login
import messenger_window


class WelcomeWindow(welcome.Ui_Greeting, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.pressed.connect(self.OpenLoginWindow)
        self.pushButton_2.pressed.connect(self.close)

    def OpenLoginWindow(self):
        self.login_user = LoginWindow()
        self.login_user.show()


class LoginWindow(QtWidgets.QMainWindow, login.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.login)

    def login(self):
        global username, password
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not username:
            self.addText("ERROR: username is empty!")
            return

        if not password:
            self.addText("ERROR: password is empty!")
            return

        self.response = requests.post(
            'http://127.0.0.1:5000/login',
            json={"username": username, "password": password}
        )

        if not self.response.json()["Response"]:
            self.addText("Password entered incorrectly! Try again")
            self.lineEdit_2.clear()
            return
        else:
            self.addText("Authorization successful!")

        self.pushButton_2.pressed.connect(self.OpenMessengerWindow)
        self.pushButton_2.pressed.connect(self.close)

    def addText(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

    def OpenMessengerWindow(self):
        self.messenger_window = MessengerWindow()
        self.messenger_window.show()

    def display_username(self):
        return username

    def display_password(self):
        return password


class MessengerWindow(QtWidgets.QMainWindow, messenger_window.Ui_Messenger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.SendMessage)
        self.pushButton_2.pressed.connect(self.exit)
        self.pushButton_2.pressed.connect(self.close)
        self.last_message_time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)

    def SendMessage(self):
        self.lw = LoginWindow()
        self.text = self.textEdit.toPlainText()

        self.name = self.lw.display_username()
        self._pass = self.lw.display_password()

        self.response = requests.post(
            'http://127.0.0.1:5000/send',
            json={"username": self.name, "password": self._pass, "text": self.text}
        )

        self.textEdit.clear()
        self.textEdit.repaint()

    def addText(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

    def getUpdates(self):
        self.response = requests.get('http://127.0.0.1:5000/history', params={'after': self.last_message_time})
        self.data = self.response.json()
        for message in self.data["messages"]:
            self.date = datetime.fromtimestamp(message["time"])  # преобразуем float в объект datetime
            self.date = self.date.strftime("%a %d/%m/%Y %H:%M:%S")
            self.addText(self.date + ' ' + message["username"])
            self.addText(message["text"])
            self.addText('')
            self.last_message_time = message["time"]

    def exit(self):
        self.response = requests.get('http://127.0.0.1:5000/shutdown')


app = QtWidgets.QApplication([])
welcome = WelcomeWindow()
welcome.show()
app.exec_()
