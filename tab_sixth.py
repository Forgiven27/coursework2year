import PySide6
from PySide6 import QtWidgets,QtGui
import pyqtgraph


class SixthTabUI(object):
    def setupUi(self, QWidget):
        #QWidget.setEnabled(False)

        self.tabwidget_main = PySide6.QtWidgets.QTabWidget()
        self.layout_main = PySide6.QtWidgets.QHBoxLayout()
        self.layout_main.addWidget(self.tabwidget_main)

        self.widget_1_rest = PySide6.QtWidgets.QWidget()
        self.widget_2_uniform = PySide6.QtWidgets.QWidget()
        self.widget_3_leap = PySide6.QtWidgets.QWidget()
        self.widget_4_cyclic = PySide6.QtWidgets.QWidget()

        self.layout_1_tab = PySide6.QtWidgets.QVBoxLayout()
        self.layout_2_tab = PySide6.QtWidgets.QVBoxLayout()
        self.layout_3_tab = PySide6.QtWidgets.QVBoxLayout()
        self.layout_4_tab = PySide6.QtWidgets.QVBoxLayout()

        self.widget_1_rest.setLayout(self.layout_1_tab)
        self.widget_2_uniform.setLayout(self.layout_2_tab)
        self.widget_3_leap.setLayout(self.layout_3_tab)
        self.widget_4_cyclic.setLayout(self.layout_4_tab)

        # tab1 Rest
        self.plot_widget_rest_w_noise = pyqtgraph.PlotWidget()
        self.plot_widget_rest_wo_noise = pyqtgraph.PlotWidget()
        self.table_rest = PySide6.QtWidgets.QTableWidget()

        self.groupbox_graph_1_rest = PySide6.QtWidgets.QGroupBox("С шумами")
        self.groupbox_graph_2_rest = PySide6.QtWidgets.QGroupBox("Без шумов")

        self.layout_graph_rest_w = PySide6.QtWidgets.QHBoxLayout()
        self.layout_graph_rest_wo = PySide6.QtWidgets.QHBoxLayout()

        self.groupbox_graph_1_rest.setLayout(self.layout_graph_rest_w)
        self.groupbox_graph_2_rest.setLayout(self.layout_graph_rest_wo)

        self.layout_graph_rest_w.addWidget(self.plot_widget_rest_w_noise)
        self.layout_graph_rest_wo.addWidget(self.plot_widget_rest_wo_noise)

        self.layout_group_rest = PySide6.QtWidgets.QHBoxLayout()

        self.layout_group_rest.addWidget(self.groupbox_graph_1_rest)
        self.layout_group_rest.addWidget(self.groupbox_graph_2_rest)

        self.layout_1_tab.addLayout(self.layout_group_rest)
        self.layout_1_tab.addWidget(self.table_rest)


        # tab2 Uniform
        self.plot_widget_uni_w_noise = pyqtgraph.PlotWidget()
        self.plot_widget_uni_wo_noise = pyqtgraph.PlotWidget()
        self.table_uni = PySide6.QtWidgets.QTableWidget()

        self.groupbox_graph_1_uni = PySide6.QtWidgets.QGroupBox("С шумами")
        self.groupbox_graph_2_uni = PySide6.QtWidgets.QGroupBox("Без шумов")

        self.layout_graph_uni_w = PySide6.QtWidgets.QHBoxLayout()
        self.layout_graph_uni_wo = PySide6.QtWidgets.QHBoxLayout()

        self.groupbox_graph_1_uni.setLayout(self.layout_graph_uni_w)
        self.groupbox_graph_2_uni.setLayout(self.layout_graph_uni_wo)

        self.layout_graph_uni_w.addWidget(self.plot_widget_uni_w_noise)
        self.layout_graph_uni_wo.addWidget(self.plot_widget_uni_wo_noise)

        self.layout_group_uni = PySide6.QtWidgets.QHBoxLayout()

        self.layout_group_uni.addWidget(self.groupbox_graph_1_uni)
        self.layout_group_uni.addWidget(self.groupbox_graph_2_uni)

        self.layout_2_tab.addLayout(self.layout_group_uni)
        self.layout_2_tab.addWidget(self.table_uni)

        # tab3 Leap
        self.plot_widget_leap_w_noise = pyqtgraph.PlotWidget()
        self.plot_widget_leap_wo_noise = pyqtgraph.PlotWidget()
        self.table_leap = PySide6.QtWidgets.QTableWidget()

        self.groupbox_graph_1_leap = PySide6.QtWidgets.QGroupBox("С шумами")
        self.groupbox_graph_2_leap = PySide6.QtWidgets.QGroupBox("Без шумов")

        self.layout_graph_leap_w = PySide6.QtWidgets.QHBoxLayout()
        self.layout_graph_leap_wo = PySide6.QtWidgets.QHBoxLayout()

        self.groupbox_graph_1_leap.setLayout(self.layout_graph_leap_w)
        self.groupbox_graph_2_leap.setLayout(self.layout_graph_leap_wo)

        self.layout_graph_leap_w.addWidget(self.plot_widget_leap_w_noise)
        self.layout_graph_leap_wo.addWidget(self.plot_widget_leap_wo_noise)

        self.layout_group_leap = PySide6.QtWidgets.QHBoxLayout()

        self.layout_group_leap.addWidget(self.groupbox_graph_1_leap)
        self.layout_group_leap.addWidget(self.groupbox_graph_2_leap)

        self.layout_3_tab.addLayout(self.layout_group_leap)
        self.layout_3_tab.addWidget(self.table_leap)

        # tab4 Cyclic
        self.plot_widget_cyclic_w_noise = pyqtgraph.PlotWidget()
        self.plot_widget_cyclic_wo_noise = pyqtgraph.PlotWidget()
        self.table_cyclic = PySide6.QtWidgets.QTableWidget()

        self.groupbox_graph_1_cyclic = PySide6.QtWidgets.QGroupBox("С шумами")
        self.groupbox_graph_2_cyclic = PySide6.QtWidgets.QGroupBox("Без шумов")

        self.layout_graph_cyclic_w = PySide6.QtWidgets.QHBoxLayout()
        self.layout_graph_cyclic_wo = PySide6.QtWidgets.QHBoxLayout()

        self.groupbox_graph_1_cyclic.setLayout(self.layout_graph_cyclic_w)
        self.groupbox_graph_2_cyclic.setLayout(self.layout_graph_cyclic_wo)

        self.layout_graph_cyclic_w.addWidget(self.plot_widget_cyclic_w_noise)
        self.layout_graph_cyclic_wo.addWidget(self.plot_widget_cyclic_wo_noise)

        self.layout_group_cyclic = PySide6.QtWidgets.QHBoxLayout()

        self.layout_group_cyclic.addWidget(self.groupbox_graph_1_cyclic)
        self.layout_group_cyclic.addWidget(self.groupbox_graph_2_cyclic)

        self.layout_4_tab.addLayout(self.layout_group_cyclic)
        self.layout_4_tab.addWidget(self.table_cyclic)

        self.table_uni.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)
        self.table_rest.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)
        self.table_leap.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)
        self.table_cyclic.setEditTriggers(PySide6.QtWidgets.QTableWidget.NoEditTriggers)

        self.tabwidget_main.addTab(self.widget_1_rest, "Покой")
        self.tabwidget_main.addTab(self.widget_2_uniform, "Равномерное движение")
        self.tabwidget_main.addTab(self.widget_3_leap, "Скачок")
        self.tabwidget_main.addTab(self.widget_4_cyclic, "Циклическое движение")
        QWidget.setLayout(self.layout_main)
