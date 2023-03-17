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

from PyQt5.QtCore import (QObject, 
                          QThread,
                          QTime,
                          Qt)

# ================================================================= #

class ClockUpdater(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui

    def update_global_time_label(self):
        t = QTime.currentTime()
        self.ui.time_label.setText(f"<b style='color:rgba(235,235,255,0.4);'>{t.toString(Qt.ISODate)}</b> CET")
        
    def start_time_update_thread(self):
        self.time_update_worker = self.TimeUpdateThread(self)
        self.time_update_worker.start()

    class TimeUpdateThread(QThread):

        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent

        def run(self):
            while True:
                self.parent.update_global_time_label()
                self.sleep(1)  # Use QThread's sleep method instead of time.sleep
