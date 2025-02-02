import pyqtgraph
import numpy
import scipy
import PySide6
from PySide6 import QtGui


class Graph(object):
    def __init__(self, GraphQt):
        self.graph = GraphQt

    def setDots(self, x_mass, y_mass, color, plotWid, vertHeaders):
        pass

        # x = numpy.array(x_mass)
        # y = numpy.array(y_mass)
        # num_points = 100
        # spl = scipy.interpolate.splrep(x, y)
        # x_smooth = numpy.linspace(x.min(), x.max(), num_points)
        # y_smooth = scipy.interpolate.splev(x_smooth, spl)
        try:
            num_points = 300
            tck, u = scipy.interpolate.splprep([x_mass, y_mass], s=0, k=2)
            u_new = numpy.linspace(0, 1, num_points)
            x_smooth, y_smooth = scipy.interpolate.splev(u_new, tck)
        except:
            x_smooth = x_mass
            y_smooth = y_mass

        # inter_func = scipy.interpolate.interp1d(x, y, kind="cubic")
        # x_new = numpy.linspace(min(x_mass), max(x_mass), 100)
        # y_new = inter_func(x_new)

        items_text = []
        font = PySide6.QtGui.QFont()
        font.setPointSize(20)



        for i, (x_val, y_val) in enumerate(zip(x_mass, y_mass)):
            text = pyqtgraph.TextItem(text=str(vertHeaders[i]), anchor=(0.5, 0.5))
            text.setPos(x_val, y_val)
            text.setFont(font)
            text.setColor((255, 255, 255, 70))
            plotWid.addItem(text)
            items_text.append(text)

        self.graph.setData(x_smooth, y_smooth, pen=color)

        return items_text

    def lockRange(self, x1, x2, y1, y2):
        self.graph.setXRange(x1, x2, padding=0)
        self.graph.setYRange(y1, y2, padding=0)