import decimal
import PySide6
import pyqtgraph
from PySide6 import QtWidgets, QtGui, QtCore
import sys
import math
import copy
import random
import DataBaseClass
import graph
import numpy
from TextWindow import HelpWindow
from main_UI import MainWindow_UI
from tab_second import SecondTabUI
from tab_third import ThirdTabUI
from tab_forth import ForthTabUI
from tab_fifth import FifthTabUI
from tab_sixth import SixthTabUI
from table_delegate import NumericDelegate


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
        self.tab5 = FifthTabUI()
        self.tab5.setupUi(self.ui.widget_fifth_tab)
        self.tab6 = SixthTabUI()
        self.tab6.setupUi(self.ui.widget_sixth_tab)

        help_open = PySide6.QtGui.QAction("Справка", self.ui.lineEdit_exp)
        help_open.triggered.connect(self.open_help_window)

        self.img = PySide6.QtGui.QPixmap()
        self.img_dots = PySide6.QtGui.QPixmap()

        self.ui.help_button.addAction(help_open)

        self.ui.button_choose_db.clicked.connect(self.show_file_dialog)
        self.ui.button_open_table.clicked.connect(self.fill_table)

        for i in self.tab2.dict_chb_graph.keys():
            i.setChecked(True)
            i.toggled.connect(self.check_box_connect_tab2)
        self.tab2.button_phase_clean.clicked.connect(self.clean_widget_tab2)
        for i in self.tab2.dict_chb_graph_func.keys():
            i.setChecked(True)
            i.toggled.connect(self.check_box_connect_func_tab2)
        self.tab2.button_func_clean.clicked.connect(self.clean_widget_func_tab2)

        for i in self.tab3.dict_chb_graph.keys():
            i.setChecked(True)
            i.toggled.connect(self.check_box_connect_tab3)
        self.tab3.button_phase_clean.clicked.connect(self.clean_widget_tab3)
        for i in self.tab3.dict_chb_graph_func.keys():
            i.setChecked(True)
            i.toggled.connect(self.check_box_connect_func_tab3)
        self.tab3.button_func_clean.clicked.connect(self.clean_widget_func_tab3)

        for i in self.tab4.dict_chb_graph.keys():
            i.setChecked(True)
            i.toggled.connect(self.check_box_connect_tab4)
        self.tab4.button_phase_clean.clicked.connect(self.clean_widget_tab4)
        for i in self.tab4.dict_chb_graph_func.keys():
            i.setChecked(True)
            i.toggled.connect(self.check_box_connect_func_tab4)
        self.tab4.button_func_clean.clicked.connect(self.clean_widget_func_tab4)

        self.tab4.combobox_block.currentTextChanged.connect(lambda: self.tab4.groupbox_settings.setEnabled(False) or self.tab4.groupbox_tab1_center.setEnabled(False))


        self.path = None
        self.my_table = None
        self.row_buffer = 0
        self.round_number = 15
        self.delta_tab6 = decimal.Decimal("0.002")
        self.blocks = []
        self.first_fill_blocks()
        self.ui.button_del_cycle.clicked.connect(self.row_delete)
        self.ui.button_add_cycle.clicked.connect(self.row_add)
        self.ui.button_confirm.clicked.connect(self.button_param_confirm)

        self.tab2.button_recom.clicked.connect(lambda:self.rec_box(self.tab2.table_monit))
        self.tab2.button_next_dec.clicked.connect(self.open_next_tab)

        self.tab3.spinbox_count_blocks.textChanged.connect(self.fill_blocks)
        self.tab3.button_confirm.clicked.connect(self.tab3_button_confirm)
        self.tab3.button_next_dec.clicked.connect(self.open_next_tab)
        self.tab3.button_recom.clicked.connect(lambda:self.rec_box(self.tab3.table_monit))

        self.tab4.button_tab10_confirm.clicked.connect(self.tab3_button_confirm)
        self.tab4.button_tab20_confirm.clicked.connect(self.button_confirm_20_tab4)
        self.tab4.button_recom.clicked.connect(lambda: self.rec_box(self.tab4.table_monit))

        self.ui.table_1.verticalHeader().hide()
        self.ui.table_1.setColumnWidth(0, 50)

        self.tab6_spinbox_round_value = self.tab6.spinbox_round.value()
        self.tab6_quantize = str(pow(10, (-self.tab6_spinbox_round_value)))
        self.tab6.button_round.clicked.connect(self.update_tab6)


    def test_functions(self):
        pass
    def checkbox_on(self):
        for i in self.tab2.dict_chb_graph.keys():
            if not i.isChecked():
                i.setChecked(True)
        for i in self.tab2.dict_chb_graph_func.keys():
            if not i.isChecked():
                i.setChecked(True)

        for i in self.tab3.dict_chb_graph.keys():
            if not i.isChecked():
                i.setChecked(True)
        for i in self.tab3.dict_chb_graph_func.keys():
            if not i.isChecked():
                i.setChecked(True)

        for i in self.tab4.dict_chb_graph.keys():
            if not i.isChecked():
                i.setChecked(True)
        for i in self.tab4.dict_chb_graph_func.keys():
            if not i.isChecked():
                i.setChecked(True)
    def fill_blocks(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        self.blocks.clear()
        for i in range(int(self.tab3.spinbox_count_blocks.text())):
            self.blocks.append(alphabet[i])
        self.tab3.widget_tab2.setEnabled(False)
        self.tab4.widget_tab1.setEnabled(False)
        self.tab4.widget_tab2.setEnabled(False)
        self.tab4.groupbox_settings.setEnabled(False)
        self.tab4.groupbox_tab1_center.setEnabled(False)
        self.update_tab3_zerotab()

    def first_fill_blocks(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        self.blocks.clear()
        for i in range(int(self.tab3.spinbox_count_blocks.text())):
            self.blocks.append(alphabet[i])
        self.tab3.listbox_all_dots.itemClicked.connect(self.move_dot_in)
        self.tab3.listbox_cont_dots.itemClicked.connect(self.move_dot_out)
        self.tab3.combobox_choose.currentTextChanged.connect(self.subblocks_switch)
        self.tab4.listbox_unselected_dots.itemClicked.connect(self.move_dot_in_tab4)
        self.tab4.listbox_selected_dots.itemClicked.connect(self.move_dot_out_tab4)
        self.tab4.combobox_block.currentTextChanged.connect(self.subblocks_switch_tab4)
        self.tab4.button_tab11_confirm.clicked.connect(self.button_confirm_settings_tab4)
        self.tab4.combobox_subblock.currentTextChanged.connect(self.subblocks_switch_tab4_sub)
        self.tab4.listbox_available_dots.itemClicked.connect(self.move_dot_in_tab4_sub)
        self.tab4.listbox_subblock_dots.itemClicked.connect(self.move_dot_out_tab4_sub)
        self.tab4.button_next_dec.clicked.connect(self.open_next_tab)

    def rec_box(self, table):
        count = 0

        for i in range(table.rowCount()):
            if table.item(i, 3).text().rfind("Не"):
                count += 1

        if count > 1:
            msgbox = PySide6.QtWidgets.QMessageBox()
            msgbox.setText("Рекомендуется перейти на следующий уровень декомпозиции")
            msgbox.exec()
        else:
            msgbox = PySide6.QtWidgets.QMessageBox()
            msgbox.setText("Состояние объектов в пределах нормы.\nДальнешая декомпозиция не требуется.")
            msgbox.exec()

    def check_box_connect_tab2(self, checked):
        checkbox = self.sender()

        plot_widget = self.tab2.dict_chb_graph[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)
        self.tab2.graph_phase.autoRange()

    def check_box_connect_tab3(self, checked):
        checkbox = self.sender()
        plot_widget = self.tab3.dict_chb_graph[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)

    def check_box_connect_tab4(self, checked):
        checkbox = self.sender()
        plot_widget = self.tab4.dict_chb_graph[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)

    def check_box_connect_func_tab2(self, checked):
        checkbox = self.sender()
        plot_widget = self.tab2.dict_chb_graph_func[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)

    def check_box_connect_func_tab3(self, checked):
        checkbox = self.sender()
        plot_widget = self.tab3.dict_chb_graph_func[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)

    def check_box_connect_func_tab4(self, checked):
        checkbox = self.sender()
        plot_widget = self.tab4.dict_chb_graph_func[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)

    def clean_widget_tab2(self):
        for i in self.tab2.dict_chb_graph.keys():
            i.setChecked(False)

    def clean_widget_func_tab2(self):
        for i in self.tab2.dict_chb_graph_func.keys():
            i.setChecked(False)

    def clean_widget_tab3(self):
        for i in self.tab3.dict_chb_graph.keys():
            i.setChecked(False)

    def clean_widget_func_tab3(self):
        for i in self.tab3.dict_chb_graph_func.keys():
            i.setChecked(False)

    def clean_widget_tab4(self):
        for i in self.tab4.dict_chb_graph.keys():
            i.setChecked(False)

    def clean_widget_func_tab4(self):
        for i in self.tab4.dict_chb_graph_func.keys():
            i.setChecked(False)

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

    def show_file_dialog(self):  # Открытие диалогового окна для выбора таблицы
        self.ui.combobox_choose_db.clear()
        text, ok = PySide6.QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор базы данных')
        if ok:
            list_comb = text.split('/')
            self.path = list_comb[-1]
            self.fill_combobox()

    def fill_combobox(self):  # Заполенение комбобокса именами таблиц БД
        self.my_table = DataBaseClass.DataBase(self.path)
        for i in self.my_table.table_names():
            if not (str(i)[2:-3].lower()).startswith("add"):
                self.ui.combobox_choose_db.addItem(str(i)[2:-3])

    def row_delete(self):  # удаление выделенной строки
        self.buffer_updater()
        row_index = self.ui.table_1.currentRow()
        if row_index >= 0:
            self.ui.table_1.removeRow(row_index)
            self.ui.table_1.selectionModel().clearCurrentIndex()
        self.table_trans_updater()
        self.update_tab2()

    def row_add_summ(self):
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

    def row_add(self):
        value = self.row_buffer+1
        self.ui.table_1.insertRow(self.ui.table_1.rowCount())
        self.ui.table_1.setItem(self.ui.table_1.rowCount()-1, 0, PySide6.QtWidgets.QTableWidgetItem(str(value)))
        for i in range(self.ui.table_1.columnCount() - 1):
            massive = []
            for j in range(self.ui.table_1.rowCount()-2):
                if self.ui.table_1.item(j, i + 1) is not None:
                    massive.append(float(self.ui.table_1.item(j+1, i + 1).text())-float(self.ui.table_1.item(j, i + 1).text()))
            d = max(massive)
            s = random.randint(0, int(d)) - d/2
            a = float(self.ui.table_1.item(self.ui.table_1.rowCount()-2, i + 1).text())
            value = round(a + s, 4)
            self.ui.table_1.setItem(self.ui.table_1.rowCount() - 1, i+1, PySide6.QtWidgets.QTableWidgetItem(str(value)))
        self.buffer_updater()
        self.table_trans_updater()
        self.update_tab2()

    def buffer_updater(self):
        last_index = int(self.ui.table_1.item(self.ui.table_1.rowCount()-1, 0).text())
        if last_index > self.row_buffer:
            self.row_buffer = last_index

    def fill_params(self):
        if self.path != None:
            for s in self.my_table.table_names():
                a = s[0]
                if (s[0].lower()).find("add") != -1:
                    self.ui.lineEdit_error.setText(str(decimal.Decimal(str(self.my_table.specific_zero_cell(a, "E")))))
                    self.ui.lineEdit_exp.setText(str(decimal.Decimal(str(self.my_table.specific_zero_cell(a, "A")))))

                    msgbox = PySide6.QtWidgets.QMessageBox()
                    msgbox.setText("Параметры добавлены")
                    msgbox.exec()

    def button_param_confirm(self):
        if self.ui.lineEdit_exp.text() != '' or self.ui.lineEdit_error.text() != '':
            A = self.ui.lineEdit_exp.text()
            E = self.ui.lineEdit_error.text()

            def is_number(s):
                try:
                    decimal.Decimal(s)
                    return True
                except decimal.InvalidOperation:
                    return False
            try:
                a = decimal.Decimal(str(A))
                b = decimal.Decimal(str(E))
            except:
                a = -1
                b = -1

            if a > 1 or a < 0 or not is_number(A) or A == "":
                msgbox = PySide6.QtWidgets.QMessageBox()
                msgbox.critical(self.ui.widget_first_tab, "Ошибка", "Коэффициент экспоненциального сглаживания некорректен.\nИзмените параметр")
            elif b < 0 or not is_number(E) or E == "":
                msgbox = PySide6.QtWidgets.QMessageBox()
                msgbox.critical(self.ui.widget_first_tab, "Ошибка", "Значение погрешности измерения некорректно.\nИзмените параметр")

            else:
                self.my_table.update_cell("Addition", "A", "id", 0, a)
                self.my_table.update_cell("Addition", "E", "id", 0, b)
                self.update_tab2()
        else:
            msgbox = PySide6.QtWidgets.QMessageBox()
            msgbox.critical(self.ui.widget_first_tab, "Ошибка",
                            "Значение погрешности измерения некорректно.\nИзмените параметр")

    def fill_img(self):
        data = self.my_table.specific_byte_cell("Img")
        with open("image.jpg", "wb") as file:
            file.write(data)

        self.img = PySide6.QtGui.QPixmap("image.jpg")
        self.ui.label_img.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        self.ui.label_img.setPixmap(self.img)

        self.ui.la_1.addWidget(self.ui.label_img)
        self.ui.groupbox_img1.updateGeometry()

        data_dots = self.my_table.specific_byte_cell("DotsImg")
        with open("imageDots.jpg", "wb") as file_:
            file_.write(data_dots)

        self.img_dots = PySide6.QtGui.QPixmap("imageDots.jpg")
        self.tab3.label_pict.setPixmap(self.img_dots)
        self.resize_image()

        msgbox = PySide6.QtWidgets.QMessageBox()
        msgbox.setText("Картинка добавлена")
        msgbox.exec()

    def resizeEvent(self, event):
        self.resize_image()
        super().resizeEvent(event)

    def resize_image(self):
        # Получение размеров QLabel
        label1_size = self.ui.label_img.size()
        label2_size = self.tab3.label_pict.size()
        # Масштабирование изображения

        scaled_pixmap1 = self.img.scaled(label1_size, PySide6.QtCore.Qt.KeepAspectRatio,
                                           PySide6.QtCore.Qt.SmoothTransformation)
        scaled_pixmap2 = self.img_dots.scaled(label2_size, PySide6.QtCore.Qt.KeepAspectRatio,
                                           PySide6.QtCore.Qt.SmoothTransformation)

        self.ui.label_img.setPixmap(scaled_pixmap1)
        self.tab3.label_pict.setPixmap(scaled_pixmap2)

    def fill_table(self):
        if self.path != "" and self.path != None:
            self.my_table = DataBaseClass.DataBase(self.path)
            content_of_table = self.my_table.rows_columns(self.ui.combobox_choose_db.currentText())
            count_of_rows = len(content_of_table)
            count_of_columns = len(content_of_table[0])

            self.ui.table_1.setColumnCount(count_of_columns)
            self.ui.table_1.setRowCount(count_of_rows)

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
            self.update_tab2()
            self.ui.widget_second_tab.setEnabled(True)
            self.ui.groupbox_img1.setEnabled(True)
            self.ui.groupbox_cycle.setEnabled(True)
            self.ui.groupbox_param.setEnabled(True)
            self.ui.groupbox_table1.setEnabled(True)


    def update_tab2(self):
        numeric_delegate = NumericDelegate()
        for col in range(self.ui.table_1.columnCount()):
            self.ui.table_1.setItemDelegateForColumn(col, numeric_delegate)
        self.ui.widget_third_tab.setEnabled(False)
        self.ui.widget_forth_tab.setEnabled(False)
        self.tab3.widget_tab2.setEnabled(False)
        self.tab3.spinbox_count_blocks.setMaximum(int(self.ui.table_1.columnCount() / 2))

        self.tab4.widget_tab1.setEnabled(False)
        self.tab4.widget_tab2.setEnabled(False)
        self.tab4.groupbox_settings.setEnabled(False)
        self.tab4.groupbox_tab1_center.setEnabled(False)

        self.fill_tab5()
        self.fill_rest_tab6()
        self.fill_table_uni_tab6()

        self.fill_table_leap_tab6()
        self.fill_table_cyclic_tab6()


        self.fill_tab6_graph()

        self.table_phase_headers(self.tab2.table_phase_coor, self.compess_table(self.ui.table_1))
        self.table_monit_headers(self.tab2.table_monit, self.compess_table(self.ui.table_1))
        self.fill_mu_a(self.compess_table(self.ui.table_1), self.tab2.table_phase_coor)
        self.fill_table_monit(self.tab2.table_phase_coor, self.tab2.table_monit)

        tabs = [self.tab2, self.tab3, self.tab4]
        for i in tabs:
            for item in i.graph_phase.items():
                if isinstance(item, pyqtgraph.TextItem):
                    i.graph_phase.removeItem(item)
            for item in i.graph_func.items():
                if isinstance(item, pyqtgraph.TextItem):
                    i.graph_func.removeItem(item)

        self.graph_ph(self.tab2.table_phase_coor, self.tab2)
        self.graph_func(self.tab2.table_phase_coor, self.tab2)
        self.checkbox_on()
    def update_tab6(self):
        self.tab6_spinbox_round_value = self.tab6.spinbox_round.value()
        self.tab6_quantize = str(pow(10, (-self.tab6_spinbox_round_value)))
        print(self.tab6_spinbox_round_value)
        print(self.tab6_quantize)
        self.fill_rest_tab6()
        self.fill_table_uni_tab6()

        self.fill_table_leap_tab6()
        self.fill_table_cyclic_tab6()

        self.fill_tab6_graph()
    def compess_table(self, table):
        massive = []
        headers = []
        for i in range(table.columnCount()):
                headers.append(table.horizontalHeaderItem(i).text())
        massive.append(headers)

        for i in range(table.rowCount()):
            row = []
            row.clear()
            for j in range(table.columnCount()):
                row.append(float(table.item(i, j).text()))
            massive.append(row)
        return massive

    def table_phase_headers(self, obj, massive):
        obj.setColumnCount(13)
        obj.setRowCount(len(massive))
        obj.verticalHeader().hide()
        obj.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem(massive[0][0]))
        obj.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("\u03BC+"))
        obj.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem("\u03B1+"))
        obj.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem("Прогноз \u03BC+"))
        obj.setHorizontalHeaderItem(4, PySide6.QtWidgets.QTableWidgetItem("Прогноз \u03B1+"))
        obj.setHorizontalHeaderItem(5, PySide6.QtWidgets.QTableWidgetItem("\u03BC"))
        obj.setHorizontalHeaderItem(6, PySide6.QtWidgets.QTableWidgetItem("\u03B1"))
        obj.setHorizontalHeaderItem(7, PySide6.QtWidgets.QTableWidgetItem("Прогноз \u03BC"))
        obj.setHorizontalHeaderItem(8, PySide6.QtWidgets.QTableWidgetItem("Прогноз \u03B1"))
        obj.setHorizontalHeaderItem(9, PySide6.QtWidgets.QTableWidgetItem("\u03BC-"))
        obj.setHorizontalHeaderItem(10, PySide6.QtWidgets.QTableWidgetItem("\u03B1-"))
        obj.setHorizontalHeaderItem(11, PySide6.QtWidgets.QTableWidgetItem("Прогноз \u03BC-"))
        obj.setHorizontalHeaderItem(12, PySide6.QtWidgets.QTableWidgetItem("Прогноз \u03B1-"))

        for i in range(len(massive)-1):
            obj.setItem(i, 0, PySide6.QtWidgets.QTableWidgetItem(str(int(massive[i+1][0]))))
        obj.setItem(len(massive)-1, 0, PySide6.QtWidgets.QTableWidgetItem(str(self.row_buffer+1)))

    def table_monit_headers(self, obj, massive):
        obj.setColumnCount(4)
        obj.setRowCount(len(massive))
        obj.verticalHeader().hide()
        obj.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem(massive[0][0]))
        obj.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("R"))
        obj.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem("L"))
        obj.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem("Состояние"))

        for i in range(len(massive) - 1):
            obj.setItem(i, 0, PySide6.QtWidgets.QTableWidgetItem(str(int(massive[i + 1][0]))))
        obj.setItem(len(massive) - 1, 0, PySide6.QtWidgets.QTableWidgetItem(str(self.row_buffer + 1)))

    def mu_a(self, massive):
        mu_a = [[], []]
        for i in range(len(massive)-1):
            sum_mu = decimal.Decimal(str("0"))
            for j in range(len(massive[1])-1):
                sum_mu += decimal.Decimal(massive[i+1][j+1])**2
            mu_a[0].append(math.sqrt(sum_mu))

        for i in range(len(massive)-2):
            sum_a = decimal.Decimal(str("0"))
            for j in range(len(massive[1])-1):
                sum_a += (decimal.Decimal(str(massive[i+1][j+1])) * decimal.Decimal(str(massive[i+2][j+1])))

            divided = sum_a / (decimal.Decimal(str(mu_a[0][i])) * decimal.Decimal(str(mu_a[0][i+1])))

            if divided < 1:
                b = decimal.Decimal(
                    str(math.acos(sum_a / (decimal.Decimal(str(mu_a[0][i])) * decimal.Decimal(str(mu_a[0][i + 1]))))))
                mu_a[1].append(b)
            else:
                b = 0
                mu_a[1].append(b)
        return mu_a

    def fill_mu_a(self, massive, table):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()-1):
                table.setItem(row, col+1, PySide6.QtWidgets.QTableWidgetItem(""))

        massive_plus = copy.deepcopy(massive)
        massive_minus = copy.deepcopy(massive)
        e1 = decimal.Decimal("0.0005")
        e_db = str(self.my_table.specific_zero_cell("Addition", "E"))
        e2 = decimal.Decimal(e_db)
        E = e1+e2
        A = decimal.Decimal(str(self.my_table.specific_zero_cell("Addition", "A")))

        for i in range(len(massive)-1):
            for j in range(len(massive[0])-1):
                a = decimal.Decimal(str(massive[i+1][j+1]))
                massive_plus[i+1][j+1] = a + E
                massive_minus[i+1][j+1] = a - E

        mu_a_ = self.mu_a(massive)
        mu_a_plus = self.mu_a(massive_plus)
        mu_a_minus = self.mu_a(massive_minus)

        mu_a_plus_forecast = mu_a_plus
        mu_a_forecast = mu_a_
        mu_a_minus_forecast = mu_a_minus

        for j in range(len(mu_a_)):
            for i in range(len(mu_a_[j]) + 1):
                if i == 0:
                    cell_plus = decimal.Decimal(str(mu_a_plus[j][i]))
                    cell_ = decimal.Decimal(str(mu_a_[j][i]))
                    cell_minus = decimal.Decimal(str(mu_a_minus[j][i]))
                    mid_plus = decimal.Decimal(str(sum(mu_a_plus[j]) / len(mu_a_plus[j])))
                    mid_ = decimal.Decimal(str(sum(mu_a_[j]) / len(mu_a_[j])))
                    mid_minus = decimal.Decimal(str(sum(mu_a_minus[j]) / len(mu_a_minus[j])))

                    mu_a_plus_forecast[j][i] = cell_plus * A + (1 - A) * mid_plus
                    mu_a_forecast[j][i] = cell_ * A + (1 - A) * mid_
                    mu_a_minus_forecast[j][i] = cell_minus * A + (1 - A) * mid_minus
                elif i == len(mu_a_[j]):
                    mu_a_plus_forecast[j].append(
                        decimal.Decimal(str(sum(mu_a_plus_forecast[j]) / len(mu_a_plus_forecast[j]))) * A + (1 - A) * decimal.Decimal(str(mu_a_plus_forecast[j][
                            len(mu_a_[j]) - 1])))
                    mu_a_minus_forecast[j].append(
                        decimal.Decimal(str(sum(mu_a_minus_forecast[j]) / len(mu_a_minus_forecast[j]))) * A + (1 - A) *
                        decimal.Decimal(str(mu_a_minus_forecast[j][len(mu_a_[j]) - 1])))
                    mu_a_forecast[j].append(
                        decimal.Decimal(str(sum(mu_a_forecast[j]) / len(mu_a_forecast[j]))) * A + (1 - A) * decimal.Decimal(str(mu_a_forecast[j][
                            len(mu_a_[j]) - 1])))

                else:
                    mu_a_plus_forecast[j][i] = decimal.Decimal(str(mu_a_plus[j][i])) * A + (1 - A) * decimal.Decimal(str(mu_a_plus_forecast[j][i - 1]))
                    mu_a_forecast[j][i] = decimal.Decimal(str(mu_a_[j][i])) * A + (1 - A) * decimal.Decimal(str(mu_a_forecast[j][i - 1]))
                    mu_a_minus_forecast[j][i] = decimal.Decimal(str(mu_a_minus[j][i])) * A + (1 - A) * decimal.Decimal(str(mu_a_minus_forecast[j][i - 1]))

        for i in range(table.rowCount() - 1):
            table.setItem(i, 1, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_plus[0][i])))
            table.setItem(i, 5, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_[0][i])))
            table.setItem(i, 9, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_minus[0][i])))
            if i == 0:
                table.setItem(i, 2, PySide6.QtWidgets.QTableWidgetItem(str(0)))
                table.setItem(i, 6, PySide6.QtWidgets.QTableWidgetItem(str(0)))
                table.setItem(i, 10, PySide6.QtWidgets.QTableWidgetItem(str(0)))
            else:
                table.setItem(i, 2, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_plus[1][i - 1])))
                table.setItem(i, 6, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_[1][i - 1])))
                table.setItem(i, 10, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_minus[1][i - 1])))

        for i in range(table.rowCount()):
            table.setItem(i, 3, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_plus_forecast[0][i])))
            table.setItem(i, 7, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_forecast[0][i])))
            table.setItem(i, 11, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_minus_forecast[0][i])))

            if i == 0:
                table.setItem(i, 4, PySide6.QtWidgets.QTableWidgetItem(str(0)))
                table.setItem(i, 8, PySide6.QtWidgets.QTableWidgetItem(str(0)))
                table.setItem(i, 12, PySide6.QtWidgets.QTableWidgetItem(str(0)))
            else:
                table.setItem(i, 4, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_plus_forecast[1][i - 1])))
                table.setItem(i, 8, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_forecast[1][i - 1])))
                table.setItem(i, 12, PySide6.QtWidgets.QTableWidgetItem(str(mu_a_minus_forecast[1][i - 1])))

    def fill_table_monit(self, table_phase, table_monit):
        mu_plus = []
        mu_ = []
        mu_minus = []

        R = []
        L = []
        row_count = table_monit.rowCount()
        for i in range(row_count):
            mu_plus.append(float(table_phase.item(i, 3).text()))
            mu_.append(float(table_phase.item(i, 7).text()))
            mu_minus.append(float(table_phase.item(i, 11).text()))

        for i in range(row_count):
            R.append(mu_plus[i] - mu_minus[i])

            table_monit.setItem(i, 1, PySide6.QtWidgets.QTableWidgetItem(str(R[i])))
            if i != 0:
                L.append(math.fabs(mu_[i - 1] - mu_[i]))
                table_monit.setItem(i, 2, PySide6.QtWidgets.QTableWidgetItem(str(L[i])))
            else:
                L.append(math.fabs(mu_[i] - mu_[i]))
                table_monit.setItem(i, 2, PySide6.QtWidgets.QTableWidgetItem(str(L[i])))

        for i in range(row_count):
            if L[i] <= R[i]:
                table_monit.setItem(i, 3, PySide6.QtWidgets.QTableWidgetItem(str("Неаварийное")))
                table_monit.item(i, 3).setBackground(QtGui.QColor(0, 255, 0))
            else:
                table_monit.setItem(i, 3, PySide6.QtWidgets.QTableWidgetItem(str("Аварийное")))
                table_monit.item(i, 3).setBackground(QtGui.QColor(255, 0, 0, 80))


    def graph_ph(self, data_table, tab_widget):
        x_plus = []
        x_ = []
        x_minus = []
        y_plus = []
        y_ = []
        y_minus = []
        x_plus_forecast = []
        x_forecast = []
        x_minus_forecast = []
        y_plus_forecast = []
        y_forecast = []
        y_minus_forecast = []

        for i in range(data_table.rowCount()-1):
            x_plus.append(float(data_table.item(i,1).text()))
            x_.append(float(data_table.item(i, 5).text()))
            x_minus.append(float(data_table.item(i, 9).text()))
            y_plus.append(float(data_table.item(i, 2).text()))
            y_.append(float(data_table.item(i, 6).text()))
            y_minus.append(float(data_table.item(i, 10).text()))
        for i in range(data_table.rowCount()):
            x_plus_forecast.append(float(data_table.item(i,3).text()))
            x_forecast.append(float(data_table.item(i, 7).text()))
            x_minus_forecast.append(float(data_table.item(i, 11).text()))
            y_plus_forecast.append(float(data_table.item(i, 4).text()))
            y_forecast.append(float(data_table.item(i, 8).text()))
            y_minus_forecast.append(float(data_table.item(i, 12).text()))

        tab_widget.scatter_pos.setData(x_plus,y_plus)
        tab_widget.scatter_.setData(x_, y_)
        tab_widget.scatter_neg.setData(x_minus, y_minus)

        vert_headers = []
        for i in range(data_table.rowCount()):
            vert_headers.append(data_table.item(i, 0).text())
        tab_widget.scatter_pos_forecast.setData(x_plus_forecast, y_plus_forecast)
        tab_widget.scatter_forecast.setData(x_forecast, y_forecast)
        tab_widget.scatter_neg_forecast.setData(x_minus_forecast, y_minus_forecast)

        line1 = graph.Graph(tab_widget.graph_phase_pos)
        text1 = line1.setDots(x_plus, y_plus, "g", tab_widget.graph_phase, vert_headers)
        line2 = graph.Graph(tab_widget.graph_phase_neu)
        text2 = line2.setDots(x_, y_, "y", tab_widget.graph_phase, vert_headers)
        line3 = graph.Graph(tab_widget.graph_phase_neg)
        text3 = line3.setDots(x_minus, y_minus, "b", tab_widget.graph_phase, vert_headers)
        line4 = graph.Graph(tab_widget.graph_phase_pos_forecast)
        text4 = line4.setDots(x_plus_forecast, y_plus_forecast, "g", tab_widget.graph_phase, vert_headers)
        line5 = graph.Graph(tab_widget.graph_phase_neu_forecast)
        text5 = line5.setDots(x_forecast, y_forecast, "y", tab_widget.graph_phase, vert_headers)
        line6 = graph.Graph(tab_widget.graph_phase_neg_forecast)
        text6 = line6.setDots(x_minus_forecast, y_minus_forecast, "b", tab_widget.graph_phase, vert_headers)
        texts = [text3, text2, text1, text6, text5, text4]

        for key, value in tab_widget.dict_chb_graph.items():
            if len(value) > 2:
                value.pop(2)
            idx = list(tab_widget.dict_chb_graph.keys()).index(key)
            value.append(texts[idx])


    def graph_func(self, data_table, tab_widget):
        x_ = []
        x_forecast = []
        y_plus = []
        y_ = []
        y_minus = []

        y_plus_forecast = []
        y_forecast = []
        y_minus_forecast = []

        for i in range(data_table.rowCount()-1):
            x_.append(int(data_table.item(i, 0).text()))
            y_plus.append(float(data_table.item(i, 1).text()))
            y_.append(float(data_table.item(i, 5).text()))
            y_minus.append(float(data_table.item(i, 9).text()))
        for i in range(data_table.rowCount()):
            x_forecast.append(int(data_table.item(i, 0).text()))
            y_plus_forecast.append(float(data_table.item(i, 3).text()))
            y_forecast.append(float(data_table.item(i, 7).text()))
            y_minus_forecast.append(float(data_table.item(i, 11).text()))

        tab_widget.scatter_func_pos.setData(x_,y_plus)
        tab_widget.scatter_func_.setData(x_, y_)
        tab_widget.scatter_func_neg.setData(x_, y_minus)

        tab_widget.scatter_func_pos_forecast.setData(x_forecast, y_plus_forecast)
        tab_widget.scatter_func_forecast.setData(x_forecast, y_forecast)
        tab_widget.scatter_func_neg_forecast.setData(x_forecast, y_minus_forecast)

        vert_headers = []
        for i in range(data_table.rowCount()):
            vert_headers.append(data_table.item(i, 0).text())

        line1 = graph.Graph(tab_widget.graph_func_pos)
        text1 = line1.setDots(x_, y_plus, "g", tab_widget.graph_func, vert_headers)
        line2 = graph.Graph(tab_widget.graph_func_neu)
        text2 = line2.setDots(x_, y_, "y", tab_widget.graph_func, vert_headers)
        line3 = graph.Graph(tab_widget.graph_func_neg)
        text3 = line3.setDots(x_, y_minus, "b", tab_widget.graph_func, vert_headers)
        line4 = graph.Graph(tab_widget.graph_func_pos_forecast)
        text4 = line4.setDots(x_forecast, y_plus_forecast, "g", tab_widget.graph_func, vert_headers)
        line5 = graph.Graph(tab_widget.graph_func_neu_forecast)
        text5 = line5.setDots(x_forecast, y_forecast, "y", tab_widget.graph_func, vert_headers)
        line6 = graph.Graph(tab_widget.graph_func_neg_forecast)
        text6 = line6.setDots(x_forecast, y_minus_forecast, "b", tab_widget.graph_func, vert_headers)
        texts = [text3, text2, text1, text6, text5, text4]

        for key, value in tab_widget.dict_chb_graph_func.items():
            if len(value) > 2:
                value.pop(2)
            idx = list(tab_widget.dict_chb_graph_func.keys()).index(key)
            value.append(texts[idx])

    def open_next_tab(self):
        index = self.ui.tab.currentIndex()
        self.ui.tab.setCurrentIndex(index + 1)
        if index == 1:
            self.ui.widget_third_tab.setEnabled(True)
            self.tab3.tabwidget_main.setCurrentIndex(0)
            self.update_tab3_zerotab()
        elif index == 2:
            self.ui.widget_forth_tab.setEnabled(True)
            self.tab4.widget_tab1.setEnabled(True)
            self.tab4.tabwidget_main.setCurrentIndex(0)
            self.update_tab4_zerotab()

    def update_tab4_zerotab(self):
        self.tab4.combobox_block.clear()

        self.tab4.dict_subblocks.clear()
        self.tab4.dict_subblocks = copy.deepcopy(self.tab3.dict_subblocks)

        for i in self.tab4.dict_subblocks.keys():
            self.tab4.combobox_block.addItem(str(i))
        try:
            self.tab4.listbox_unselected_dots.clear()
            self.tab4.listbox_selected_dots.clear()
        except:
            print("листбоксы пусты")
        for i in range(self.tab3.listbox_all_dots.count()):
            item = self.tab3.listbox_all_dots.item(i)
            self.tab4.listbox_unselected_dots.addItem(item.text())
        if self.tab4.combobox_block.currentText() is not None and self.tab4.combobox_block.currentText() != '':
            for i in self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()]:
                self.tab4.listbox_selected_dots.addItem(str(i))

    def update_tab3_zerotab(self):

        self.tab3.combobox_choose.clear()
        self.tab3.dict_subblocks.clear()

        for i in self.blocks:
            self.tab3.dict_subblocks[i] = []
            self.tab3.combobox_choose.addItem(str(i))

        massive = self.compess_table(self.ui.table_1)
        self.tab3.listbox_all_dots.clear()
        for i in range(len(massive[0])-1):
            self.tab3.listbox_all_dots.addItem(str(massive[0][i+1]))

        if self.tab3.listbox_cont_dots.count() != 0:
            self.tab3.listbox_cont_dots.clear()

    def move_dot_in(self):

        item = self.tab3.listbox_all_dots.currentItem()
        dot = item.text()
        self.tab3.listbox_all_dots.takeItem(self.tab3.listbox_all_dots.row(item))
        self.tab3.listbox_cont_dots.addItem(dot)
        self.tab3.dict_subblocks[self.tab3.combobox_choose.currentText()].append(dot)



    def move_dot_out(self):
        item = self.tab3.listbox_cont_dots.currentItem()
        dot = item.text()
        self.tab3.listbox_cont_dots.takeItem(self.tab3.listbox_cont_dots.row(item))
        self.tab3.listbox_all_dots.addItem(dot)
        self.tab3.dict_subblocks[self.tab3.combobox_choose.currentText()].remove(dot)

    def subblocks_switch(self):
        if self.tab3.combobox_choose.currentText() != '':
            self.tab3.listbox_cont_dots.clear()
            for i in self.tab3.dict_subblocks[self.tab3.combobox_choose.currentText()]:
                self.tab3.listbox_cont_dots.addItem(i)

    def move_dot_in_tab4(self):
        item = self.tab4.listbox_unselected_dots.currentItem()
        dot = item.text()
        self.tab4.listbox_unselected_dots.takeItem(self.tab4.listbox_unselected_dots.row(item))
        self.tab4.listbox_selected_dots.addItem(dot)
        self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()].append(dot)

    def move_dot_out_tab4(self):
        item = self.tab4.listbox_selected_dots.currentItem()
        dot = item.text()
        self.tab4.listbox_selected_dots.takeItem(self.tab4.listbox_selected_dots.row(item))
        self.tab4.listbox_unselected_dots.addItem(dot)
        self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()].remove(dot)

    def subblocks_switch_tab4(self):
        if self.tab4.combobox_block.currentText() is not None and self.tab4.combobox_block.currentText() != '':
            self.tab4.listbox_selected_dots.clear()
            for i in self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()]:
                self.tab4.listbox_selected_dots.addItem(i)

    def button_confirm_settings_tab4(self):
        print("Full - ", len(self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()]))
        print("Divided - ", len(self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()])/2)
        if int(self.tab4.spinbox_count_subblock.text()) < len(self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()])/2:
            self.tab4.groupbox_tab1_center.setEnabled(True)
            self.tab4.dict_subblocks_sub.clear()


            self.tab4.combobox_subblock.clear()
            for i in range(int(self.tab4.spinbox_count_subblock.text())):
                self.tab4.combobox_subblock.addItem(str(i + 1))
                self.tab4.dict_subblocks_sub[str(i+1)] = []

            self.tab4.listbox_available_dots.clear()

            for i in range(self.tab4.listbox_selected_dots.count()):
                item = self.tab4.listbox_selected_dots.item(i).text()
                self.tab4.listbox_available_dots.addItem(item)

        else:
            msg_box = PySide6.QtWidgets.QMessageBox()
            msg_box.setIcon(PySide6.QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Некорректное значение количества подблоков.")
            msg_box.setInformativeText(
                "Для исправления ошибки измените количества блоков.")
            msg_box.setStandardButtons(PySide6.QtWidgets.QMessageBox.Ok)
            msg_box.exec()

    def move_dot_in_tab4_sub(self):
        item = self.tab4.listbox_available_dots.currentItem()
        dot = item.text()
        self.tab4.listbox_available_dots.takeItem(self.tab4.listbox_available_dots.row(item))
        self.tab4.listbox_subblock_dots.addItem(dot)
        self.tab4.dict_subblocks_sub[self.tab4.combobox_subblock.currentText()].append(dot)

    def move_dot_out_tab4_sub(self):
        item = self.tab4.listbox_subblock_dots.currentItem()
        dot = item.text()
        self.tab4.listbox_subblock_dots.takeItem(self.tab4.listbox_subblock_dots.row(item))
        self.tab4.listbox_available_dots.addItem(dot)
        self.tab4.dict_subblocks_sub[self.tab4.combobox_subblock.currentText()].remove(dot)

    def subblocks_switch_tab4_sub(self):
        try:
            if self.tab4.combobox_subblock.currentText() is not None and self.tab4.combobox_subblock.currentText() != '':
                self.tab4.listbox_subblock_dots.clear()

                for i in self.tab4.dict_subblocks_sub[self.tab4.combobox_subblock.currentText()]:
                    self.tab4.listbox_subblock_dots.addItem(i)
        except:
            a = 1


    def button_confirm_20_tab4(self):
        mass = []

        for i in self.tab4.dict_subblocks_sub.keys():
            mass.append(len(self.tab4.dict_subblocks_sub[i]))
        a = mass[0]
        flag = True
        for i in range(len(mass)-1):
            if a != mass[i+1] or a < 2:
                flag = False
                msg_box = PySide6.QtWidgets.QMessageBox()
                msg_box.setIcon(PySide6.QtWidgets.QMessageBox.Critical)
                msg_box.setWindowTitle("Ошибка")
                msg_box.setText("Количество точек в подблоках разное.")
                msg_box.setInformativeText(
                    "Для исправления ошибки измените количества точек.")
                msg_box.setStandardButtons(PySide6.QtWidgets.QMessageBox.Ok)
                msg_box.exec()
                break
        if flag:
            self.tab4.tabwidget_main.setCurrentIndex(1)
            self.tab4.widget_tab2.setEnabled(True)
            self.tab4.combobox_choose_2.clear()
            for index in range(self.tab4.combobox_subblock.count()):
                item_text = self.tab4.combobox_subblock.itemText(index)
                self.tab4.combobox_choose_2.addItem(item_text)
            self.update_tab4_onetab()
            self.tab4.combobox_choose_2.currentTextChanged.connect(self.update_tab4_onetab)

    def update_tab4_onetab(self):
        if self.tab4.combobox_choose_2.currentText() is not None and self.tab4.combobox_choose_2.currentText() != '':

            tabs = [self.tab4]
            for i in tabs:
                for item in i.graph_phase.items():
                    if isinstance(item, pyqtgraph.TextItem):
                        i.graph_phase.removeItem(item)
                for item in i.graph_func.items():
                    if isinstance(item, pyqtgraph.TextItem):
                        i.graph_func.removeItem(item)
            massive = self.massive_from_dots(self.tab4.dict_subblocks_sub[self.tab4.combobox_choose_2.currentText()])

            self.table_phase_headers(self.tab4.table_phase_coor, massive)
            self.table_monit_headers(self.tab4.table_monit, massive)
            self.fill_mu_a(massive, self.tab4.table_phase_coor)
            self.fill_table_monit(self.tab4.table_phase_coor, self.tab4.table_monit)


            self.graph_ph(self.tab4.table_phase_coor, self.tab4)
            self.graph_func(self.tab4.table_phase_coor, self.tab4)
            self.checkbox_on()

    def tab3_button_confirm(self):
        mass = []
        if self.ui.tab.currentIndex() == 2:
            for i in self.tab3.dict_subblocks.keys():
                mass.append(len(self.tab3.dict_subblocks[i]))
            a = mass[0]
            flag = True
            for i in range(len(mass)-1):
                if a != mass[i+1] or a < 2:
                    flag = False
                    msg_box = PySide6.QtWidgets.QMessageBox()
                    msg_box.setIcon(PySide6.QtWidgets.QMessageBox.Critical)
                    msg_box.setWindowTitle("Ошибка")
                    msg_box.setText("Количество точек в подблоках разное.")
                    msg_box.setInformativeText(
                        "Для исправления ошибки измените количества точек.")
                    msg_box.setStandardButtons(PySide6.QtWidgets.QMessageBox.Ok)
                    msg_box.exec()
                    break
            if flag:
                self.tab3.tabwidget_main.setCurrentIndex(1)
                self.tab3.widget_tab2.setEnabled(True)
                self.tab3.combobox_choose_2.clear()
                for index in range(self.tab3.combobox_choose.count()):
                    item_text = self.tab3.combobox_choose.itemText(index)
                    self.tab3.combobox_choose_2.addItem(item_text)
                self.update_tab3_onetab()
                self.tab3.combobox_choose_2.currentTextChanged.connect(self.update_tab3_onetab)
        elif self.ui.tab.currentIndex() == 3:

            for i in self.tab4.dict_subblocks.keys():
                mass.append(len(self.tab4.dict_subblocks[i]))
            a = mass[0]
            flag = True
            for i in range(len(mass) - 1):
                if a != mass[i + 1] or a < 2:
                    flag = False
                    msg_box = PySide6.QtWidgets.QMessageBox()
                    msg_box.setIcon(PySide6.QtWidgets.QMessageBox.Critical)
                    msg_box.setWindowTitle("Ошибка")
                    msg_box.setText("Количество точек в подблоках разное.")
                    msg_box.setInformativeText(
                        "Для исправления ошибки измените количества точек.")
                    msg_box.setStandardButtons(PySide6.QtWidgets.QMessageBox.Ok)
                    msg_box.exec()
                    break
            if flag:
                self.tab4.groupbox_settings.setEnabled(True)
                self.fill_tab4_table()


    def fill_tab4_table(self):

        dots = len(self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()])
        columns = (dots*(dots-1))/2
        self.tab4.table1_tab1.setColumnCount(columns + 1)
        self.tab4.table1_tab1.setRowCount(self.ui.table_1.rowCount())
        self.tab4.table1_tab1.verticalHeader().hide()

        self.tab4.table2_tab1.setColumnCount(self.tab4.table1_tab1.columnCount())
        self.tab4.table2_tab1.setRowCount(self.tab4.table1_tab1.rowCount())
        self.tab4.table2_tab1.verticalHeader().hide()

        massive = self.massive_from_dots(self.tab4.dict_subblocks[self.tab4.combobox_block.currentText()])

        for i in range(len(massive)-1):
            self.tab4.table1_tab1.setItem(i,0,PySide6.QtWidgets.QTableWidgetItem(str(int(massive[i+1][0]))))
            self.tab4.table2_tab1.setItem(i, 0, PySide6.QtWidgets.QTableWidgetItem(str(int(massive[i + 1][0]))))
        self.tab4.table1_tab1.setHorizontalHeaderItem(0,PySide6.QtWidgets.QTableWidgetItem(massive[0][0]))
        self.tab4.table2_tab1.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem(massive[0][0]))

        breker = 0
        col_name = []
        for el_mass in range(len(massive[0]) - 1):
            contr_cell = massive[0][el_mass + 1]
            breker += 1
            for n in range(len(massive[0]) - breker - 1):

                cell = contr_cell + " - " + massive[0][el_mass + 1 + n + 1]
                col_name.append(cell)

        for i in range(self.tab4.table1_tab1.columnCount()-1):
            self.tab4.table1_tab1.setHorizontalHeaderItem(i + 1, PySide6.QtWidgets.QTableWidgetItem(col_name[i]))
            self.tab4.table2_tab1.setHorizontalHeaderItem(i + 1, PySide6.QtWidgets.QTableWidgetItem(col_name[i]))

        for row in range(len(massive)-1):
            breker = 0
            cell_mass = []
            for el_mass in range(len(massive[0])-1):
                contr_cell = massive[row+1][el_mass+1]
                breker += 1

                for n in range(len(massive[row])-breker-1):

                    cell = round(math.fabs(contr_cell - massive[row+1][el_mass+1 + n+1]),4)
                    cell_mass.append(cell)

            for col in range(self.tab4.table1_tab1.columnCount()-1):
                self.tab4.table1_tab1.setItem(row, col + 1, PySide6.QtWidgets.QTableWidgetItem(str(cell_mass[col])))

        full_green = 0
        E = self.my_table.specific_zero_cell("Addition", "E")

        rows = self.tab4.table2_tab1.rowCount()
        for col in range(self.tab4.table2_tab1.columnCount() - 1):
            cell_zero = float(self.tab4.table1_tab1.item(0, col + 1).text())
            cell_green = 0
            for row in range(self.tab4.table2_tab1.rowCount()):
                cell_current = float(self.tab4.table1_tab1.item(row, col + 1).text())
                cell_diff = round(math.fabs(cell_zero - cell_current), 4)
                self.tab4.table2_tab1.setItem(row, col + 1, PySide6.QtWidgets.QTableWidgetItem(str(cell_diff)))

                if cell_diff <= E:
                    self.tab4.table2_tab1.item(row, col+1).setBackground(QtGui.QColor(0, 255, 0))
                    cell_green += 1
                else:
                    self.tab4.table2_tab1.item(row, col+1).setBackground(QtGui.QColor(255, 0, 0, 80))
            if cell_green == rows:
                full_green += 1

        print("Полностью зеленые связи", full_green)

    def update_tab3_onetab(self):
        if self.tab3.combobox_choose_2.currentText() is not None and self.tab3.combobox_choose_2.currentText() != '':
            tabs = [self.tab3]
            for i in tabs:
                for item in i.graph_phase.items():
                    if isinstance(item, pyqtgraph.TextItem):
                        i.graph_phase.removeItem(item)
                for item in i.graph_func.items():
                    if isinstance(item, pyqtgraph.TextItem):
                        i.graph_func.removeItem(item)
            massive = self.massive_from_dots(self.tab3.dict_subblocks[self.tab3.combobox_choose_2.currentText()])
            self.table_phase_headers(self.tab3.table_phase_coor, massive)
            self.table_monit_headers(self.tab3.table_monit, massive)
            self.fill_mu_a(massive, self.tab3.table_phase_coor)
            self.fill_table_monit(self.tab3.table_phase_coor, self.tab3.table_monit)


            self.graph_ph(self.tab3.table_phase_coor, self.tab3)
            self.graph_func(self.tab3.table_phase_coor, self.tab3)
            self.checkbox_on()

    def massive_from_dots(self, massive_headers):
        massive = self.compess_table(self.ui.table_1)
        idx = []
        massive_return = [[] for i in range(len(massive))]
        for i in massive_headers:
            idx.append(massive[0].index(i))

        for i in range(len(massive)):
            massive_return[i].append(massive[i][0])

        for i in range(len(massive)):
            for j in range(len(massive_headers)):
                massive_return[i].append(massive[i][idx[j]])
        return massive_return

    def fill_tab5(self):
        massive = self.compess_table(self.ui.table_1)
        x = []
        head = []
        self.tab5.listbox_all_dots.clear()
        self.tab5.graph_phase.clear()
        self.tab5.dict_chb_graph.clear()
        for i in range(len(massive)-1):
            x.append(massive[i+1][0])
        x.append(self.row_buffer + 1)

        def dot_forecast(mass_y):
            A = decimal.Decimal(str(self.my_table.specific_zero_cell("Addition", "A")))
            mass_y_expanded = copy.deepcopy(mass_y)
            for i in range(len(mass_y) + 1):
                if i == 0:
                    cell_ = decimal.Decimal(str(mass_y[i]))
                    mid_ = decimal.Decimal(str(sum(mass_y) / len(mass_y)))
                    mass_y_expanded[i] = cell_ * A + (1 - A) * mid_
                elif i == len(mass_y):
                    mass_y_expanded.append(
                        decimal.Decimal(str(sum(mass_y_expanded) / len(mass_y_expanded))) * A + (1 - A) * decimal.Decimal(str(mass_y_expanded[
                            len(mass_y) - 1])))
                else:
                    mass_y_expanded[i] = decimal.Decimal(str(mass_y[i])) * A + (1 - A) * decimal.Decimal(str(mass_y_expanded[i - 1]))
            for i in range(len(mass_y_expanded)):
                mass_y_expanded[i] = float(mass_y_expanded[i])
            return mass_y_expanded


        for i in range(len(massive[0])-1):
            chb_item = PySide6.QtWidgets.QCheckBox(str(massive[0][i+1]))
            list_item = PySide6.QtWidgets.QListWidgetItem()
            self.tab5.listbox_all_dots.addItem(list_item)
            self.tab5.listbox_all_dots.setItemWidget(list_item, chb_item)
            y = []
            for j in range(len(massive)-1):
                y.append(massive[j+1][i+1])

            y_ex = dot_forecast(y)
            plot = self.tab5.main_plot.plot(x, y_ex)
            plot.setVisible(False)
            self.tab5.dict_chb_graph[chb_item] = [plot]

            count = 0
            texts = []
            for (xi, yi) in zip(x, y_ex):
                text = pyqtgraph.TextItem(str(int(x[count])), anchor=(0, 1))
                text.setPos(xi, yi)
                self.tab5.graph_phase.addItem(text)
                text.setVisible(False)
                texts.append(text)
                count += 1
            self.tab5.dict_chb_graph[chb_item].append(texts)

        for checkbox in self.tab5.dict_chb_graph.keys():
            checkbox.stateChanged.connect(self.update_plots)

    def update_plots(self):
        for checkbox, plot_text in self.tab5.dict_chb_graph.items():
            plot_text[0].setVisible(checkbox.isChecked())
            for i in plot_text[1]:
                i.setVisible(checkbox.isChecked())
        self.tab5.graph_phase.autoRange()



    def design_table_tab6(self, table):
        massive = self.compess_table(self.ui.table_1)
        add_head = ["\u03BC", "\u03B1 с шумом", "\u03B1 без шума", "Оценка"]
        massive[0].extend(add_head)

        table.setRowCount(len(massive)-1)
        table.setColumnCount(len(massive[0]))
        table.verticalHeader().hide()
        for col in range(len(massive[0])):
            table.setHorizontalHeaderItem(col, PySide6.QtWidgets.QTableWidgetItem(str(massive[0][col])))
        for row in range(len(massive)-1):
            table.setItem(row, 0, PySide6.QtWidgets.QTableWidgetItem(str(int(massive[row+1][0]))))


    def fill_rest_tab6(self):
        self.design_table_tab6(self.tab6.table_rest)
        massive_main = self.compess_table(self.ui.table_1)

        for row in range(len(massive_main)-1):
            self.tab6.table_rest.setItem(row, 0, PySide6.QtWidgets.QTableWidgetItem(str(int(massive_main[row+1][0]))))
            for col in range(len(massive_main[0]) - 1):
                self.tab6.table_rest.setItem(row, col+1, PySide6.QtWidgets.QTableWidgetItem(str(massive_main[1][col+1])))

        massive_rest = []
        headers_rest = []
        for i in range(self.tab6.table_rest.columnCount()-4):
            headers_rest.append(self.tab6.table_rest.horizontalHeaderItem(i).text())
        massive_rest.append(headers_rest)

        for i in range(self.tab6.table_rest.rowCount()):
            row = []
            row.clear()
            for j in range(self.tab6.table_rest.columnCount()-4):
                row.append(float(self.tab6.table_rest.item(i, j).text()))
            massive_rest.append(row)

        mu_a = self.mu_a(massive_rest)

        # С шумом
        for i in range(self.tab6.table_rest.rowCount()):
            self.tab6.table_rest.setItem(i, self.tab6.table_rest.columnCount() - 4,
                                         PySide6.QtWidgets.QTableWidgetItem(str(mu_a[0][i])))
        self.tab6.table_rest.setItem(0, self.tab6.table_rest.columnCount() - 3,
                                     PySide6.QtWidgets.QTableWidgetItem(str(0)))

        for i in range(self.tab6.table_rest.rowCount()-1):
            self.tab6.table_rest.setItem(i+1, self.tab6.table_rest.columnCount() - 3,
                                         PySide6.QtWidgets.QTableWidgetItem(str(mu_a[1][i])))
        self.tab6.table_rest.resizeColumnToContents(self.tab6.table_rest.columnCount() - 3)

        # Без шума
        self.tab6.table_rest.setItem(0, self.tab6.table_rest.columnCount() - 2,
                                     PySide6.QtWidgets.QTableWidgetItem(str(0)))

        for i in range(self.tab6.table_rest.rowCount()-1):
            self.tab6.table_rest.setItem(i+1, self.tab6.table_rest.columnCount() - 2,
                                         PySide6.QtWidgets.QTableWidgetItem(str(round(mu_a[1][i], self.tab6_spinbox_round_value))))

        # Оценка
        E_const = float(self.my_table.specific_zero_cell("Addition", "E"))
        evaluation = []
        for i in range(self.tab6.table_rest.rowCount()):
            cell_standart = float(self.tab6.table_rest.item(i, 1).text())
            cell = float(self.tab6.table_rest.item(i, 1).text())
            delta = math.fabs(cell - cell_standart)
            evaluation.append(delta)

        for i in range(self.tab6.table_rest.rowCount()):
            if evaluation[i] <= E_const:
                self.tab6.table_rest.setItem(i, self.tab6.table_rest.columnCount() - 1,
                                             PySide6.QtWidgets.QTableWidgetItem(str("+")))
                self.tab6.table_rest.item(i, self.tab6.table_rest.columnCount() - 1).setBackground(QtGui.QColor(0, 255, 0))
            else:
                self.tab6.table_rest.setItem(i, self.tab6.table_rest.columnCount() - 1,
                                             PySide6.QtWidgets.QTableWidgetItem(str("-")))
                self.tab6.table_rest.item(i, self.tab6.table_rest.columnCount() - 1).setBackground(
                    QtGui.QColor(255, 0, 0))

    def fill_table_uni_tab6(self):
        self.design_table_tab6(self.tab6.table_uni)
        row_zero = []
        massive = self.compess_table(self.ui.table_1)

        for i in range(len(massive[1])-1):
            row_zero.append(massive[1][i+1])
        for i in range(self.tab6.table_uni.rowCount()):
            for j in range(len(row_zero)):
                self.tab6.table_uni.setItem(i, j + 1, PySide6.QtWidgets.QTableWidgetItem(str(decimal.Decimal(str(row_zero[j])) + self.delta_tab6 * i)))

        self.fill_table_analyze_tab6(self.tab6.table_uni)



    def fill_table_leap_tab6(self):
        self.design_table_tab6(self.tab6.table_leap)
        row_zero = []
        massive = self.compess_table(self.ui.table_1)

        for i in range(len(massive[1]) - 1):
            row_zero.append(massive[1][i + 1])

        for i in range(self.tab6.table_leap.rowCount()):
            for j in range(len(row_zero)):
                self.tab6.table_leap.setItem(i, j + 1, PySide6.QtWidgets.QTableWidgetItem(str(self.tab6.table_uni.item(i, j + 1).text())))

        cent_id = int(self.tab6.table_uni.rowCount() / 2)

        for i in range(len(row_zero)):
            cell = decimal.Decimal(self.tab6.table_leap.item(cent_id, i+1).text())
            self.tab6.table_leap.setItem(cent_id, i + 1, PySide6.QtWidgets.QTableWidgetItem(str(cell + self.delta_tab6 * 8)))
        self.fill_table_analyze_tab6(self.tab6.table_leap)

    def fill_table_cyclic_tab6(self):# Не доделана
        self.design_table_tab6(self.tab6.table_cyclic)
        row_zero = []
        massive = self.compess_table(self.ui.table_1)

        for i in range(len(massive[1]) - 1):
            row_zero.append(massive[1][i + 1])

        for j in range(len(row_zero)):
            self.tab6.table_cyclic.setItem(0, j + 1, PySide6.QtWidgets.QTableWidgetItem(
                str(row_zero[j])))
            self.tab6.table_cyclic.setItem(self.tab6.table_cyclic.rowCount()-1, j + 1, PySide6.QtWidgets.QTableWidgetItem(
                str(row_zero[j])))

        cent_id = int(self.tab6.table_cyclic.rowCount() / 2)
        # if self.tab6.table_cyclic.rowCount() % 2 == 0:
        for i in range(1, cent_id):
            rand = decimal.Decimal(str(random.randint(0, 50) * decimal.Decimal("0.00001")))
            for j in range(len(row_zero)):
                cell =  rand + decimal.Decimal(self.tab6.table_cyclic.item(i-1, j + 1).text())
                self.tab6.table_cyclic.setItem(i, j + 1, PySide6.QtWidgets.QTableWidgetItem(
                    str(cell)))
        rand = decimal.Decimal(str(random.randint(0, 50) * decimal.Decimal("0.00004")))
        for j in range(len(row_zero)):
            cell = rand + decimal.Decimal(self.tab6.table_cyclic.item(cent_id-1, j + 1).text())
            self.tab6.table_cyclic.setItem(cent_id, j + 1, PySide6.QtWidgets.QTableWidgetItem(
                str(cell)))

        for i in range(cent_id+1, self.tab6.table_cyclic.rowCount()-1):
            rand = decimal.Decimal(str(random.randint(0, 50) * decimal.Decimal("0.00001")))
            for j in range(len(row_zero)):
                cell =  decimal.Decimal(self.tab6.table_cyclic.item(i-1, j + 1).text()) - rand
                self.tab6.table_cyclic.setItem(i, j + 1, PySide6.QtWidgets.QTableWidgetItem(
                    str(cell)))

        self.fill_table_analyze_tab6(self.tab6.table_cyclic)

    def fill_table_analyze_tab6(self, table):
        massive_data = []
        headers_rest = []
        for i in range(table.columnCount() - 4):
            headers_rest.append(table.horizontalHeaderItem(i).text())
        massive_data.append(headers_rest)

        for i in range(table.rowCount()):
            row = []
            row.clear()
            for j in range(table.columnCount() - 4):
                row.append(float(table.item(i, j).text()))
            massive_data.append(row)

        mu_a = self.mu_a(massive_data)

        # С шумом
        for i in range(table.rowCount()):
            table.setItem(i, table.columnCount() - 4,
                                         PySide6.QtWidgets.QTableWidgetItem(str(mu_a[0][i])))
        table.setItem(0, table.columnCount() - 3,
                                     PySide6.QtWidgets.QTableWidgetItem(str(0)))

        for i in range(table.rowCount() - 1):
            table.setItem(i + 1, table.columnCount() - 3,
                                         PySide6.QtWidgets.QTableWidgetItem(str(mu_a[1][i])))
        table.resizeColumnToContents(table.columnCount() - 3)

        # Без шума
        table.setItem(0, table.columnCount() - 2,
                                     PySide6.QtWidgets.QTableWidgetItem(str(0)))
        for i in range(table.rowCount() - 1):
            table.setItem(i + 1, table.columnCount() - 2,
                                         PySide6.QtWidgets.QTableWidgetItem(str(decimal.Decimal(str(mu_a[1][i])).quantize(decimal.Decimal(self.tab6_quantize)))))

        # Оценка
        E_const = float(self.my_table.specific_zero_cell("Addition", "E"))
        evaluation = []
        for i in range(table.rowCount()):
            cell_standart = float(self.tab6.table_uni.item(i, 1).text())
            cell = float(table.item(i, 1).text())
            delta_calc = math.fabs(cell - cell_standart)
            evaluation.append(delta_calc)

        for i in range(table.rowCount()):
            if evaluation[i] <= E_const:
                table.setItem(i, table.columnCount() - 1,
                                             PySide6.QtWidgets.QTableWidgetItem(str("+")))
                table.item(i, table.columnCount() - 1).setBackground(
                    QtGui.QColor(0, 255, 0))
            else:
                table.setItem(i, table.columnCount() - 1,
                                             PySide6.QtWidgets.QTableWidgetItem(str("-")))
                table.item(i, table.columnCount() - 1).setBackground(
                    QtGui.QColor(255, 0, 0))

    def fill_tab6_graph(self):
        # Clear
        self.tab6.plot_widget_rest_w_noise.clear()
        self.tab6.plot_widget_rest_wo_noise.clear()
        self.tab6.plot_widget_uni_w_noise.clear()
        self.tab6.plot_widget_uni_wo_noise.clear()
        self.tab6.plot_widget_leap_w_noise.clear()
        self.tab6.plot_widget_leap_wo_noise.clear()
        self.tab6.plot_widget_cyclic_w_noise.clear()
        self.tab6.plot_widget_cyclic_wo_noise.clear()
        # Constants
        row_count = self.tab6.table_rest.rowCount()
        col_mu = self.tab6.table_rest.columnCount() - 4
        col_a_w = self.tab6.table_rest.columnCount() - 3
        col_a_wo = self.tab6.table_rest.columnCount() - 2
        headers = []
        for i in range(row_count):
            headers.append(str(int(self.tab6.table_rest.item(i, 0).text())))

        # tab rest
        x_rest = []
        y_rest_w = []
        y_rest_wo = []

        x_rest.append(float(self.tab6.table_rest.item(0, col_mu).text()))
        y_rest_w.append(float(self.tab6.table_rest.item(0, col_a_w).text()))
        y_rest_wo.append(float(self.tab6.table_rest.item(0, col_a_wo).text()))

        scatter_rest_w = pyqtgraph.ScatterPlotItem(x_rest, y_rest_w)
        scatter_rest_wo = pyqtgraph.ScatterPlotItem(x_rest, y_rest_wo)
        self.tab6.plot_widget_rest_w_noise.addItem(scatter_rest_w, brush="r")
        self.tab6.plot_widget_rest_wo_noise.addItem(scatter_rest_wo, brush="r")

        # tab uni
        x_uni = []
        y_uni_w = []
        y_uni_wo = []

        for i in range(row_count):
            x_uni.append(float(self.tab6.table_uni.item(i, col_mu).text()))
            y_uni_w.append(float(self.tab6.table_uni.item(i, col_a_w).text()))
            y_uni_wo.append(float(self.tab6.table_uni.item(i, col_a_wo).text()))


        uni_w = graph.Graph(self.tab6.plot_widget_uni_w_noise.plot())
        uni_w.setDots(x_uni, y_uni_w, "w", self.tab6.plot_widget_uni_w_noise, headers)

        uni_wo = graph.Graph(self.tab6.plot_widget_uni_wo_noise.plot())
        uni_wo.setDots(x_uni, y_uni_wo, "w", self.tab6.plot_widget_uni_wo_noise, headers)

        # tab leap
        x_leap = []
        y_leap_w = []
        y_leap_wo = []

        for i in range(row_count):
            x_leap.append(float(self.tab6.table_leap.item(i, col_mu).text()))
            y_leap_w.append(float(self.tab6.table_leap.item(i, col_a_w).text()))
            y_leap_wo.append(float(self.tab6.table_leap.item(i, col_a_wo).text()))

        leap_w = graph.Graph(self.tab6.plot_widget_leap_w_noise.plot())
        leap_w.setDots(x_leap, y_leap_w, "w", self.tab6.plot_widget_leap_w_noise, headers)

        leap_wo = graph.Graph(self.tab6.plot_widget_leap_wo_noise.plot())
        leap_wo.setDots(x_leap, y_leap_wo, "w", self.tab6.plot_widget_leap_wo_noise, headers)

        # tab cyclic
        x_cyclic = []
        y_cyclic_w = []
        y_cyclic_wo = []

        for i in range(row_count):
            x_cyclic.append(float(self.tab6.table_cyclic.item(i, col_mu).text()))
            y_cyclic_w.append(float(self.tab6.table_cyclic.item(i, col_a_w).text()))
            y_cyclic_wo.append(float(self.tab6.table_cyclic.item(i, col_a_wo).text()))

        cyclic_w = graph.Graph(self.tab6.plot_widget_cyclic_w_noise.plot())
        cyclic_w.setDots(x_cyclic, y_cyclic_w, "w", self.tab6.plot_widget_cyclic_w_noise, headers)

        cyclic_wo = graph.Graph(self.tab6.plot_widget_cyclic_wo_noise.plot())
        cyclic_wo.setDots(x_cyclic, y_cyclic_wo, "w", self.tab6.plot_widget_cyclic_wo_noise, headers)


if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
