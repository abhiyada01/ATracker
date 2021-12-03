# This is a sample Python script.
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Ui(QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowState(Qt.WindowMaximized)
        loadUi('basic_ui.ui', self)
        self.drop_down_setting()
        self.table_setting()

    def drop_down_setting(self):
        self.acc_box.addItem("Administration")
        self.acc_box.addItem("AIO")
        self.acc_box.addItem("TCL")
        self.acc_box.addItem("PREWAVE")
        self.acc_box.addItem("POSTWAVE")
        self.acc_box.addItem("TESTING")
        self.acc_box.addItem("COATING")
        self.acc_box.addItem("DISPATCH")

    def table_setting(self):
        col_width = 170
        self.data_list.setColumnWidth(0, 350)
        self.data_list.setColumnWidth(1, col_width)
        self.data_list.setColumnWidth(2, col_width)
        self.data_list.setColumnWidth(3, col_width)
        self.data_list.setColumnWidth(4, col_width)
        self.data_list.setColumnWidth(5, col_width)
        self.data_list.setColumnWidth(6, col_width)
        self.data_list.setColumnWidth(7, col_width)
        self.data_list.setColumnWidth(8, col_width)
        self.data_list.setColumnWidth(0, col_width)


def Application():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Application()
