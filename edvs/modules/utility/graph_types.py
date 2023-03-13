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
        
        self.graph_data = np.zeros(linspace_x)

        self.curve = pg.PlotCurveItem()
        self.curve.pxMode = False
        self.addItem(self.curve)
        
        self.ptr1 = 0


    def update(self, value, elapsed_time):
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