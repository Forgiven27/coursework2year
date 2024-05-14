import PySide6
from PySide6 import QtWidgets,QtGui

class MainWindow_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Курсовая работа Мищенко М")

        # self.menu_bar = PySide6.QtWidgets.QMenuBar().addMenu("Help")
        self.tab = PySide6.QtWidgets.QTabWidget()
        self.menubar = MainWindow.menuBar()
        self.help_button = self.menubar.addMenu('Help')
        # Group box db 1 page
        self.button_choose_db = PySide6.QtWidgets.QPushButton("Выбрать БД")
        self.button_open_table = PySide6.QtWidgets.QPushButton("Открыть таблицу")
        self.label_choose_db = PySide6.QtWidgets.QLabel("Выбрать данные")
        self.combobox_choose_db = PySide6.QtWidgets.QComboBox()

        self.layout_label_comb = PySide6.QtWidgets.QHBoxLayout()
        self.layout_label_comb.addWidget(self.label_choose_db)
        self.layout_label_comb.addWidget(self.combobox_choose_db, 1)

        self.layout_gb_db = PySide6.QtWidgets.QVBoxLayout()
        self.layout_gb_db.addWidget(self.button_choose_db)
        self.layout_gb_db.addLayout(self.layout_label_comb)
        self.layout_gb_db.addWidget(self.button_open_table)

        self.groupbox_db = PySide6.QtWidgets.QGroupBox("База данных")
        self.groupbox_db.setLayout(self.layout_gb_db)

        # Group box Cycle 1 page
        self.button_add_cycle = PySide6.QtWidgets.QPushButton("Добавить цикл наблюдения")
        self.button_del_cycle = PySide6.QtWidgets.QPushButton("Удалить цикл наблюдения")

        self.layout_cycle = PySide6.QtWidgets.QVBoxLayout()
        self.layout_cycle.addWidget(self.button_add_cycle)
        self.layout_cycle.addWidget(self.button_del_cycle)

        self.groupbox_cycle = PySide6.QtWidgets.QGroupBox("Имитационное моделирование")
        self.groupbox_cycle.setLayout(self.layout_cycle)

        # Group box param 1 page
        self.label_exp = PySide6.QtWidgets.QLabel("Коэффициент экспоненциального сглаживания")
        self.label_error = PySide6.QtWidgets.QLabel("Погрешность измерения")
        self.button_confirm = PySide6.QtWidgets.QPushButton("Применить")
        self.lineEdit_exp = PySide6.QtWidgets.QLineEdit()
        self.lineEdit_error = PySide6.QtWidgets.QLineEdit()


        self.layout_first_row = PySide6.QtWidgets.QHBoxLayout()
        self.layout_second_row = PySide6.QtWidgets.QHBoxLayout()

        self.layout_first_row.addWidget(self.label_exp)
        self.layout_first_row.addWidget(self.lineEdit_exp)
        self.layout_second_row.addWidget(self.label_error)
        self.layout_second_row.addWidget(self.lineEdit_error)

        self.layout_param = PySide6.QtWidgets.QVBoxLayout()

        self.layout_param.addLayout(self.layout_first_row)
        self.layout_param.addLayout(self.layout_second_row)
        self.layout_param.addWidget(self.button_confirm)

        self.groupbox_param = PySide6.QtWidgets.QGroupBox("Параметры имитационной модели")
        self.groupbox_param.setLayout(self.layout_param)

        # Table page 1
        self.groupbox_table1 = PySide6.QtWidgets.QGroupBox("Координаты Z контрольных точек")

        self.table_1 = PySide6.QtWidgets.QTableWidget()
        self.layout_table1 = PySide6.QtWidgets.QVBoxLayout()
        self.layout_table1.addWidget(self.table_1)
        self.groupbox_table1.setLayout(self.layout_table1)

        # Img page1
        self.groupbox_img1 = PySide6.QtWidgets.QGroupBox("Координаты Z контрольных точек")
        #self.groupbox_img1.setMaximumHeight(int(self.tab.height() * 0.7))
        #self.groupbox_img1.setMaximumWidth(int(self.groupbox_table1.width()))

        self.la_1 = PySide6.QtWidgets.QVBoxLayout()

        self.label_img = PySide6.QtWidgets.QLabel()
        self.label_img.setScaledContents(True)
        self.la_1.addWidget(self.label_img)

        self.groupbox_img1.setLayout(self.la_1)


        # Left side 1 page
        self.layout_groups_left = PySide6.QtWidgets.QVBoxLayout()
        self.layout_groups_left.addWidget(self.groupbox_db)
        self.layout_groups_left.addWidget(self.groupbox_cycle)
        self.layout_groups_left.addWidget(self.groupbox_param)

        # Right side 1 page
        self.layout_groups_right = PySide6.QtWidgets.QVBoxLayout()
        self.layout_groups_right.spacerItem()
        self.layout_groups_right.addWidget(self.groupbox_table1, 2)
        self.layout_groups_right.addWidget(self.groupbox_img1, 2)

        # fill 1 page
        self.layout_data_tab = PySide6.QtWidgets.QHBoxLayout()
        self.layout_data_tab.addLayout(self.layout_groups_left)
        self.layout_data_tab.addLayout(self.layout_groups_right)

        # Widgets для TabWidget
        self.widget_first_tab = PySide6.QtWidgets.QWidget()
        self.widget_second_tab = PySide6.QtWidgets.QWidget()
        self.widget_third_tab = PySide6.QtWidgets.QWidget()
        self.widget_forth_tab = PySide6.QtWidgets.QWidget()
        self.widget_fifth_tab = PySide6.QtWidgets.QWidget()
        self.widget_sixth_tab = PySide6.QtWidgets.QWidget()
        self.widget_first_tab.setLayout(self.layout_data_tab)

        # Создание и заполнение TabWidget

        self.tab.addTab(self.widget_first_tab, "Данные")
        self.tab.addTab(self.widget_second_tab, "Первый уровень декомпозиции")
        self.tab.addTab(self.widget_third_tab, "Второй уровень декомпозиции")
        self.tab.addTab(self.widget_forth_tab, "Третий уровень декомпозиции")
        self.tab.addTab(self.widget_fifth_tab, "Четвертый уровень декомпозиции")
        self.tab.addTab(self.widget_sixth_tab, "Тестирование")

        # Блокировка
        self.groupbox_cycle.setEnabled(False)
        self.groupbox_param.setEnabled(False)
        self.groupbox_img1.setEnabled(False)
        self.groupbox_table1.setEnabled(False)


        MainWindow.setCentralWidget(self.tab)
        
