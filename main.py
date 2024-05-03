import PySide6
from PySide6 import QtWidgets, QtGui
import sys

import DataBaseClass
from TextWindow import HelpWindow
from main_UI import MainWindow_UI
from tab_second import SecondTabUI
from tab_third import ThirdTabUI
from tab_forth import ForthTabUI


class MainApp(PySide6.QtWidgets.QMainWindow, MainWindow_UI):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)

        self.tab2 = SecondTabUI()
        self.tab2.setupUi(self.ui.widget_second_tab)
        self.tab3 = ThirdTabUI()
        self.tab3.setupUi(self.ui.widget_third_tab)
        self.tab4 = ForthTabUI()
        self.tab4.setupUi(self.ui.widget_forth_tab)


        help_open = PySide6.QtGui.QAction("Справка", self.ui.lineEdit_exp)
        help_open.triggered.connect(self.open_help_window)

        self.ui.help_button.addAction(help_open)

        self.ui.button_choose_db.clicked.connect(self.show_file_dialog)
        self.ui.button_open_table.clicked.connect(self.fill_table)



        self.path = None
        self.my_table = None
        self.row_buffer = 0


        #self.vert_head_massive = []

        self.ui.button_del_cycle.clicked.connect(self.row_delete)
        self.ui.button_add_cycle.clicked.connect(self.row_add)

        self.ui.table_1.verticalHeader().hide()
        self.ui.table_1.setColumnWidth(0, 50)

        #self.ui.table_1.clicked.connect(self.test_functions)

        self.ui.lineEdit_exp.textChanged.connect(self.test_functions)

    def test_functions(self):
        if self.ui.lineEdit_exp.text() != '':
            a = float(self.ui.lineEdit_exp.text())
            if a > 1 or a < 0:
                msgbox = PySide6.QtWidgets.QMessageBox()
                msgbox.critical(self.ui.widget_first_tab, "Параметр некорректен", "Измените параметр")


    def open_help_window(self):
        global help_win
        help_win = HelpWindow()
        help_win.show()


    def table_trans_updater(self):
        self.my_table.update_table(self.row_take(), self.ui.combobox_choose_db.currentText())

    def row_take(self):
        rows = []
        for j in range(self.ui.table_1.rowCount()):
            mass = []
            for i in range(self.ui.table_1.columnCount()):
                if i == 0:
                    mass.append(int(self.ui.table_1.item(j, i).text()))
                else:
                    mass.append(float(self.ui.table_1.item(j, i).text()))
            rows.append(tuple(mass))
        return rows

    def show_file_dialog(self): # Открытие диалогового окна для выбора таблицы
        text, ok = PySide6.QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор базы данных')
        if ok:
            list_comb = text.split('/')
            self.path = list_comb[-1]
            self.fill_combobox()

    def fill_combobox(self): # Заполенение комбобокса именами таблиц БД
        self.my_table = DataBaseClass.DataBase(self.path)
        for i in self.my_table.table_names():
            self.ui.combobox_choose_db.addItem(str(i)[2:-3])

    def row_delete(self): # удаление выделенной строки
        self.buffer_updater()
        row_index = self.ui.table_1.currentRow()
        if row_index >= 0:
            self.ui.table_1.removeRow(row_index)
            self.ui.table_1.selectionModel().clearCurrentIndex()
        self.table_trans_updater()

    def row_add(self):
        value = self.row_buffer+1
        self.ui.table_1.insertRow(self.ui.table_1.rowCount())
        self.ui.table_1.setItem(self.ui.table_1.rowCount()-1, 0, PySide6.QtWidgets.QTableWidgetItem(str(value)))
        for i in range(self.ui.table_1.columnCount() - 1):
            sum_cells = 0
            for j in range(self.ui.table_1.rowCount()-1):

                if self.ui.table_1.item(j, i + 1) is not None:
                    sum_cells += float(self.ui.table_1.item(j, i + 1).text())
            value = round(sum_cells, 4)
            self.ui.table_1.setItem(self.ui.table_1.rowCount() - 1, i+1, PySide6.QtWidgets.QTableWidgetItem(str(value)))
        self.buffer_updater()
        self.table_trans_updater()

    def buffer_updater(self):
        last_index = int(self.ui.table_1.item(self.ui.table_1.rowCount()-1, 0).text())
        print(last_index)
        if last_index > self.row_buffer:
            self.row_buffer = last_index

    def fill_params(self):
        if self.path != None:
            for s in self.my_table.table_names():
                a = s[0]
                if (s[0].lower()).find("add") != -1:
                    self.ui.lineEdit_error.setText(str(self.my_table.specific_zero_cell(a, "E")))
                    self.ui.lineEdit_exp.setText(str(self.my_table.specific_zero_cell(a, "A")))

                    msgbox = PySide6.QtWidgets.QMessageBox()
                    msgbox.setText("Параметры добавлены")
                    msgbox.exec()
    def fill_img(self):
        data = self.my_table.specific_byte_cell()
        with open("image.jpg", "wb") as file:
            file.write(data)

        img = PySide6.QtGui.QPixmap("image.jpg")
        #img.scaledToHeight(int(self.ui.groupbox_table1.height()))
        #img.scaledToWidth(int(self.ui.groupbox_table1.width()))
        self.ui.label_img.setMaximumWidth(int(self.ui.groupbox_table1.width()))
        self.ui.label_img.setMaximumHeight(int(self.ui.groupbox_table1.height()))
        self.ui.label_img.setPixmap(img)

        self.ui.la_1.addWidget(self.ui.label_img)
        # self.ui.groupbox_img1.setFixedHeight(int(self.ui.groupbox_table1.height()))
        # self.ui.groupbox_img1.setFixedWidth(int(self.ui.groupbox_table1.width()))
        self.ui.groupbox_img1.updateGeometry()

        msgbox = PySide6.QtWidgets.QMessageBox()
        msgbox.setText("Картинка добавлена")
        msgbox.exec()


    def fill_table(self):
        if self.path != "":
            self.my_table = DataBaseClass.DataBase(self.path)
            content_of_table = self.my_table.rows_columns(self.ui.combobox_choose_db.currentText())
            count_of_rows = len(content_of_table)
            count_of_columns = len(content_of_table[0])

            self.ui.table_1.setColumnCount(count_of_columns)
            self.ui.table_1.setRowCount(count_of_rows)
            #self.ui.table_1.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem('Эпоха'))

            vert_head_massive = []
            for i in content_of_table:
                vert_head_massive.append(i[0])
            columns_names = self.my_table.columns_names(self.ui.combobox_choose_db.currentText())
            for i in range(count_of_columns):
                self.ui.table_1.setHorizontalHeaderItem(i, PySide6.QtWidgets.QTableWidgetItem(columns_names[i]))
            for i in vert_head_massive:
                self.ui.table_1.setVerticalHeaderItem(i, PySide6.QtWidgets.QTableWidgetItem(str(i)))

            for j in range(len(vert_head_massive)):
                for i in range(count_of_columns):
                    cell = str(content_of_table[j][i]).replace(',', '.')
                    self.ui.table_1.setItem(j, i, PySide6.QtWidgets.QTableWidgetItem(cell))
            self.buffer_updater()
            self.fill_params()
            self.fill_img()










if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()


    sys.exit(app.exec())
