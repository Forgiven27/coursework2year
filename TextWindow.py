from PySide6 import QtWidgets
import PySide6

class HelpWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        # super().__init__()
        help_w = PySide6.QtWidgets.QMainWindow

        a = PySide6.QtWidgets.QWidget()
        b = PySide6.QtWidgets.QHBoxLayout()
        c = PySide6.QtWidgets.QPushButton("nooo")
        b.addWidget(c)
        a.setLayout(b)
        self.setCentralWidget(a)
        print('окно HELP')