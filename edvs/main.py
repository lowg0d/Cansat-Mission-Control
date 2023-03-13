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

import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from edvs.ui import Ui_MainWindow

from edvs.modules.managers import (
    ConfigManager,
    WindowManager,
    TerminalManager,
    SerialManager,
    GraphManager,
    ButtonManager)

from edvs.modules.utility import (ConnectionBuffer, 
                                ClockUpdater)

# ============================================================== #

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # == SetUp UI == #
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # == Managers == #
        self.config = ConfigManager
        self.window_manager = WindowManager(self) 
        self.terminal = TerminalManager(self)
        self.serial = SerialManager(self)
        self.clock_updater = ClockUpdater(self)
        self.button_manager = ButtonManager(self)
        # == Utility == # 
        self.connection_buffer = ConnectionBuffer(self)
        self.serial.data_available.connect(self.terminal.write)
        
        # == SetUps == #
        self.setup_window()
        self.setup_buttons() 
        self.setup_graphs()
        
        # connect graph updater to the signal
        self.serial.update_graphs.connect(self.graph_manager.update)
     
        # == Start main clock thread == #
        self.clock_updater.update_global_time_label()
        self.clock_updater.start_time_update_thread()
        
        # == send bootup message
        self.terminal.boot_up_message()
        self.update_status_bar("Sucesfully Started")
        self.apply_config()
        
        # show
        self.show()
        
        # version check
        #self.check_app_version()
    
    # ================================================================= #
    
    # == Set up => WINDOW == #
    def setup_window(self):
        
        # get values from configution
        window_name = self.config.get("application.name")
        window_icon = self.config.get("application.icon_path")
        self.app_status = self.config.get("version.status")
        self.application_build = self.config.get("version.build")
        self.app_version = self.config.get("version.version")
        
        bauds_dic = self.config.get("connection.bauds_dic")
        bauds_default = self.config.get("connection.bauds_default")
        
        # == delete title == #
        self.setWindowFlag(Qt.FramelessWindowHint)

        # == set window title & icon == #
        self.setWindowTitle(window_name)
        self.setWindowIcon(QIcon(window_icon))

        # window focus
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

        # == draggable window == #
        self.ui.fr_top_bar.mouseMoveEvent = self.window_manager.move_window

        # == hide normalize button == #
        self.ui.btn_normalize.hide()
        
        # == add data to baudrate combo-boxes // connection + config == #
        self.ui.cb_bauds.addItems(bauds_dic)
        self.ui.config_default_bauds.addItems(bauds_dic)

        self.ui.config_default_bauds.setCurrentText(bauds_default)
        self.ui.cb_bauds.setCurrentText(bauds_default)
        
        self.window_version = f"{self.app_status}-{self.app_version}"
        self.window_id = f"{window_name} | v: {self.app_status}-{self.app_version} | b: {self.application_build}"
        
    # == Set up => BUTTONS == #
    def setup_buttons(self):
        
        # maximize or minimze window by 2x click on top bar
        self.ui.fr_top_bar.mouseDoubleClickEvent = self.window_manager.topbar_double_click
        
        # input enter
        self.ui.terminal_input.returnPressed.connect(
            self.connection_buffer.send_data
        )
        
        # serial btns
        # update ports
        self.ui.btn_update_ports.clicked.connect(
            self.connection_buffer.update_ports
        )
        
        # connect / disconnect
        self.ui.btn_connect_serial.clicked.connect(
            self.connection_buffer.connect
        )
        
        self.ui.btn_togle_log.clicked.connect(
            self.connection_buffer.toggle_recording
        )
        
        # terminal btns
        self.ui.btn_clear.clicked.connect(
            self.terminal.clear
        )
        
        self.ui.btn_send.clicked.connect(
            self.connection_buffer.send_data
        )
        
        # titlebar btns
        # close
        self.ui.btn_close.clicked.connect(
            lambda: self.close()
        ) 
        
        # minimize
        self.ui.btn_minimize.clicked.connect(
            lambda: self.showMinimized()
        )
        
        # maximize
        self.ui.btn_maximize.clicked.connect(
            self.window_manager.maximize_app
        )
        
        # normalize
        self.ui.btn_normalize.clicked.connect(
            self.window_manager.normalize_app
        )

        # togle menu
        self.ui.btn_togle_menu.clicked.connect(
            self.window_manager.togle_menu
        )

        # f1 to togle the menu 
        menu_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        menu_shortcut.activated.connect(
            self.window_manager.togle_menu
        )
        
        terminal_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        terminal_shortcut.activated.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        flight_shortcut = QShortcut(QKeySequence(Qt.Key_F2), self)
        flight_shortcut.activated.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        
        fs_shortcut = QShortcut(QKeySequence(Qt.Key_F11), self)
        fs_shortcut.activated.connect(
            self.window_manager.show_full_screen)
        
        # config btns
        self.ui.btn_opn_logs.clicked.connect(
            self.opn_logs)
        
        self.ui.btn_refresh.clicked.connect(
            self.window_manager.reload_window)
        
        self.ui.btn_set_full_screen.clicked.connect(
            self.window_manager.show_full_screen)
        
        self.ui.config_default_bauds.currentTextChanged.connect(
            self.button_manager.btn_clicked)
        
        self.ui.btn_start_max.clicked.connect(
            self.button_manager.btn_clicked)
        self.ui.btn_auto_update.clicked.connect(
            self.button_manager.btn_clicked)
        
        # menu btns
        self.ui.btn_menu_1.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_menu_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_menu_config.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

    # == Set up => GRAPHS == #
    def setup_graphs(self):        
        self.graph_manager = GraphManager(self)
        
    # ================================================================= #

    # == MousePress Event == #
    def mousePressEvent(self, e):
        self.window_manager.clickPostion = e.globalPos()
    
    # ================================================================= #
    
    # == Update the status bar msg == #
    def update_status_bar(self,msg):
        if len(msg) == 0:
          self.ui.statusBar.showMessage(f"// {self.window_id}")
        else:
            self.ui.statusBar.showMessage(f"// {self.window_id}    -   {msg}")
    
    # ================================================================= #
    
    # == Open the logs folder == #
    def opn_logs(self):
        folder = self.serial.logs_path
        
        if not os.path.exists(folder):
            os.mkdir(folder)
            
        path = os.path.realpath(folder)
        os.startfile(path)

    # ================================================================= #
    def apply_config(self):
        update_ports_on_start = self.config.get(
            "application.settings.on_start_port_update")

        maximized_on_start = self.config.get(
            "application.settings.on_start_maximized")
        
        if update_ports_on_start == True:
            self.ui.btn_auto_update.setChecked(True)
            self.connection_buffer.update_ports()
            
        if maximized_on_start == True:
            self.ui.btn_start_max.setChecked(True)
            self.window_manager.maximize_app()