import PySide6
from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
from scipy.interpolate import interp1d
import graph

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size), 'valid') / window_size
class FifthTabUI(object):
    def setupUi(self, QWidget):
        #QWidget.setEnabled(False)
        # Главный слой
        self.main_horlay = PySide6.QtWidgets.QHBoxLayout()

        subblock_combo = PySide6.QtWidgets.QComboBox()
        subblock_combo.addItems(["Subblock 1", "Subblock 2", "Subblock 3"])

        # Создаем два QListWidget
        listbox_all_points = PySide6.QtWidgets.QListWidget()  # Список всех точек
        listbox_subblock_points = PySide6.QtWidgets.QListWidget()  # Список точек выбранного подблока

        # Заполняем первый QListWidget
        for i in range(10):
            listbox_all_points.addItem(f"Point {i}")

        # Функция для перемещения элементов из одного QListWidget в другой
        def move_point():
            # Получаем выделенный элемент из первого QListWidget
            selected_items = listbox_all_points.selectedItems()

            if selected_items:
                # Берем первый выделенный элемент
                item_to_move = selected_items[0]

                # Добавляем его во второй QListWidget
                listbox_subblock_points.addItem(item_to_move.text())

                # Удаляем его из первого QListWidget
                listbox_all_points.takeItem(listbox_all_points.row(item_to_move))

        # Кнопка для перемещения точки из первого во второй
        move_button = PySide6.QtWidgets.QPushButton("Move Point")
        move_button.clicked.connect(move_point)  # Перемещаем точку по нажатию кнопки

        # Добавляем виджет выбора подблока и listbox'ы в компоновку
        self.main_horlay.addWidget(subblock_combo)
        self.main_horlay.addWidget(listbox_all_points)
        self.main_horlay.addWidget(move_button)
        self.main_horlay.addWidget(listbox_subblock_points)




        QWidget.setLayout(self.main_horlay)