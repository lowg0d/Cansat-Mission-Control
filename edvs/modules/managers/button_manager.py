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

from PySide6.QtCore import QObject

# ================================================================= #

class ButtonManager(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui
        self.config = parent.config
    
    def btn_clicked(self, value):
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_start_max":
            if self.parent.ui.btn_start_max.isChecked():
                self.config.edit(
                    "application.settings.on_start_maximized", True)
            else:
                self.config.edit(
                    "application.settings.on_start_maximized", False)

        if btnName == "btn_auto_update":
            if self.parent.ui.btn_auto_update.isChecked():
                self.config.edit("application.settings.on_start_port_update", True)
            else:
                self.config.edit("application.settings.on_start_port_update", False)
                
        if btnName == "config_default_bauds":
            self.config.edit("connection.bauds_default", value)