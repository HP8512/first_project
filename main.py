from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from PyQt6 import uic
import sys

em = " "
ps = " "
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register.ui",self)
        self.msg = QMessageBox()
        self.registerbutton.clicked.connect(self.check)
        self.haveanaccount.clicked.connect(self.logup)
    def check(self):
        global em,ps
        em = self.email.text()
        ps = self.pwd.text()
        usr = self.username.text()
        cf = self.cfpwd.text()
        if em == "" and ps == "" and usr == "" and cf == "":
            self.msg.setText("Vui lòng nhập thông tin")
            self.msg.setIcon(QMessageBox.Icon.Warning)
            self.msg.exec()
        else:
            login.show()
            self.close()
    def logup(self):
        login.show()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login.ui",self)
        self.msg2 = QMessageBox()
        self.msg3 = QMessageBox()
        self.loginbutton.clicked.connect(self.check2)
        self.needanaccount.clicked.connect(self.resup)
    def check2(self):
        lem = self.emailline.text()
        lps = self.pwdline.text()
        if lem == "" and lps == "":
            self.msg2.setText("Vui lòng nhập email và mật khẩu")
            self.msg2.setIcon(QMessageBox.Icon.Warning)
            self.msg2.exec()
        elif lem != em and lps != ps:
            self.msg2.setText("Email hoặc mật khẩu sai hoặc chưa tạo")
            self.msg2.setIcon(QMessageBox.Icon.Warning)
            self.msg2.exec()
        elif lem == em and lps == ps:
            home.show()
            self.close()
    def resup(self):
        register.show()
        self.close()

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Home.ui",self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register = Register()
    login = Login()
    home = Home()
    login.show()
    app.exec()
    