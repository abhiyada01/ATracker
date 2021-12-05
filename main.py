# This is a sample Python script.
import sys
import sqlite3 as sq
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class Ui(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowState(Qt.WindowMaximized)
        loadUi('basic_ui.ui', self)
        self.drop_down_setting()
        self.table_setting()
        self.login_but.clicked.connect(self.check_password)
        self.load_data()

    def drop_down_setting(self):
        item_list = self.check_user()
        for item in item_list:
            self.acc_box.addItem(item)

    def table_setting(self):
        col_width = 170
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
            print('invalid')

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
        people = [{"name": "jone", "age": 45, "address": "LA"}]
        row = 0
        self.data_list.setRowCount(len(people))
        for person in people:
            self.data_list.setItem(0, 0, QTableWidgetItem(person["name"]))
            row += 1


def Application():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Application()
