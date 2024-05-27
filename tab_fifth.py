import PySide6
from PySide6 import QtWidgets
import pyqtgraph
import numpy as np
import graph


class FifthTabUI(object):
    def setupUi(self, QWidget):
        #QWidget.setEnabled(False)
        # Главный слой
        self.main_horlay = PySide6.QtWidgets.QHBoxLayout()

        self.dict_chb_graph = {}

        # Left
        self.listbox_all_dots = PySide6.QtWidgets.QListWidget()
        # self.button_confirm = PySide6.QtWidgets.QPushButton("Подтвердить")
        self.button_clear = PySide6.QtWidgets.QPushButton("Сбросить всё")
        self.button_clear.clicked.connect(self.checkbox_off)

        self.layout_left = PySide6.QtWidgets.QVBoxLayout()
        self.layout_left.addWidget(self.listbox_all_dots)
        # self.layout_left.addWidget(self.button_confirm)
        self.layout_left.addWidget(self.button_clear)

        # Right
        self.graph_phase = pyqtgraph.PlotWidget()
        self.main_plot = self.graph_phase.getPlotItem()
        self.graph_phase.addLegend()

        self.graph_phase.setLabel("left", "Z", **{'color': '#EEE', 'font-size': '14pt'})
        self.graph_phase.setLabel("bottom", "Цикл наблюдения (t)", **{'color': '#EEE', 'font-size': '14pt'})

        self.layout_right = PySide6.QtWidgets.QVBoxLayout()
        self.layout_right.addWidget(self.graph_phase)



        # Компановка
        self.main_horlay.addLayout(self.layout_left,1)
        self.main_horlay.addLayout(self.layout_right,3)

        QWidget.setLayout(self.main_horlay)

    def checkbox_off(self):
        for i in self.dict_chb_graph.keys():
            if i.isChecked():
                i.setChecked(False)