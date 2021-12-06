# This is a sample Python script.
import sys
import sql_data as sd
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi


class Ui(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowState(Qt.WindowMaximized)
        loadUi('basic_ui.ui', self)
        self.drop_down_setting()
        self.table_setting()
        self.login_but.clicked.connect(self.check_password)
        self.reload_but.clicked.connect(self.load_data)
        # self.load_data()

    def drop_down_setting(self):
        item_list = self.check_user()
        for item in item_list:
            self.acc_box.addItem(item)

    def table_setting(self):
        col_width = 165
        self.data_list.setColumnWidth(0, 230)
        for i in range(1, 7):
            self.data_list.setColumnWidth(i, col_width)

    def check_password(self):
        user_dict = self.get_password()
        user = self.acc_box.currentText()
        pass_word = self.pass_entry.text()
        password = user_dict[user]
        if password == pass_word:
            print('Login in :', user)
        else:
            if len(pass_word) == 0:
                self.error_message("Please Enter Password")
            else:
                self.error_message("Please Correct Password")

    def check_user(self):
        with open('cred_data.json', 'r') as data:
            d = json.load(data)
        l1 = [key['user'] for key in d['F1']]
        return l1

    def get_password(self):
        with open('cred_data.json', 'r') as data:
            d = json.load(data)
            user = [(key['user'], key['password']) for key in d['F1']]
            user = dict(user)
            return user

    def load_data(self):
        return_data = sd.find_all()
        row = 0
        # print(row)
        self.data_list.setRowCount(len(return_data))
        for person in return_data:
            # print(person)
            for col in range(8):
                self.data_list.setItem(row, col, QTableWidgetItem(str(person[col])))
            row += 1

    def error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Password Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()


def Application():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Application()
