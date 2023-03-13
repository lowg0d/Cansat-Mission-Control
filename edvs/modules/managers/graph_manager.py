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

from PyQt5.QtCore import QObject, QDateTime
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
        
        self.set_config()
        self.set_layout()
        self.set_graphs()

        self.last_update_time = QDateTime.currentDateTime()
        self.total_time = 0

    # ================================================================= #

    def update(self, value):
        try:
            value_chain = []
            value_chain = value

            now = QDateTime.currentDateTime()
            time_mission = self.last_update_time.msecsTo(now) / 1000
            self.last_update_time = now
            
            self.total_time += time_mission

            self.graph_temp.update(value_chain[0],time_mission)
            self.graph_humidity.update(value_chain[1],time_mission)
            self.graph_bp.update(value_chain[2],time_mission)
            
            self.update_labels(value_chain[3],int(self.total_time))
            
            self.graph_gps.update(value_chain[4],value_chain[5])
            self.graph_altitude.update(value_chain[6],time_mission)
            self.graph_speed.update(value_chain[7],time_mission)
            
            
        except Exception as e:
            print(f"[WARNING] UPDATING - {e}")
            
    # ================================================================= #
            
    def set_graphs(self):
        # create the graphics
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

        # add the graphics to the layouts
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

        # create a pyqtgraph layout
        self.layout = pg.GraphicsLayoutWidget()
        self.layout.setAntialiasing(True)
        self.layout.setRenderHints(QPainter.Antialiasing)

        # create a container layout for the layout that will display the graphs
        self.graphs_layout = self.layout.addLayout(
            colspan=1, 
            rowspan=1)

        # superior graph layout
        self.graphs_suprerior_layout = self.graphs_layout.addLayout(
            rowspan=1, 
            colspan=1,
            border=(63, 63, 63, 50))
        
        # next of the container layout row
        self.graphs_layout.nextRow()

        # create a inferior layout
        self.graphs_inferior_layout = self.graphs_layout.addLayout(
            rowspan=1,
            colspan=1,
            border=(63, 63, 63, 50))

        # set contents margins and spacing
        self.graphs_suprerior_layout.setContentsMargins(0, 0, 0, 0)
        self.graphs_inferior_layout.setContentsMargins(0, 0, 0, 0)
        self.graphs_layout.setContentsMargins(0, 0, 0, 0)

        self.graphs_suprerior_layout.setSpacing(3)
        self.graphs_inferior_layout.setSpacing(3)
        self.graphs_layout.setSpacing(0)

        # add the layout to the UI
        self.ui.telemetry_graphs.addWidget(self.layout)
    
    # ================================================================= #
    
    def update_labels(self, sats, time):
        if sats != self.last_sats:
            self.last_sats = sats
            satellites_color = "#8cb854"
            if float(sats) < 2:
                satellites_color = "#d79921"
            if float(sats) < 1:
                satellites_color = "#a8002a"
            
            self.parent.ui.lb_telemetry_info_1.setText(
                f"<b style='color:{satellites_color};'>{int(sats)} SATS</b>")

            self.parent.ui.lb_countdown.setText(
                f"T+ <b style='color:#8cb854;'>{time}</b> s")
        