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

import pyqtgraph as pg
import numpy as np

from PyQt5.QtGui import QColor, QBrush

# ================================================================= #
class MonoAxisPlotWidget(pg.PlotItem):
    def __init__(self, parent=None, labels={'bottom': 'T(s)'}, title=None,
                 color: str = "#00BA42", enableMenu=False, linspace_x=100, **kargs):
        super().__init__(parent=parent, labels=labels, title=title,
                         enableMenu=enableMenu, **kargs)

        x_vals = np.linspace(0.0, (linspace_x-1)/linspace_x, linspace_x)
        self.graph_plot = self.plot(
            x=x_vals, 
            pen=pg.mkPen(color, width=2.5), 
            antialias=True, connect='finite')
        
        self.graph_plot.pxMode = False

        fill_color = QColor(color)
        fill_color.setAlpha(20)
        brush = QBrush(fill_color)
        
        self.graph_plot.setFillBrush(brush)
        self.graph_plot.setFillLevel(0)
        self.graph_plot.setDownsampling(auto=False)
        
        self.graph_data = np.zeros(linspace_x)

        self.curve = pg.PlotCurveItem()
        self.curve.pxMode = False
        self.addItem(self.curve)
        
        self.ptr1 = 0.0
        self.window_size = 5 
        self.weights = np.ones(self.window_size) / self.window_size

        self.showGrid(x=True, y=True)
        self.getAxis('bottom').setPen(pg.mkPen('#777'))
        self.getAxis('left').setPen(pg.mkPen('#777'))
        
        self.getViewBox().disableAutoRange(axis="x")
        self.hideButtons()
        self.getViewBox().setMouseEnabled(x=False, y=False)
        
    def update(self, value, elapsed_time):
        value = float(value)
    
        self.graph_data[:-1] = self.graph_data[1:]
        self.graph_data[-1] = value
        
        smoothed_data = np.convolve(self.graph_data, self.weights, mode='valid')
        
        x_vals = np.linspace(self.ptr1, self.ptr1 + elapsed_time, len(smoothed_data))
        self.ptr1 += float(elapsed_time)
        
        self.setXRange(self.ptr1 - elapsed_time, self.ptr1, padding=0.01)        
        self.graph_plot.setData(x=x_vals, y=smoothed_data)

# ================================================================= #
class GpsPlotWidget(pg.PlotItem):
    def __init__(self, parent=None, labels={'bottom': 'Longitude', 'left': 'Latitude'}, title=None,
                 color: str = "#00BA42", enableMenu=False, **kargs):
        super().__init__(parent=parent, labels=labels, title=title,
                         enableMenu=enableMenu, **kargs)

        fill_color = QColor(color)
        fill_color.setAlpha(80)

        self.graph_data = {'x': [], 'y': []}
        self.lastet_data = {'x': [], 'y': []}

        self.graph_plot = self.plot(
            pen=pg.mkPen(fill_color, width=2),
            antialias=True, 
            connect='finite',
            symbol=None)

        self.graph_plot.setDownsampling(auto=True)
        self.graph_plot.pxMode = False

        self.scatter_plot = pg.ScatterPlotItem(symbol='x', size=7, brush=pg.mkBrush(color))
        self.addItem(self.scatter_plot)

        self.showGrid(x=True, y=True)
        self.getAxis('bottom').setPen(pg.mkPen('#777'))
        self.getAxis('left').setPen(pg.mkPen('#777'))

        self.hideButtons()
        self.getViewBox().setMouseEnabled(x=False, y=False)

    def update(self, latitude, longitude):
        longitude = float(longitude)
        latitude = float(latitude)

        self.graph_data['x'].append(longitude)
        self.graph_data['y'].append(latitude)

        if len(self.graph_data['x']) > 20:
            self.graph_data['x'].pop(0)
            self.graph_data['y'].pop(0)

        self.lastet_data = {'x': [longitude], 'y': [latitude]}
        self.graph_plot.setData(self.graph_data['x'], self.graph_data['y'])
        self.scatter_plot.setData(self.lastet_data['x'], self.lastet_data['y'], symbol='x', connect='finite')
        
        x_range = (min(self.graph_data['x']) - 0.0001, max(self.graph_data['x']) + 0.0001)
        y_range = (min(self.graph_data['y']) - 0.0001, max(self.graph_data['y']) + 0.0001)
        self.setRange(xRange=x_range, yRange=y_range)