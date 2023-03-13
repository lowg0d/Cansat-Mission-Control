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

from PyQt5.QtCore import (QObject, Qt,
                          QPropertyAnimation,
                          QEasingCurve,
                          QPoint)

# ============================================================== #

class WindowManager(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui
        self.config = parent.config

        self.clickPostion = None
        self.full_screen = False

        # == setup menu animations == #
        # on
        self.menu_animation_on = QPropertyAnimation(
            self.ui.fr_menu, b'minimumWidth')
        self.menu_animation_on.setDuration(60)
        self.menu_animation_on.setStartValue(0)
        self.menu_animation_on.setEndValue(200)
        self.menu_animation_on.setEasingCurve(QEasingCurve.InOutQuart)

        # off
        self.menu_animation_off = QPropertyAnimation(
            self.ui.fr_menu, b'minimumWidth')
        self.menu_animation_off.setDuration(60)
        self.menu_animation_off.setStartValue(200)
        self.menu_animation_off.setEndValue(0)
        self.menu_animation_off.setEasingCurve(QEasingCurve.InOutQuart)

    # ============================================================== #

    def show_full_screen(self):
        
        if self.full_screen == False:
            self.full_screen = True
            self.ui.btn_set_full_screen.setChecked(True)
            self.parent.showFullScreen()
        
        else:
            self.parent.showNormal()
            self.full_screen = False
            self.ui.btn_set_full_screen.setChecked(False)
            
    # == reload the window == #
    def reload_window(self):

        if self.parent.serial.is_connected:
            self.parent.connection_buffer.disconnect()
        
        if self.parent.serial.dummy_enabled == True:
            self.parent.serial.stop_dummy()
            
        self.parent.close()
        self.parent.__init__()

    # ================================================================= #

    # == window movement == #
    def move_window(self, event):
        if self.parent.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                delta = QPoint(event.globalPos() - self.clickPostion)
                self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
                self.clickPostion = event.globalPos()
                event.accept()

        if event.globalPos().y() < 15:
            self.maximize_app()

        else:     
            self.normalize_app()
        
    # == double click on titlebar == #
    def topbar_double_click(self, e):
        if self.parent.isMaximized():
            self.normalize_app()
        else:
            self.maximize_app()

    # ================================================================= #

    # == normalize == #
    def normalize_app(self):
        self.ui.btn_maximize.show()
        self.ui.btn_normalize.hide()
        
        self.parent.showNormal()

    # == maximize == #
    def maximize_app(self):
        self.ui.btn_normalize.show()
        self.ui.btn_maximize.hide()
        
        self.parent.showMaximized()

    # ================================================================= #

    # == togle menu btn handler == #
    def togle_menu(self):
        width = self.ui.fr_menu.width()

        if width == 0:
            self.menu_animation_on.start()

        else:
            self.menu_animation_off.start()

    # ================================================================= #
    """
    # == btn handler == #
    def btn_clicked(self, value):
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_start_max":
            if self.parent.ui.btn_start_max.isChecked():
                self.config.set_ini("options", "start_maximized", "True")
            else:
                self.config.set_ini("options", "start_maximized", "False")

        if btnName == "btn_auto_conn":
            if self.parent.ui.btn_auto_conn.isChecked():
                self.config.set_ini(
                    "options", "attempt_connection_on_start", "True")
            else:
                self.config.set_ini(
                    "options", "attempt_connection_on_start", "False")

        if btnName == "btn_auto_update":
            if self.parent.ui.btn_auto_update.isChecked():
                self.config.set_ini("options", "update_ports_on_start", "True")
            else:
                self.config.set_ini(
                    "options", "update_ports_on_start", "False")

        if btnName == "config_default_bauds":
            self.config.set_ini("conn", "default_bauds", value)
    """