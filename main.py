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

    def table_setting(self):
        col_width = 170
        self.data_list.setColumnWidth(0, 230)
        for i in range(1,7):
            self.data_list.setColumnWidth(i, col_width)

    def check_password(self):
        current_user = None
        # print(user, password)
        for user, password in self.get_password():
            try:
                if self.acc_box.currentText() == user and self.pass_entry.text() == password:
                    current_user = user
                    print('Login in :', current_user)
                    break
            except Exception as e:
                print(e)



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
