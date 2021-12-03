# This is a sample Python script.
import sys

from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Ui(QMainWindow):
    FROM, SUBJECT, DATE = range(3)

    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowState(Qt.WindowMaximized)
        loadUi('basic_ui.ui', self)
        self.acc_box.addItem("Administration")
        self.acc_box.addItem("AIO")
        self.acc_box.addItem("TCL")
        self.acc_box.addItem("PREWAVE")
        self.acc_box.addItem("POSTWAVE")
        self.acc_box.addItem("TESTING")
        self.acc_box.addItem("COATING")
        self.acc_box.addItem("DISPATCH")



class OtherWindow(QWidget):
    def __init__(self):
        pass


def Application():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    Application()
