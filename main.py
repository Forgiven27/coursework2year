import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
import pyqtgraph
import sys
import math
import copy
import random
import DataBaseClass
import graph
from TextWindow import HelpWindow
from main_UI import MainWindow_UI
from tab_second import SecondTabUI
from tab_third import ThirdTabUI
from tab_forth import ForthTabUI
from tab_fifth import FifthTabUI


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

        help_open = PySide6.QtGui.QAction("Справка", self.ui.lineEdit_exp)
        help_open.triggered.connect(self.open_help_window)

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



        self.path = None
        self.my_table = None
        self.row_buffer = 0
        self.blocks = []
        self.first_fill_blocks()
        self.ui.button_del_cycle.clicked.connect(self.row_delete)
        self.ui.button_add_cycle.clicked.connect(self.row_add)
        self.ui.button_confirm.clicked.connect(self.button_param_confirm)

        self.tab2.button_recom.clicked.connect(self.rec_box)
        self.tab2.button_next_dec.clicked.connect(self.open_next_tab)
        # self.tab2.button_recom.clicked.connect(lambda :self.clear_all_graph(self.tab2))

        self.tab3.spinbox_count_blocks.textChanged.connect(self.fill_blocks)
        self.tab3.button_confirm.clicked.connect(self.tab3_button_confirm)
        self.tab3.button_next_dec.clicked.connect(self.open_next_tab)

        self.tab4.button_tab10_confirm.clicked.connect(self.tab3_button_confirm)
        self.tab4.button_tab20_confirm.clicked.connect(self.button_confirm_20_tab4)

        self.ui.table_1.verticalHeader().hide()
        self.ui.table_1.setColumnWidth(0, 50)

    def test_functions(self):
        pass

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

    def rec_box(self):
        count = 0
        for i in range(self.tab2.table_monit.rowCount()):
            if self.tab2.table_monit.item(i, 3).text().rfind("Не"):
                count += 1

        if count > self.tab2.table_monit.rowCount() * 0.75 or count < self.tab2.table_monit.rowCount() * 0.2:
            msgbox = PySide6.QtWidgets.QMessageBox()
            msgbox.setText("Полученные данные сильно не надёжны. Рекомендуется изменить параметры/данные")
            msgbox.exec()
        else:
            msgbox = PySide6.QtWidgets.QMessageBox()
            msgbox.setText("Рекомендуется перейти на следующий уровень")
            msgbox.exec()

    def check_box_connect_tab2(self, checked):
        checkbox = self.sender()

        plot_widget = self.tab2.dict_chb_graph[checkbox]
        plot_widget[0].setVisible(checked)
        plot_widget[1].setVisible(checked)
        for text in plot_widget[2]:
            text.setVisible(checked)

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
                    self.ui.lineEdit_error.setText(str(self.my_table.specific_zero_cell(a, "E")))
                    self.ui.lineEdit_exp.setText(str(self.my_table.specific_zero_cell(a, "A")))

                    msgbox = PySide6.QtWidgets.QMessageBox()
                    msgbox.setText("Параметры добавлены")
                    msgbox.exec()

    def button_param_confirm(self):
        if self.ui.lineEdit_exp.text() != '':
            a = float(self.ui.lineEdit_exp.text())
            b = float(self.ui.lineEdit_error.text())
            if a > 1 or a < 0:
                msgbox = PySide6.QtWidgets.QMessageBox()
                msgbox.critical(self.ui.widget_first_tab, "Параметр некорректен", "Измените параметр")
            else:
                self.my_table.update_cell("Addition", "A", "id", 0, a)
                self.my_table.update_cell("Addition", "E", "id", 0, b)
                self.update_tab2()

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
            self.ui.table_1.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)

    def update_tab2(self):
        self.ui.widget_third_tab.setEnabled(False)
        self.ui.widget_forth_tab.setEnabled(False)
        self.tab3.widget_tab2.setEnabled(False)
        self.tab4.widget_tab1.setEnabled(False)
        self.tab4.widget_tab2.setEnabled(False)
        self.tab4.groupbox_settings.setEnabled(False)
        self.tab4.groupbox_tab1_center.setEnabled(False)

        self.fill_tab5()

        self.table_phase_headers(self.tab2.table_phase_coor, self.compess_table())
        self.table_monit_headers(self.tab2.table_monit, self.compess_table())
        self.fill_mu_a(self.compess_table(), self.tab2.table_phase_coor)
        self.fill_table_monit(self.tab2.table_phase_coor, self.tab2.table_monit)
        #self.clear_all_graph(self.tab2)

        self.graph_ph(self.tab2.table_phase_coor, self.tab2)
        self.graph_func(self.tab2.table_phase_coor, self.tab2)


    def clear_all_graph(self, tab_widget):
        self.clear_text_items(tab_widget.graph_phase)

    def clear_text_items(self, plot_widget):
        items_to_remove = []
        # print(type(plot_widget.getPlotItem().items()))
        a = plot_widget.getPlotItem()
        v = type(a.items())
        print(v)
        # for item in plot_widget.getPlotItem().items():
        #     if isinstance(item, pyqtgraph.TextItem):
        #         items_to_remove.append(item)
        # for item in items_to_remove:
        #     plot_widget.removeItem(item)

    def compess_table(self):
        massive = []
        headers = []
        for i in range(self.ui.table_1.columnCount()):
                headers.append(self.ui.table_1.horizontalHeaderItem(i).text())
        massive.append(headers)

        for i in range(self.ui.table_1.rowCount()):
            row = []
            row.clear()
            for j in range(self.ui.table_1.columnCount()):
                row.append(float(self.ui.table_1.item(i, j).text()))
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
        sum_mu = 0

        for i in range(len(massive)-1):
            for j in range(len(massive[0])-1):
                sum_mu += math.pow(massive[i+1][j+1], 2)
            mu_a[0].append(math.sqrt(sum_mu))
        sum_a = 0

        for i in range(len(massive)-2):
            for j in range(len(massive[0])-1):
                sum_a += (massive[i+1][j+1] * massive[i+2][j+1])
            a = math.acos(sum_a / (mu_a[0][i] * mu_a[0][i+1]))
            mu_a[1].append(a)
        return mu_a

    def fill_mu_a(self, massive, table):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()-1):
                table.setItem(row, col+1, PySide6.QtWidgets.QTableWidgetItem(""))


        massive_plus = copy.deepcopy(massive)
        massive_minus = copy.deepcopy(massive)
        e1 = 0.0005
        e2 = float(self.my_table.specific_zero_cell("Addition", "E"))
        E = e1+e2
        A = float(self.my_table.specific_zero_cell("Addition", "A"))

        for i in range(len(massive)-1):
            for j in range(len(massive[0])-1):
                a = float(massive[i+1][j+1])

                massive_plus[i+1][j+1] = a + E
                massive_minus[i+1][j+1] = a - E

        mu_a_plus = self.mu_a(massive_plus)
        mu_a_ = self.mu_a(massive)
        mu_a_minus = self.mu_a(massive_minus)

        mu_a_plus_forecast = mu_a_plus
        mu_a_forecast = mu_a_
        mu_a_minus_forecast = mu_a_minus


        for j in range(len(mu_a_)):
            for i in range(len(mu_a_[j]) + 1):
                if i == 0:
                    mu_a_plus_forecast[j][i] = mu_a_plus[j][i] * A + (1 - A) * (sum(mu_a_plus[j]) / len(mu_a_plus[j]))
                    mu_a_forecast[j][i] = mu_a_[j][i] * A + (1 - A) * (sum(mu_a_[j]) / len(mu_a_[j]))
                    mu_a_minus_forecast[j][i] = mu_a_minus[j][i] * A + (1 - A) * (
                                sum(mu_a_minus[j]) / len(mu_a_minus[j]))
                elif i == len(mu_a_[j]):
                    mu_a_plus_forecast[j].append(
                        (sum(mu_a_plus_forecast[j]) / len(mu_a_plus_forecast[j])) * A + (1 - A) * mu_a_plus_forecast[j][
                            len(mu_a_[j]) - 1])
                    mu_a_minus_forecast[j].append(
                        (sum(mu_a_minus_forecast[j]) / len(mu_a_minus_forecast[j])) * A + (1 - A) *
                        mu_a_minus_forecast[j][len(mu_a_[j]) - 1])
                    mu_a_forecast[j].append(
                        (sum(mu_a_forecast[j]) / len(mu_a_forecast[j])) * A + (1 - A) * mu_a_forecast[j][
                            len(mu_a_[j]) - 1])

                else:
                    mu_a_plus_forecast[j][i] = mu_a_plus[j][i] * A + (1 - A) * mu_a_plus_forecast[j][i - 1]
                    mu_a_forecast[j][i] = mu_a_[j][i] * A + (1 - A) * mu_a_forecast[j][i - 1]
                    mu_a_minus_forecast[j][i] = mu_a_minus[j][i] * A + (1 - A) * mu_a_minus_forecast[j][i - 1]

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

        tab_widget.scatter_pos_forecast.setData(x_plus_forecast, y_plus_forecast)
        tab_widget.scatter_forecast.setData(x_forecast, y_forecast)
        tab_widget.scatter_neg_forecast.setData(x_minus_forecast, y_minus_forecast)

        line1 = graph.Graph(tab_widget.graph_phase_pos)
        text1 = line1.setDots(x_plus, y_plus, "g", tab_widget.graph_phase)
        line2 = graph.Graph(tab_widget.graph_phase_neu)
        text2 = line2.setDots(x_, y_, "y", tab_widget.graph_phase)
        line3 = graph.Graph(tab_widget.graph_phase_neg)
        text3 = line3.setDots(x_minus, y_minus, "b", tab_widget.graph_phase)
        line4 = graph.Graph(tab_widget.graph_phase_pos_forecast)
        text4 = line4.setDots(x_plus_forecast, y_plus_forecast, "g", tab_widget.graph_phase)
        line5 = graph.Graph(tab_widget.graph_phase_neu_forecast)
        text5 = line5.setDots(x_forecast, y_forecast, "y", tab_widget.graph_phase)
        line6 = graph.Graph(tab_widget.graph_phase_neg_forecast)
        text6 = line6.setDots(x_minus_forecast, y_minus_forecast, "b", tab_widget.graph_phase)
        texts = [text3, text2, text1, text6, text5, text4]

        for key, value in tab_widget.dict_chb_graph.items():
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

        line1 = graph.Graph(tab_widget.graph_func_pos)
        text1 = line1.setDots(x_, y_plus, "g", tab_widget.graph_func)
        line2 = graph.Graph(tab_widget.graph_func_neu)
        text2 = line2.setDots(x_, y_, "y", tab_widget.graph_func)
        line3 = graph.Graph(tab_widget.graph_func_neg)
        text3 = line3.setDots(x_, y_minus, "b", tab_widget.graph_func)
        line4 = graph.Graph(tab_widget.graph_func_pos_forecast)
        text4 = line4.setDots(x_forecast, y_plus_forecast, "g", tab_widget.graph_func)
        line5 = graph.Graph(tab_widget.graph_func_neu_forecast)
        text5 = line5.setDots(x_forecast, y_forecast, "y", tab_widget.graph_func)
        line6 = graph.Graph(tab_widget.graph_func_neg_forecast)
        text6 = line6.setDots(x_forecast, y_minus_forecast, "b", tab_widget.graph_func)
        texts = [text3, text2, text1, text6, text5, text4]

        for key, value in tab_widget.dict_chb_graph_func.items():
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

        # self.tab4.listbox_unselected_dots.itemClicked.connect(self.move_dot_in_tab4)
        # self.tab4.listbox_selected_dots.itemClicked.connect(self.move_dot_out_tab4)
        # self.tab4.combobox_block.currentTextChanged.connect(self.subblocks_switch_tab4)





    def update_tab3_zerotab(self):

        self.tab3.combobox_choose.clear()
        self.tab3.dict_subblocks.clear()

        for i in self.blocks:
            self.tab3.dict_subblocks[i] = []
            self.tab3.combobox_choose.addItem(str(i))

        massive = self.compess_table()
        self.tab3.listbox_all_dots.clear()
        for i in range(len(massive[0])-1):
            self.tab3.listbox_all_dots.addItem(str(massive[0][i+1]))

        if self.tab3.listbox_cont_dots.count() != 0:
            self.tab3.listbox_cont_dots.clear()
        # self.tab3.listbox_all_dots.itemClicked.connect(self.move_dot_in)
        # self.tab3.listbox_cont_dots.itemClicked.connect(self.move_dot_out)
        # self.tab3.combobox_choose.currentTextChanged.connect(self.subblocks_switch)

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
        if self.tab4.lineedit_count_cont_dots.text() != '' and int(self.tab4.lineedit_count_cont_dots.text()) > 1:
            self.tab4.groupbox_tab1_center.setEnabled(True)
            self.tab4.dict_subblocks_sub.clear()


            self.tab4.combobox_subblock.clear()
            for i in range(int(self.tab4.spinbox_count_subblock.text())):
                self.tab4.combobox_subblock.addItem(str(i + 1))
                self.tab4.dict_subblocks_sub[str(i+1)] = []
            print(self.tab4.dict_subblocks_sub)
            self.tab4.listbox_available_dots.clear()

            for i in range(self.tab4.listbox_selected_dots.count()):
                item = self.tab4.listbox_selected_dots.item(i).text()
                self.tab4.listbox_available_dots.addItem(item)

        else:
            msg_box = PySide6.QtWidgets.QMessageBox()
            msg_box.setIcon(PySide6.QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Некорректное значение количества точек в подблоке.")
            msg_box.setInformativeText(
                "Для исправления ошибки измените количества точек.")
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
            massive = self.massive_from_dots(self.tab4.dict_subblocks_sub[self.tab4.combobox_choose_2.currentText()])

            self.table_phase_headers(self.tab4.table_phase_coor, massive)
            self.table_monit_headers(self.tab4.table_monit, massive)
            self.fill_mu_a(massive, self.tab4.table_phase_coor)
            self.fill_table_monit(self.tab4.table_phase_coor, self.tab4.table_monit)
            # self.clear_all_graph(self.tab2)

            self.graph_ph(self.tab4.table_phase_coor, self.tab4)
            self.graph_func(self.tab4.table_phase_coor, self.tab4)














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
                print(massive[0][el_mass + 1], massive[0][el_mass + 1 + n + 1])
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
                    print(massive[0][el_mass+1], massive[0][el_mass+1 + n+1])
                    cell = round(math.fabs(contr_cell - massive[row+1][el_mass+1 + n+1]),4)
                    cell_mass.append(cell)

            for col in range(self.tab4.table1_tab1.columnCount()-1):
                self.tab4.table1_tab1.setItem(row, col + 1, PySide6.QtWidgets.QTableWidgetItem(str(cell_mass[col])))

        full_green = 0
        E = self.my_table.specific_zero_cell("Addition", "E")
        print("E = ", E)
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
            massive = self.massive_from_dots(self.tab3.dict_subblocks[self.tab3.combobox_choose_2.currentText()])
            self.table_phase_headers(self.tab3.table_phase_coor, massive)
            self.table_monit_headers(self.tab3.table_monit, massive)
            self.fill_mu_a(massive, self.tab3.table_phase_coor)
            self.fill_table_monit(self.tab3.table_phase_coor, self.tab3.table_monit)
            # self.clear_all_graph(self.tab2)

            self.graph_ph(self.tab3.table_phase_coor, self.tab3)
            self.graph_func(self.tab3.table_phase_coor, self.tab3)

    def massive_from_dots(self, massive_headers):
        massive = self.compess_table()
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
        massive = self.compess_table()
        x = []
        for i in range(len(massive)-1):
            x.append(massive[i+1][0])
        for i in range(len(massive[0])-1):
            chb_item = PySide6.QtWidgets.QCheckBox(str(massive[0][i+1]))
            list_item = PySide6.QtWidgets.QListWidgetItem()
            self.tab5.listbox_all_dots.addItem(list_item)
            self.tab5.listbox_all_dots.setItemWidget(list_item, chb_item)
            y = []
            for j in range(len(massive)-1):
                y.append(massive[j+1][i+1])
            print(x, y, sep="\n")
            plot = self.tab5.main_plot.plot(x, y)
            plot.setVisible(False)
            self.tab5.dict_chb_graph[chb_item] = plot

        for checkbox in self.tab5.dict_chb_graph.keys():
            checkbox.stateChanged.connect(self.update_plots)

    def update_plots(self):
        for checkbox, plot in self.tab5.dict_chb_graph.items():
            plot.setVisible(checkbox.isChecked())
            print(checkbox.isChecked())


if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()


    sys.exit(app.exec())
