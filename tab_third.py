import PySide6
from PySide6 import QtWidgets
import pyqtgraph


class ThirdTabUI(object):
    def setupUi(self, QWidget):
        QWidget.setEnabled(False)
        # Главный слой
        self.main_horlay = PySide6.QtWidgets.QHBoxLayout()
        self.tabwidget_main = PySide6.QtWidgets.QTabWidget()

        # Табвиджет "Распределение контрольных точек по блокам"
        self.widget_tab1 = PySide6.QtWidgets.QWidget()
        self.layout_tab1 = PySide6.QtWidgets.QHBoxLayout()

        # Left
        self.layout_left_tab1 = PySide6.QtWidgets.QVBoxLayout()

        self.layout_grid = PySide6.QtWidgets.QGridLayout()
        self.label_choose_1 = PySide6.QtWidgets.QLabel("Выберите блок")
        self.label_all_dots = PySide6.QtWidgets.QLabel("Все контрольные точки объекта")
        self.label_cont_dots = PySide6.QtWidgets.QLabel("Контрольные точки блока")
        self.combobox_choose = PySide6.QtWidgets.QComboBox()
        self.listbox_all_dots = PySide6.QtWidgets.QListWidget()
        self.listbox_cont_dots = PySide6.QtWidgets.QListWidget()
        self.button_confirm = PySide6.QtWidgets.QPushButton("Подтвердить")

        self.label_count_blocks = PySide6.QtWidgets.QLabel("Количество блоков")
        self.spinbox_count_blocks = PySide6.QtWidgets.QSpinBox()
        self.spinbox_count_blocks.setMinimum(2)


        self.dict_subblocks = {}

        self.layout_spinbox = PySide6.QtWidgets.QHBoxLayout()
        self.layout_spinbox.addWidget(self.label_count_blocks)
        self.layout_spinbox.addWidget(self.spinbox_count_blocks)

        self.layout_top = PySide6.QtWidgets.QVBoxLayout()
        self.layout_top.addWidget(self.label_choose_1)
        self.layout_top.addWidget(self.combobox_choose)

        self.layout_center = PySide6.QtWidgets.QHBoxLayout()
        self.layout_center_left = PySide6.QtWidgets.QVBoxLayout()
        self.layout_center_right = PySide6.QtWidgets.QVBoxLayout()
        self.layout_center_left.addWidget(self.label_all_dots)
        self.layout_center_left.addWidget(self.listbox_all_dots)
        self.layout_center_right.addWidget(self.label_cont_dots)
        self.layout_center_right.addWidget(self.listbox_cont_dots)

        self.layout_center.addLayout(self.layout_center_left,1)
        self.layout_center.addLayout(self.layout_center_right,1)

        self.layout_bottom = PySide6.QtWidgets.QHBoxLayout()
        self.layout_bottom.addWidget(self.button_confirm)

        self.layout_left_tab1.addLayout(self.layout_spinbox)
        self.layout_left_tab1.addLayout(self.layout_top)
        self.layout_left_tab1.addLayout(self.layout_center)
        self.layout_left_tab1.addLayout(self.layout_bottom)

        # Right
        self.groupbox_pict = PySide6.QtWidgets.QGroupBox("Схема техногенного объекта")

        self.layout_pict = PySide6.QtWidgets.QHBoxLayout()
        self.label_pict = PySide6.QtWidgets.QLabel()
        self.layout_pict.addWidget(self.label_pict)
        self.groupbox_pict.setLayout(self.layout_pict)

        # Табвиджет "Расчеты и графики"
        self.widget_tab2 = PySide6.QtWidgets.QWidget()
        self.layout_tab2 = PySide6.QtWidgets.QHBoxLayout()
        self.widget_tab2.setLayout(self.layout_tab2)

        # Выбор блока
        self.layout_choose_2 = PySide6.QtWidgets.QHBoxLayout()
        self.label_choose_2 = PySide6.QtWidgets.QLabel("Выберите блок")
        self.combobox_choose_2 = PySide6.QtWidgets.QComboBox()
        self.layout_choose_2.addWidget(self.label_choose_2)
        self.layout_choose_2.addWidget(self.combobox_choose_2)



        # Гроупбокс "Фазовые координаты"
        self.groupbox_phase_coor = PySide6.QtWidgets.QGroupBox("Фазовые координаты")
        self.table_phase_coor = PySide6.QtWidgets.QTableWidget()
        self.layout_phase_coor = PySide6.QtWidgets.QHBoxLayout()
        self.layout_phase_coor.addWidget(self.table_phase_coor)
        self.groupbox_phase_coor.setLayout(self.layout_phase_coor)

        # Гроупбокс "Мониторинг состояния объекта"
        self.groupbox_monit = PySide6.QtWidgets.QGroupBox("Мониторинг состояния")
        self.table_monit = PySide6.QtWidgets.QTableWidget()
        self.layout_monit = PySide6.QtWidgets.QHBoxLayout()
        self.layout_monit.addWidget(self.table_monit)
        self.groupbox_monit.setLayout(self.layout_monit)

        # Табвиджет создание
        self.tabwidget_inserted = PySide6.QtWidgets.QTabWidget()

        # Табвиджет виджет "Фазовые траектории"
        # <График альфа
        self.graph_phase = graph_phase = pyqtgraph.PlotWidget()
        self.graph_phase.addLegend()

        self.graph_phase.setLabel("left", "\u03B1", **{'color': '#EEE', 'font-size': '14pt'})
        self.graph_phase.setLabel("bottom", "\u03BC", **{'color': '#EEE', 'font-size': '14pt'})

        self.scatter_pos = pyqtgraph.ScatterPlotItem(symbol='o', brush='g', size=10)  # Красные точки
        self.graph_phase.addItem(self.scatter_pos)
        self.scatter_ = pyqtgraph.ScatterPlotItem(symbol='o', brush='y', size=10)  # Желтые точки
        self.graph_phase.addItem(self.scatter_)
        self.scatter_neg = pyqtgraph.ScatterPlotItem(symbol='o', brush='b', size=10)  # Красные точки
        self.graph_phase.addItem(self.scatter_neg)

        self.graph_phase_pos = graph_phase.plot(name="\u03B1(\u03BC)+")
        self.graph_phase_neu = graph_phase.plot(name="\u03B1(\u03BC)")
        self.graph_phase_neg = graph_phase.plot(name="\u03B1(\u03BC)-")

        self.scatter_pos_forecast = pyqtgraph.ScatterPlotItem(symbol='o', brush='b', size=10)
        self.graph_phase.addItem(self.scatter_pos_forecast)
        self.scatter_forecast = pyqtgraph.ScatterPlotItem(symbol='o', brush='r', size=10)
        self.graph_phase.addItem(self.scatter_forecast)
        self.scatter_neg_forecast = pyqtgraph.ScatterPlotItem(symbol='o', brush='w', size=10)
        self.graph_phase.addItem(self.scatter_neg_forecast)

        self.graph_phase_pos_forecast = graph_phase.plot(name="\u03B1(\u03BC)+")
        self.graph_phase_neu_forecast = graph_phase.plot(name="\u03B1(\u03BC)")
        self.graph_phase_neg_forecast = graph_phase.plot(name="\u03B1(\u03BC)-")

        # <Гроупбокс "Параметры графиков"
        self.groupbox_phase_param = PySide6.QtWidgets.QGroupBox("Параметры графиков")
        self.checkbox_phase_param_00 = PySide6.QtWidgets.QCheckBox("\u03B1(\u03BC)-")
        self.checkbox_phase_param_01 = PySide6.QtWidgets.QCheckBox("Прогноз \u03B1(\u03BC)-")
        self.checkbox_phase_param_10 = PySide6.QtWidgets.QCheckBox("\u03B1(\u03BC)")
        self.checkbox_phase_param_11 = PySide6.QtWidgets.QCheckBox("Прогноз \u03B1(\u03BC)")
        self.checkbox_phase_param_20 = PySide6.QtWidgets.QCheckBox("\u03B1(\u03BC)+")
        self.checkbox_phase_param_21 = PySide6.QtWidgets.QCheckBox("Прогноз \u03B1(\u03BC)+")
        self.button_phase_clean = PySide6.QtWidgets.QPushButton("Убрать всё")

        self.layout_grid_phase = PySide6.QtWidgets.QGridLayout()
        self.layout_grid_phase.addWidget(self.checkbox_phase_param_00, 0, 0)
        self.layout_grid_phase.addWidget(self.checkbox_phase_param_01, 0, 1)
        self.layout_grid_phase.addWidget(self.checkbox_phase_param_10, 1, 0)
        self.layout_grid_phase.addWidget(self.checkbox_phase_param_11, 1, 1)
        self.layout_grid_phase.addWidget(self.checkbox_phase_param_20, 2, 0)
        self.layout_grid_phase.addWidget(self.checkbox_phase_param_21, 2, 1)
        self.layout_grid_phase.addWidget(self.button_phase_clean, 0, 4)

        self.groupbox_phase_param.setLayout(self.layout_grid_phase)

        self.widget_phase = PySide6.QtWidgets.QWidget()
        self.layout_vert_phase = PySide6.QtWidgets.QVBoxLayout()
        self.layout_vert_phase.addWidget(self.graph_phase)
        self.layout_vert_phase.addWidget(self.groupbox_phase_param)
        self.widget_phase.setLayout(self.layout_vert_phase)
        self.tabwidget_inserted.addTab(self.widget_phase, "Фазовые траектории \u03B1(\u03BC)")

        self.dict_chb_graph = {self.checkbox_phase_param_00: [self.graph_phase_neg, self.scatter_neg],
                               self.checkbox_phase_param_10: [self.graph_phase_neu, self.scatter_],
                               self.checkbox_phase_param_20: [self.graph_phase_pos, self.scatter_pos],
                               self.checkbox_phase_param_01: [self.graph_phase_neg_forecast, self.scatter_neg_forecast],
                               self.checkbox_phase_param_11: [self.graph_phase_neu_forecast, self.scatter_forecast],
                               self.checkbox_phase_param_21: [self.graph_phase_pos_forecast, self.scatter_pos_forecast]
                               }

        # Табвиджет виджет "Функция"
        # <График ню
        self.graph_func = graph_func = pyqtgraph.PlotWidget()
        self.graph_func_neg = graph_func.plot(name="\u03BC(t)-")
        self.graph_func_neu = graph_func.plot(name="\u03BC(t)")
        self.graph_func_pos = graph_func.plot(name="\u03BC(t)+")

        self.graph_func.setLabel("left", "\u03BC", **{'color': '#EEE', 'font-size': '14pt'})
        self.graph_func.setLabel("bottom", "Цикл наблюдения (t)", **{'color': '#EEE', 'font-size': '10pt'})

        self.scatter_func_pos = pyqtgraph.ScatterPlotItem(symbol='o', brush='g', size=10)  # Красные точки
        self.graph_func.addItem(self.scatter_func_pos)
        self.scatter_func_ = pyqtgraph.ScatterPlotItem(symbol='o', brush='y', size=10)  # Желтые точки
        self.graph_func.addItem(self.scatter_func_)
        self.scatter_func_neg = pyqtgraph.ScatterPlotItem(symbol='o', brush='b', size=10)  # Красные точки
        self.graph_func.addItem(self.scatter_func_neg)

        self.graph_func_pos = graph_func.plot(name="\u03B1(\u03BC)+")
        self.graph_func_neu = graph_func.plot(name="\u03B1(\u03BC)")
        self.graph_func_neg = graph_func.plot(name="\u03B1(\u03BC)-")

        self.scatter_func_pos_forecast = pyqtgraph.ScatterPlotItem(symbol='o', brush='b', size=10)
        self.graph_func.addItem(self.scatter_func_pos_forecast)
        self.scatter_func_forecast = pyqtgraph.ScatterPlotItem(symbol='o', brush='r', size=10)
        self.graph_func.addItem(self.scatter_func_forecast)
        self.scatter_func_neg_forecast = pyqtgraph.ScatterPlotItem(symbol='o', brush='w', size=10)
        self.graph_func.addItem(self.scatter_func_neg_forecast)

        self.graph_func_pos_forecast = graph_func.plot(name="\u03B1(\u03BC)+")
        self.graph_func_neu_forecast = graph_func.plot(name="\u03B1(\u03BC)")
        self.graph_func_neg_forecast = graph_func.plot(name="\u03B1(\u03BC)-")

        # <Гроупбокс "Параметры графиков"
        self.groupbox_func_param = PySide6.QtWidgets.QGroupBox("Параметры графиков")
        self.checkbox_func_param_00 = PySide6.QtWidgets.QCheckBox("\u03BC(t)-")
        self.checkbox_func_param_01 = PySide6.QtWidgets.QCheckBox("Прогноз \u03BC(t)-")
        self.checkbox_func_param_10 = PySide6.QtWidgets.QCheckBox("\u03BC(t)")
        self.checkbox_func_param_11 = PySide6.QtWidgets.QCheckBox("Прогноз \u03BC(t)")
        self.checkbox_func_param_20 = PySide6.QtWidgets.QCheckBox("\u03BC(t)+")
        self.checkbox_func_param_21 = PySide6.QtWidgets.QCheckBox("Прогноз \u03BC(t)+")
        self.button_func_clean = PySide6.QtWidgets.QPushButton("Убрать всё")

        self.dict_chb_graph_func = {self.checkbox_func_param_00: [self.graph_func_neg, self.scatter_func_neg],
                                    self.checkbox_func_param_10: [self.graph_func_neu, self.scatter_func_],
                                    self.checkbox_func_param_20: [self.graph_func_pos, self.scatter_func_pos],
                                    self.checkbox_func_param_01: [self.graph_func_neg_forecast,
                                                                  self.scatter_func_neg_forecast],
                                    self.checkbox_func_param_11: [self.graph_func_neu_forecast,
                                                                  self.scatter_func_forecast],
                                    self.checkbox_func_param_21: [self.graph_func_pos_forecast,
                                                                  self.scatter_func_pos_forecast]
                                    }


        self.layout_grid_func = PySide6.QtWidgets.QGridLayout()
        self.layout_grid_func.addWidget(self.checkbox_func_param_00, 0, 0)
        self.layout_grid_func.addWidget(self.checkbox_func_param_01, 0, 1)
        self.layout_grid_func.addWidget(self.checkbox_func_param_10, 1, 0)
        self.layout_grid_func.addWidget(self.checkbox_func_param_11, 1, 1)
        self.layout_grid_func.addWidget(self.checkbox_func_param_20, 2, 0)
        self.layout_grid_func.addWidget(self.checkbox_func_param_21, 2, 1)
        self.layout_grid_func.addWidget(self.button_func_clean, 0, 4)

        self.groupbox_func_param.setLayout(self.layout_grid_func)

        self.widget_func = PySide6.QtWidgets.QWidget()
        self.layout_vert_func = PySide6.QtWidgets.QVBoxLayout()
        self.layout_vert_func.addWidget(self.graph_func)
        self.layout_vert_func.addWidget(self.groupbox_func_param)
        self.widget_func.setLayout(self.layout_vert_func)
        self.tabwidget_inserted.addTab(self.widget_func, "Функция \u03BC(t)")

        # Гроубокс "Переход на второй уровень декомпозиции"
        self.layout_next_dec = PySide6.QtWidgets.QHBoxLayout()
        self.groupbox_next_dec = PySide6.QtWidgets.QGroupBox("Переход на третий уровень декомпозиции")
        self.button_recom = PySide6.QtWidgets.QPushButton("Рекомендации")
        self.button_next_dec = PySide6.QtWidgets.QPushButton("Перейти на третий уровень декомпозиции")

        self.layout_next_dec.addWidget(self.button_recom)
        self.layout_next_dec.addWidget(self.button_next_dec)
        self.groupbox_next_dec.setLayout(self.layout_next_dec)

        # Слой левый + заполнение
        self.layout_left_tab2 = PySide6.QtWidgets.QVBoxLayout()
        self.layout_left_tab2.addLayout(self.layout_choose_2)
        self.layout_left_tab2.addWidget(self.groupbox_phase_coor)
        self.layout_left_tab2.addWidget(self.groupbox_monit)

        # Слой правый
        self.layout_right_tab2 = PySide6.QtWidgets.QVBoxLayout()
        self.layout_right_tab2.addWidget(self.tabwidget_inserted)
        self.layout_right_tab2.addWidget(self.groupbox_next_dec)

        # Блокировка ячеек
        self.table_monit.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)
        self.table_phase_coor.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)

        # Сборка таб 2
        self.layout_tab2.addLayout(self.layout_left_tab2)
        self.layout_tab2.addLayout(self.layout_right_tab2)

        # Сборка таб 1
        self.layout_tab1.addLayout(self.layout_left_tab1, 2)
        self.layout_tab1.addWidget(self.groupbox_pict, 3)
        self.widget_tab1.setLayout(self.layout_tab1)

        self.tabwidget_main.addTab(self.widget_tab1, "Распределение контрольных точек по блокам")
        self.tabwidget_main.addTab(self.widget_tab2, "Расчеты и функции")
        self.main_horlay.addWidget(self.tabwidget_main)
        QWidget.setLayout(self.main_horlay)
