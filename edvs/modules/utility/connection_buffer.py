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
import time

from PySide6.QtCore import QObject

# ================================================================= #

class ConnectionBuffer(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.ui = parent.ui
        self.serial = parent.serial
        self.config = parent.config
        self.terminal = parent.terminal

        # messages from config
        self.message_ports_update = self.config.get(
            "serial.ports_update", 2)
        self.message_error_connecting = self.config.get(
            "serial.error_connecting", 2)
        self.message_disconnected = self.config.get(
            "serial.disconnected", 2)
        self.message_connected = self.config.get(
            "serial.connected", 2)

        # logs folder from config
        self.logs_folder = self.config.get(
                "application.settings.logs_folder")

    # ================================================================= #

    # == Update Ports == #
    def update_ports(self, override_message=False):
        
        self.serial.update_ports()
        self.ui.cb_ports.clear()
        
        if len(self.serial.portList) == 0:
            available_ports = "0"

        else:
            available_ports = str(
                self.serial.portList).replace(
                "['", "").replace(
                "']", "")
            
            self.ui.cb_ports.addItems(
                self.serial.portList)


        if override_message == False:
            self.terminal.write(
                self.message_ports_update.replace(
                    "$PORT_LIST", f"{available_ports}"))
    
    # == Send Data == #
    def send_data(self):
        data = self.ui.terminal_input.text()

        # if the data is a command
        if data.startswith(self.config.get("application.settings.command_prefix")):
            self.parent.terminal.handle_command(data)

        # else send the data
        else:
            if self.serial.is_connected:
                if len(data) > 0:
                    try:
                        self.serial.send_data(data)
                        self.parent.terminal.write(
                            f"<b style='color:#8cb854;'>(OK)</b> <ins style='color:#8cb854';>[Sended - '{data}']</ins>")
                    except:
                        self.parent.terminal.write(
                            f"<b style='color:#a8002a;'>(!)</b> <b style='color:#a8002a;'>[Error Sending]</b> '{data}'")

                else:
                    self.parent.terminal.write("<b style='color:#a8002a;'>(!)</> <ins style='color:#a8002a;'>[Aborting - Data Is Empty]</ins>")
                    
            else:
                self.parent.terminal.write(
                    "<b style='color:#a8002a;'>(!)</b> <ins style='color:#a8002a';>[Error Sending - Not Connected] </ins>")

        self.ui.terminal_input.setText("")
    
    # == BTN_Connect == #
    def connect(self):
        
        # update ports in case the device is disconnected
        self.update_ports(True)
        
        # if the device is unplugged
        if self.serial.is_unplugged:
            self.terminal.write("DEVICE UNPLUGGED")
            
        elif self.serial.dummy_enabled:
            self.error_connecting()
            
        # if you are already connected
        elif self.serial.is_connected:
            self.disconnect()
        
        # connect
        else:
            # if you the combobox is empty
            if len(self.ui.cb_ports.currentText()) == 0:
                self.error_connecting()

            else:
                # change the connection variables to the ones in the ComboBoxes
                self.serial.ser.port = self.ui.cb_ports.currentText()
                self.serial.ser.baudrate = self.ui.cb_bauds.currentText()

                # Attempt to connect to the port
                self.serial.connect_serial()
                
                if self.serial.ser.is_open:
                    
                    # set connected to True
                    self.serial.is_connected = True
                    
                    # format the message from the configuration file
                    formated_msg = self.message_connected.replace(
                        "$PORT",
                        f"{self.serial.ser.portstr}"
                    )
                    
                    # update terminal with the connnected message and add a port to the connected label
                    self.terminal.write(formated_msg)

                    # change the button text to connected
                    self.ui.btn_connect_serial.setText("connected")
                    
                    # update the status bar
                    self.parent.update_status_bar(f"// #CONNECTED -> {self.serial.ser.portstr} <- {self.serial.ser.baudrate}")

    # == Disconnect == #
    def disconnect(self):
        # disconnect from the port using the serial util
        self.serial.disconnect_serial()

        # change button text to disconnected
        self.ui.btn_connect_serial.setText("disconnected")
        
        # format the message from the configuration file
        formated_msg = self.message_disconnected.replace(
            "$PORT", 
            f"{self.serial.ser.portstr}")
        
        # send the a terminal message confirming the action 
        self.terminal.write(formated_msg)
        
        # update the connection state
        self.serial.is_connected = False
        
        # update the status bar
        self.parent.update_status_bar("")
        self.serial.start_error = False
        
    # == Error Connecting == #
    def error_connecting(self):
        # change button checked status and label
        self.ui.btn_connect_serial.setChecked(False)
        self.ui.btn_connect_serial.setText("ERROR")
        
        # update the terminal with the error message
        self.terminal.write(self.message_error_connecting)
        
        # update the status bar
        self.parent.update_status_bar(f"// #ERROR_CONNECTING")
        
    # == Toggle recording == #
    def toggle_recording(self):
        
        if self.ui.btn_togle_log.isChecked():
            
            # if the path dont exits, create it
            if not os.path.exists(self.logs_folder):
                os.mkdir(self.logs_folder)
            
            log_date = time.strftime("%d.%m.%y")
            log_number = 1
            log_id = f"{log_date}-{log_number}" 
            logs_path = f"{self.logs_folder}/flight_data-{log_id}.csv"
            
            while os.path.exists(logs_path):
                log_number = log_number+1
                log_id = f"{log_date}-{log_number}"
                logs_path = f"{self.logs_folder}/flight_data-{log_id}.csv"
            
            self.serial.logs_file = open(logs_path, "w", newline='')
            
            self.serial.record_enabled = True
            self.terminal.write(f"<b style='color:#8cb854;'>(OK)</b> Recording: <ins style='color:#8cb854';>ON</ins> (<b>{logs_path}</b>)")
            
        else:
            self.serial.record_enabled = False
            
            self.file = self.serial.logs_file
            self.file.close()
            
            self.terminal.write(
                "<b style='color:#8cb854;'>(OK)</b> Recording: <ins style='color:#a8002a';>OFF</ins>")