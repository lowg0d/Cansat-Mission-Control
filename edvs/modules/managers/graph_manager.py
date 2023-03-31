"""
888888 8888b.  Yb    dP .dP"Y8 
88__    8I  Yb  Yb  dP  `Ybo."  
88""    8I  dY   YbdP   o.`Y8b 
888888 8888Y"     YP    8bodP' 

© Elburgo Tecnoclub - Martin Ortiz.
© Elburgo Data Visualization Software.
-- @Version: 1.0-BETA
-- @data: 3/13/2023

este/o 3/0
n/s 44 40
"""

import pyqtgraph as pg

from PySide6.QtCore import QObject, QDateTime
from PySide6.QtGui import QPainter

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
        self.total_time = 0.0
        
        self.filter_ranges = dict(self.config.get("graphs.filter_ranges"))
        self.filter_enabled = self.config.get("graphs.filter_enabled")
        self.previous_values = {}
        self.previous_altitude = 0
        self.altitude_match_times = 0
        
    # ================================================================= #

    def update(self, value):
        try:
            value_chain = []
            if self.filter_enabled == True:
                value_chain = self.data_filter(value)
            else:
                value_chain = value

            now = QDateTime.currentDateTime()
            ping = self.last_update_time.msecsTo(now)
            time_mission = ping / 1000
            
            self.update_state(value_chain[3])
            self.update_labels(self.total_time, ping)

            self.graph_temp.update(value_chain[0],time_mission)
            self.graph_humidity.update(value_chain[1],time_mission)
            self.graph_bp.update(value_chain[2],time_mission)
            
            self.graph_gps.update(value_chain[4],value_chain[5])
            self.graph_altitude.update(value_chain[3],time_mission)
            self.graph_speed.update(value_chain[6],time_mission)
            
            self.last_update_time = now
            self.total_time += time_mission
    
        except Exception as e:
            print(f"[WARNING] UPDATING - {e}")
   
    def data_filter(self, value_chain):
        filtered_values = []
        for i, value in enumerate(value_chain):
            value = float(value)
            if str(i) in self.filter_ranges:
                min_value, max_value = self.filter_ranges[str(i)]
                
                if value < min_value:
                    filtered_value = min_value
                elif value > max_value:
                    filtered_value = max_value
                else:
                    filtered_value = value
                    
                filtered_values.append(filtered_value)
                self.previous_values[i] = filtered_value
            else:
                filtered_values.append(value)
        return filtered_values
            
    def update_state(self, altitude):
        message = f"<b style='color:#16a085;'>// #IDLE</b>"
        
        if float(altitude) > float(self.previous_altitude):
            if self.altitude_match_times > 3:
                self.previous_altitude = altitude
                message = f"<b style='color:#8cb854;'>// #ASCENT</b>"
            else:
                self.previous_altitude = altitude
                self.altitude_match_times += 1
        
        elif float(altitude) < float(self.previous_altitude):
            self.previous_altitude = altitude
            message = f"<b style='color:#d79921;'>// #DESCENT</b>"
        
        elif float(altitude) == float(self.previous_altitude):
            self.previous_altitude = altitude
            message = f"<b style='color:#9b59b6;'>// #LANDED</b>"
        
        else:
            self.previous_altitude = altitude
            message = f"<b style='color:#a8002a;'>// #UNKNOWN</b>"
        
        self.parent.ui.lb_state.setText(message)
        
    # ================================================================= #
    
    def update_labels(self, time, ping):
        
        ping_color = "#8cb854"
        if ping > 1100:
            ping_color = "#d79921"
        if ping > 5100:
            ping_color = "#a8002a"
        
        self.parent.ui.lb_countdown.setText(
                        f"<b style='color:rgba(235,235,255,0.4);'>{time:.2f}S</b> MIT")
        
        self.parent.ui.lb_ping.setText(
                    f"<b style='color:{ping_color};'>{ping} ms</b>")
            
    # ================================================================= #
            
    def set_graphs(self):
        # create the graphics
        self.graph_temp = MonoAxisPlotWidget(
            title="TEMP(ºC)",
            linspace_x=50,
            color="#2980b9",
        )

        self.graph_bp = MonoAxisPlotWidget(
            title="BP(BAR)",
            linspace_x=50,
            color="#2980b9"
        )
        
        self.graph_humidity = MonoAxisPlotWidget(
            title="HUMIDITY(%)",
            color="#e67e22",
            linspace_x=50
        )

        self.graph_altitude = MonoAxisPlotWidget(
            title="ALT(M)",
            color="#9b59b6",
            linspace_x=50
        )
        
        self.graph_speed = MonoAxisPlotWidget(
            title="SPEED(M/S)",
            color="#27ae60",
            linspace_x=50
        )
        
        self.graph_gps = GpsPlotWidget(
            title="LAT/LON",
            color="#c0392b"
        )
        
        # add the graphs to the layouts
        self.graphs_suprerior_layout.addItem(self.graph_temp)
        self.graphs_suprerior_layout.addItem(self.graph_bp)
        
        self.graphs_inferior_layout.addItem(self.graph_speed)
        self.graphs_inferior_layout.addItem(self.graph_altitude)
        self.graphs_inferior_layout.addItem(self.graph_humidity)
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
            border=(0, 0, 0, 0))
        
        # next of the container layout row
        self.graphs_layout.nextRow()

        # create a inferior layout
        self.graphs_inferior_layout = self.graphs_layout.addLayout(
            rowspan=1,
            colspan=1,
            border=(0, 0, 0, 0))

        # set contents margins and spacing
        self.graphs_suprerior_layout.setContentsMargins(0, 0, 0, 0)
        self.graphs_inferior_layout.setContentsMargins(4, 4, 4, 4)
        self.graphs_layout.setContentsMargins(0, 0, 0, 0)

        self.graphs_suprerior_layout.setSpacing(3)
        self.graphs_inferior_layout.setSpacing(3)
        self.graphs_layout.setSpacing(0)

        # add the layout to the UI
        self.ui.telemetry_graphs.addWidget(self.layout)

