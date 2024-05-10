from PySide6 import QtWidgets
import PySide6

class HelpWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        # super().__init__()
        help_w = PySide6.QtWidgets.QMainWindow
        HelpWindow.setMinimumSize(self,500, 500)
        HelpWindow.setWindowTitle(self, "Справка")
        a = PySide6.QtWidgets.QWidget()
        self.layout_main = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit = PySide6.QtWidgets.QTextEdit()
        self.text_edit.setReadOnly(True)
        help_text = """
                <h1>Руководство к использованию программы</h1>
                <p>This is the help information for the application.ммммммммммммммммммммммммммммм
                мммммммммммммммммммммммммммммммммммммммммммммммммммммммм
                ммммммммммммммммммммммммммммммммммммммммммммммммм
                ммммммммммммммммммммммммммммммммммммммммммммммммм
                мммммммммммммммммммммммммммммммммммммммммммммммммммммммммммммммммм</p>
                <p>Use the navigation buttons to move around.</p>
                <p><a href="https://example.com">Visit our website</a> for more information.</p>
                """

        self.text_edit.setHtml(help_text)


        self.close_button = PySide6.QtWidgets.QPushButton("Close")
        self.close_button.clicked.connect(self.close)


        self.layout_main.addWidget(self.text_edit)
        self.layout_main.addWidget(self.close_button)
        a.setLayout(self.layout_main)
        self.setCentralWidget(a)
