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

import platform
from PyQt5.QtCore import QObject, QTime

# ================================================================= #

class TerminalManager(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui
        self.config = parent.config

        self.command_prefix = self.config.get(
            "application.settings.command_prefix")
        
        self.disconnected_msg = self.config.get(
            "serial.disconnected", 2)

    # == write in the terminal == #
    def write(self, data, override_time_stamp=False):
        time_str = QTime.currentTime().toString("hh:mm:ss.zzz")
        time_stamp = time_str.ljust(10)

        if not override_time_stamp:
            if self.parent.serial.is_connected:
                if self.parent.serial.record_enabled == True:
                    time_stamp += " (R)"

                prefix = f"[{time_stamp} <strong style='color:#786fa6';>{self.parent.serial.ser.name}</strong>]:"

            elif self.parent.serial.dummy_enabled == True:
                prefix = f"[{time_stamp} <strong style='color:#786fa6';>Dummy</strong>]:"

            else:
                prefix = f"[{time_stamp} <strong>EDVS</strong>]:"

        else:
            prefix = f"[<strong>EDVS</strong>]:"

        self.ui.terminal.append(f"\t<td>{prefix} {data}</td>")


    def insert(self, data):
        self.ui.terminal.insertPlainText(data)

    # == clear terminal == #
    def clear(self):
        self.ui.terminal.clear()

    # ================================================================= #

    # == handle commands == #
    def handle_command(self, raw_data):
        data = raw_data.lower()
        
        if data == f"{self.command_prefix}help":
            
            self.write("<b style='color:#8cb854;'>(OK)</b> Available Commands:")
            self.ui.terminal.append(f"""- <b>{self.command_prefix}clear:</b> clear the terminal""")
            self.ui.terminal.append(f"""- <b>{self.command_prefix}reload:</b> reload the window""")
            self.ui.terminal.append(f"""- <b>{self.command_prefix}dummy:</b> (.on) (.off) (.time [time])""")
            self.ui.terminal.append(f"""- <b>{self.command_prefix}saves:</b> open the saves folder""")
            
        elif data == f"{self.command_prefix}clear":
            self.clear()

        elif data == f"{self.command_prefix}saves":
            self.parent.opn_logs()

        elif data == f"{self.command_prefix}reload":
            self.parent.window_manager.reload_window()

        elif data == f"{self.command_prefix}dummy.on":
            self.parent.serial.start_dummy()

        elif data == f"{self.command_prefix}dummy.off":
            self.parent.serial.stop_dummy()

        elif data.startswith(f"{self.command_prefix}dummy.time"):
            if self.parent.serial.dummy_enabled == True:
                try:
                    time = data.replace(f"{self.command_prefix}dummy.time", "")
                    converted = float(time)
                    self.parent.serial.set_dummy_time(converted)
                except ValueError:
                    self.write(f"<b style='color:#a8002a;'>(!) INVALID or NONE arguments given")

            else:
                self.write(f"<b style='color:#a8002a;'>(!) Dummy is Disabled </b>")
                
        else:
            self.write(f"<b style='color:#a8002a;'>(!) Unknown command '{data}' - try /help</b>")


    def boot_up_message(self):
        message = f"""888888 8888b.  Yb    dP .dP"Y8  ▸  Elburgo Data Visualization Software
88__    8I  Yb  Yb  dP  `Ybo."  ▸  VERSION: {self.parent.window_version}
88""    8I  dY   YbdP   o.`Y8b  ▸  RUNNING: OS:{platform.system()}-{platform.release()} | Python:{platform.python_version()}
888888 8888Y"     YP    8bodP'  ▸  AUTHOR: Martin Ortiz
"""
        self.ui.terminal.append(message)  
        self.write("<ins style='color:#8cb854;'><b>(✓)</b> Sucesfully Started</ins>")