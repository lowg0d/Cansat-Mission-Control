"""
888888 8888b.  Yb    dP .dP"Y8 
88__    8I  Yb  Yb  dP  `Ybo."  
88""    8I  dY   YbdP   o.`Y8b 
888888 8888Y"     YP    8bodP' 

© Elburgo Tecnoclub - Martin Ortiz.
© Elburgo Data Visualization Software.
-- @Version: 1.0-BETA
-- @data: 2/20/2023
"""

# ================================================================= #

import pyqtgraph as pg
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QPainter

from edvs.modules.utility import (
    MonoAxisPlotWidget,
    GpsPlotWidget)

# ================================================================= #

class GraphManager(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.config = parent.config
        self.ui = parent.ui
        self.last_sats = 100
        
        # ================================================================= #
        
        self.set_config()
        self.set_layout()
        self.set_graphs()

    # ================================================================= #

    def update(self, value):
        try:
            value_chain = []
            value_chain = value

            self.graph_temp.update(value_chain[0])
            self.graph_humidity.update(value_chain[1])
            self.graph_bp.update(value_chain[2])
            
            self.update_labels(value_chain[3],value_chain[3])
            self.graph_speed.update(float(value_chain[7]))
            
            self.graph_gps.update(value_chain[4],value_chain[5])
            self.graph_altitude.update(value_chain[6])
            
            
        except Exception as e:
            print(f"[WARNING] Graph Update Data NOT a int - {e}")
            
    # ================================================================= #
            
    def set_graphs(self):
        self.graph_temp = MonoAxisPlotWidget(
            title="TEMP(ºC)",
            linspace_x=50,
            color="#e74c3c"
        )

        self.graph_bp = MonoAxisPlotWidget(
            title="BP(BAR)",
            linspace_x=50,
            color="#e74c3c"
        )
        
        self.graph_humidity = MonoAxisPlotWidget(
            title="HUMIDITY(%)",
            color="#16a085",
            linspace_x=25
        )

        self.graph_altitude = MonoAxisPlotWidget(
            title="ALT(M)",
            color="#9b59b6",
            linspace_x=25
        )
        
        self.graph_speed = MonoAxisPlotWidget(
            title="SPEED(M/S)",
            color="#27ae60",
            linspace_x=25
        )
        
        self.graph_gps = GpsPlotWidget(
            title="LAT/LON"
        )
        
        # ================================================================= #
        
        self.graphs_suprerior_layout.addItem(self.graph_temp)
        self.graphs_suprerior_layout.addItem(self.graph_bp)
        
        self.graphs_inferior_layout.addItem(self.graph_altitude)
        self.graphs_inferior_layout.addItem(self.graph_humidity)
        self.graphs_inferior_layout.addItem(self.graph_speed)
        self.graphs_inferior_layout.addItem(self.graph_gps)
        
    # ================================================================= #
        
    def set_config(self):
        pg.setConfigOption("background", (20, 21, 22))
        pg.setConfigOption("foreground", (145, 145, 145))
        pg.setConfigOption("antialias", self.config.get("graphs.settings.antialias"))
        pg.setConfigOption("exitCleanup", True)
        pg.setConfigOption("useOpenGL", self.config.get("graphs.settings.opengl"))
        pg.setConfigOption("useCupy", self.config.get("graphs.settings.cupy"))
        pg.setConfigOption("useNumba", self.config.get("graphs.settings.numba"))
        pg.setConfigOption("segmentedLineMode", self.config.get("graphs.settings.segmentedLineMode"))

    # ================================================================= #

    def set_layout(self):        
        # create a graphic layout
        self.layout = pg.GraphicsLayoutWidget()
        self.layout.setAntialiasing(True)
        self.layout.setRenderHints(QPainter.Antialiasing)
        
        # ================================================================= #
        
        # create a seconday layout
        self.graphs_layout = self.layout.addLayout(
            colspan=1, 
            rowspan=1)
        
        self.graphs_suprerior_layout = self.graphs_layout.addLayout(
            rowspan=1, 
            colspan=1,
            border=(63, 63, 63, 50))
        
        self.graphs_layout.nextRow()
        
        self.graphs_inferior_layout = self.graphs_layout.addLayout(
            rowspan=1,
            colspan=1,
            border=(63, 63, 63, 50))
        
        # ================================================================= #
        
        self.graphs_suprerior_layout.setContentsMargins(0, 0, 0, 0)
        self.graphs_inferior_layout.setContentsMargins(0, 0, 0, 0)
        self.graphs_layout.setContentsMargins(0, 0, 0, 0)
        
        self.graphs_suprerior_layout.setSpacing(4)
        self.graphs_inferior_layout.setSpacing(4)
        self.graphs_layout.setSpacing(4)
        
        self.ui.telemetry_graphs.addWidget(self.layout)
    
    # ================================================================= #
    
    def update_labels(self, sats, send_time):
        
        if sats != self.last_sats:
            self.last_sats = sats
            satellites_color = "#8cb854"
            if float(sats) < 2:
                satellites_color = "#d79921"
            if float(sats) < 1:
                satellites_color = "#a8002a"
            
            self.parent.ui.lb_connection_info.setText(
                f"<b style='color:{satellites_color};'>{sats} SATS</b>")
    
            self.parent.ui.lb_info.setText(
                f"<b style='color:{satellites_color};'>{sats} SATS</b>")
        