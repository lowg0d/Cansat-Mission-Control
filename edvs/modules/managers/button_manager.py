from PyQt5.QtCore import QObject, QTime

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