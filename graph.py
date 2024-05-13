import pyqtgraph
import numpy
import scipy
import PySide6
from PySide6 import QtWidgets,QtGui


class Graph(object):
    def __init__(self, GraphQt):
        self.graph = GraphQt

    def setDots(self, x_mass, y_mass, color, plotWid):

        x = numpy.array(x_mass)
        y = numpy.array(y_mass)

        inter_func = scipy.interpolate.interp1d(x, y, kind="cubic")
        x_new = numpy.linspace(min(x_mass), max(x_mass), 100)
        y_new = inter_func(x_new)
        items_text = []
        font = PySide6.QtGui.QFont()
        font.setPointSize(20)
        for i, (x_val, y_val) in enumerate(zip(x_mass, y_mass)):
            text = pyqtgraph.TextItem(text=str(i), anchor=(0.5, 0.5))
            text.setPos(x_val+0.5, y_val)
            text.setFont(font)
            text.setColor((255, 255, 255, 70))
            plotWid.addItem(text)
            items_text.append(text)

        self.graph.setData(x_new, y_new, pen=color)

        return items_text
