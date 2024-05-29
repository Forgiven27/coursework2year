from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QDoubleValidator, QKeyEvent
from PySide6.QtCore import QLocale

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        validator = QDoubleValidator(self)
        validator.setNotation(QDoubleValidator.StandardNotation)
        validator.setDecimals(10)
        validator.setLocale(QLocale(QLocale.C))
        self.setValidator(validator)

    def keyPressEvent(self, event):
        if event.text() == ',':
            # Заменяем запятую на точку
            event = QKeyEvent(event.type(), event.key(), event.modifiers(), '.', event.isAutoRepeat(), event.count())
        if event.text() == '.':
            # Запрещаем ввод точки в начале строки
            if self.cursorPosition() == 0:
                return
            # Запрещаем ввод второй точки
            if '.' in self.text():
                return
        super().keyPressEvent(event)

    def focusOutEvent(self, event):
        # Запрещаем наличие точки в конце строки
        text = self.text()
        print(text)
        if text.endswith('.'):
            self.setText(text[:-1])
            print(self.text())

        super().focusOutEvent(event)
