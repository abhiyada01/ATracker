# This is a sample Python script.
import sys
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Ui(QMainWindow):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowState(Qt.WindowMaximized)
        loadUi('basic_ui.ui', self)
        self.drop_down_setting()
        self.table_setting()
        self.login_but.clicked.connect(self.check_password)

    def drop_down_setting(self):
        item_list = self.check_user()
        for item in item_list:
            self.acc_box.addItem(item)
        # self.acc_box.addItem("AOI")
        # self.acc_box.addItem("TCL")
        # self.acc_box.addItem("PREWAVE")
        # self.acc_box.addItem("POSTWAVE")
        # self.acc_box.addItem("TESTING")
        # self.acc_box.addItem("COATING")
        # self.acc_box.addItem("DISPATCH")

    def table_setting(self):
        col_width = 170
        self.data_list.setColumnWidth(0, 200)
        self.data_list.setColumnWidth(1, col_width)
        self.data_list.setColumnWidth(2, col_width)
        self.data_list.setColumnWidth(3, col_width)
        self.data_list.setColumnWidth(4, col_width)
        self.data_list.setColumnWidth(5, col_width)
        self.data_list.setColumnWidth(6, col_width)
        self.data_list.setColumnWidth(7, col_width)
        self.data_list.setColumnWidth(8, col_width)

    def check_password(self):
        current_user = None
        # print(user, password)
        for user, password in self.get_password():
            if self.acc_box.currentText() == user and self.pass_entry.text() == password:
                current_user = user
                print('Login in :', current_user)
                break
            else:
                print('Wrong input')


    def check_user(self):
        with open('cred_data.json', 'r') as data:
            d = json.load(data)
        l1 = [key['user'] for key in d['F1']]
        return l1

    def get_password(self):
        with open('cred_data.json', 'r') as data:
            d = json.load(data)
            user = [(key['user'], key['password']) for key in d['F1']]
            return user


def Application():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Application()
