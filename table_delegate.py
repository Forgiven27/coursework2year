from PySide6.QtWidgets import QStyledItemDelegate
from custom_lineEd import CustomLineEdit
class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return CustomLineEdit(parent)

    def setEditorData(self, editor, index):
        text = index.model().data(index, 0)
        editor.setText(text)

    def setModelData(self, editor, model, index):
        value = editor.text()
        model.setData(index, value, 0)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
