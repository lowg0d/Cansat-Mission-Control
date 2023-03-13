"""
888888 8888b.  Yb    dP .dP"Y8 
88__    8I  Yb  Yb  dP  `Ybo."  
88""    8I  dY   YbdP   o.`Y8b 
888888 8888Y"     YP    8bodP' 

© Elburgo Tecnoclub - Martin Ortiz.
© Elburgo Data Visualization Software.
-- @Version: 1.0-BETA
-- @data: 3/13/2023
"""

# ================================================================= #

import pyqtgraph as pg
import numpy as np

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QColor, QFont

# ================================================================= #
class MonoAxisPlotWidget(pg.PlotItem):
    def __init__(self, parent=None, labels={'bottom': 'T(s)'}, title=None,
                 color: str = "#00BA42", enableMenu=False, linspace_x=100, **kargs):
        super().__init__(parent=parent, labels=labels, title=title,
                         enableMenu=enableMenu, **kargs)

        x_vals = np.arange(0, 0, linspace_x)
        self.graph_plot = self.plot(
            x=x_vals, 
            pen=pg.mkPen(color, width=2.5), 
            antialias=True, connect='finite')
        
        self.graph_plot.pxMode = False

        fill_color = QColor(color)
        fill_color.setAlpha(10)

        fill_color2 = QColor(color)
        fill_color2.setAlpha(50)

        grad = QtGui.QLinearGradient(0, 0, 0, 3)
        grad.setColorAt(0, fill_color)
        grad.setColorAt(1, fill_color2)
        brush = QtGui.QBrush(grad)
        
        self.graph_plot.setFillBrush(brush)
        self.graph_plot.setFillLevel(0)
        self.graph_plot.setDownsampling(auto=True)

        self.last_update_time = QtCore.QDateTime.currentDateTime()

        self.graph_data = np.zeros(linspace_x)

        self.curve = pg.PlotCurveItem()
        self.curve.pxMode = False
        self.addItem(self.curve)
        
        self.ptr1 = 0


    def update(self, value):
        now = QtCore.QDateTime.currentDateTime()
        elapsed_time = self.last_update_time.msecsTo(now) / 1000
        self.last_update_time = now
    
        value = float(value)
    
        self.graph_data[:-1] = self.graph_data[1:]
        self.graph_data[-1] = value

        x_vals = np.linspace(self.ptr1, self.ptr1 + elapsed_time, len(self.graph_data))
        
        self.ptr1 += float(elapsed_time)
        
        self.setXRange(self.ptr1 - elapsed_time, self.ptr1, padding=0)
        
        self.graph_plot.setData(x=x_vals, y=self.graph_data)
        
# ================================================================= #

class GpsPlotWidget(pg.PlotItem):
    def __init__(self, parent=None, labels={'bottom': 'Longitude', 'left': 'Latitude'}, title=None,
                 color: str = "#00BA42", enableMenu=False, **kargs):
        super().__init__(parent=parent, labels=labels, title=title,
                         enableMenu=enableMenu, **kargs)

        fill_color = QColor(color)
        fill_color.setAlpha(50)
        
    
        self.graph_plot = self.plot(
            pen=pg.mkPen(fill_color, width=1.5),
            symbol='x',
            symbolSize=6,
            symbolBrush=pg.mkBrush(color),
            symbolPen=None,  # Set symbol border to None
            antialias=True, 
            connect='finite')
        
        self.graph_plot.setDownsampling(auto=True)

        self.graph_plot.pxMode = False

        self.last_update_time = QtCore.QDateTime.currentDateTime()
        self.graph_data = {'x': [], 'y': []}
        self.counter = 0


    def update(self, latitude, longitude):
        longitude = float(longitude)
        latitude = float(latitude)

        self.graph_data['x'].append(longitude)
        self.graph_data['y'].append(latitude)

        if len(self.graph_data['x']) <= 9:
            self.graph_plot.setData(self.graph_data['x'], self.graph_data['y'])
            
        else:
            self.graph_plot.setData(self.graph_data['x'], self.graph_data['y'], symbol=None)
            self.graph_data['x'] = self.graph_data['x'][1:]
            self.graph_data['y'] = self.graph_data['y'][1:]
            self.graph_plot.setData(self.graph_data['x'], self.graph_data['y'])
            
            
        

# ================================================================= #

class Type_two_graph(pg.PlotItem):

    def __init__(self, parent=None, name=None, labels=None, title=None, viewBox=None, axisItems=None, color_1=None, color_2=None, color_3=None, name_1=None, name_2=None, name_3=None, enableMenu=False, linspace_x=None, ** kargs,):
        
        super().__init__(parent, name, labels, title,
                         viewBox, axisItems, enableMenu, **kargs)
        
        font = QFont('Arame', 9)
        self.titleLabel.item.setFont(font)
        
        if color_1 == None or color_2 == None or color_3 == None:
            color_1 = "#195EFF"
            color_2 = "#BC2649"
            color_3 = "#00BA42"

        if name_1 == None or name_2 == None or name_3 == None:
            name_1 = "X"
            name_2 = "Y"
            name_3 = "Z"

        fill_color_1 = QColor(color_1)
        fill_color_2 = QColor(color_2)
        fill_color_3 = QColor(color_3)
        
        fill_color_1.setAlpha(10)
        fill_color_2.setAlpha(10)
        fill_color_3.setAlpha(10)

        fill_color_1_2 = QColor(color_1)
        fill_color_2_2 = QColor(color_2)
        fill_color_3_2 = QColor(color_3)

        fill_color_1_2.setAlpha(87)
        fill_color_2_2.setAlpha(87)
        fill_color_3_2.setAlpha(87)

        grad1 = QtGui.QLinearGradient(0, 0, 0, 3)
        grad1.setColorAt(0.1, fill_color_1)
        grad1.setColorAt(0.9, fill_color_1_2)
        brush1 = QtGui.QBrush(grad1)

        grad2 = QtGui.QLinearGradient(0, 0, 0, 3)
        grad2.setColorAt(0.1, fill_color_2)
        grad2.setColorAt(0.9, fill_color_2_2)
        brush2 = QtGui.QBrush(grad2)
        
        grad3 = QtGui.QLinearGradient(0, 0, 0, 3)
        grad3.setColorAt(0.1, fill_color_3)
        grad3.setColorAt(0.9, fill_color_3_2)
        brush3 = QtGui.QBrush(grad3)

        if linspace_x == None:
            linspace_x = 800

        self.addLegend()

        self.plot_1 = self.plot(pen=pg.mkPen(color_1, width=2), name=name_1, antialias=True)
        self.plot_2 = self.plot(pen=pg.mkPen(color_2, width=2), name=name_2, antialias=True)
        self.plot_3 = self.plot(pen=pg.mkPen(color_3, width=2), name=name_3, antialias=True)
        
        self.plot_1.setFillBrush(brush1)
        self.plot_2.setFillBrush(brush2)
        self.plot_3.setFillBrush(brush3)
        
        self.plot_1.setLogMode(False, False)
        self.plot_2.setLogMode(False, False)
        self.plot_3.setLogMode(False, False)
        
        self.plot_1.setFillLevel(0)
        self.plot_2.setFillLevel(0)
        self.plot_3.setFillLevel(0)
        
        self.data_1 = np.linspace(0, 0, linspace_x)
        self.data_2 = np.linspace(0, 0, linspace_x)
        self.data_3 = np.linspace(0, 0, linspace_x)
        
        self.ptr = 0

    def update(self, value_1, value_2, value_3):

        self.data_1[:-1] = self.data_1[1:]
        self.data_2[:-1] = self.data_2[1:]
        self.data_3[:-1] = self.data_3[1:]

        self.data_1[-1] = float(value_1)
        self.data_2[-1] = float(value_2)
        self.data_3[-1] = float(value_3)

        self.ptr += 0.5

        self.plot_1.setData(self.data_1)
        self.plot_2.setData(self.data_2)
        self.plot_3.setData(self.data_3)

        self.plot_1.setPos(self.ptr, 0)
        self.plot_2.setPos(self.ptr, 0)
        self.plot_3.setPos(self.ptr, 0)

    def clear(self):
        pass

