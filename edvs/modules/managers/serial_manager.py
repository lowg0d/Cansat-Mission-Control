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

# ============================================================== #

import csv
import time
import numpy as np
import winsound

import serial
import serial.tools.list_ports

from PyQt5.QtCore import (QObject,
                            pyqtSignal,
                            QThread)

# ================================================================= #

class SerialManager(QObject):
    data_available = pyqtSignal(str)
    update_graphs = pyqtSignal(list)
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.ui = parent.ui
        self.terminal = parent.terminal
        self.config = parent.config
        
        self.start_error = False
        
        # serial & connection
        self.is_connected = False
        self.is_unplugged = False
        self.ser = serial.Serial()
        self.ser.timeout = self.config.get("connection.time_out")
        
        
        # logs
        self.logs_path = self.config.get("application.settings.logs_folder")
        self.logs_file = f"./{self.logs_path}/default.csv"
        self.record_enabled = False
        
        # dummy
        self.dummy_enabled = False
        self.dummy_update_time = self.config.get("graphs.dummy.default_update_time")
        
        self.baudratesDIC = self.config.get("connection.bauds_dic")
        self.portList = []
        
        self.message_unplugged = self.config.get("serial.un_plugged",2)
        self.message_replugged = self.config.get("serial.re_plugged",2)
    
    # ================================================================= #
    
    # == Update Ports == #
    def update_ports(self):
        try:
            self.portList = [
                port.device for port in serial.tools.list_ports.comports()]

        except Exception as e:
            self.parent.terminal.write(f"[-] Error Updating Ports - {e}")
    
    # ================================================================= #
    
    # == Connect == #
    def connect(self):
        try:
            self.ser.open()
            self.start_thread()
    
        except Exception as e:
            self.parent.terminal.write(f"[-] Error Connecting - {e}")

    # == Disconnect == #
    def disconnect(self):
          
        try:
            self.stop_thread()
            self.ser.close()    
            
        except Exception as e:
            self.parent.terminal.write(f"[-] Error Disconnecting - {e}")

    # ================================================================= #

    # == Send Data == #
    def send_data(self, data):
        try:
            b_data = bytes(data, 'utf-8')
            self.ser.write(b_data)
            
        except Exception as e:
            self.parent.terminal.write(f"[-] Error Sending Data - {e}")

    # == Read Serial == #
    def read_serial(self):
        data = self.ser.readline().decode("utf-8")
        if len(data) > 1:
            data_dic = str(data).strip().split(";")
            if '#' in str(data):
                self.start_error = True
               
            self.update_graphs.emit(data_dic)
            self.data_available.emit(str(data_dic))
            
            if self.record_enabled == True:
                values = data.split(";")
                writer = csv.writer(self.logs_file, delimiter=",")
                writer.writerow(values)

    # ================================================================= #
    
    # == Dummy Serial == #
    def dummy_serial(self):
        """
        data_dic = np.concatenate(([1], np.random.choice(range(-20, 100), 2), [np.random.randint(0, 4)], np.random.choice(range(-10, 20), 8)))
        """
        
        # Initialize the last data value to use as a reference point
        last_latitude = 42.84283
        last_longitude = -2.66806
        last_temperature = 14
        last_altitude = 0.0

        # Generate random data with correlation to the last data value
        humidity = np.random.uniform(0, 100)
        pressure = np.random.uniform(800, 1200)
        random_value = np.random.randint(0, 10)
        latitude = last_latitude + np.random.uniform(0.21, 0.01)
        longitude = last_longitude + np.random.uniform(0.11, 0.01)
        speed = np.random.uniform(0, 100)
        altitude = np.random.uniform(0, 70) + last_altitude

        temperature_decrease = np.random.uniform(-10, 1)
        temperature = max(last_temperature - temperature_decrease, 0)
        
        # Combine the data into a numpy array
        data_dic = np.concatenate(([temperature], [humidity], [pressure], [random_value], [latitude], [longitude], [speed], [altitude]))

        # Update the last data value
        last_latitude = latitude
        last_longitude = longitude
        last_temperature = temperature
        
        self.update_graphs.emit(list(data_dic))
        self.data_available.emit(f"<ins style>{data_dic}")
        
        time.sleep(self.dummy_update_time)
    
    # == Start Dummy == #
    def start_dummy(self):
        if self.is_connected == False:
            self.dummy_enabled = True
            self.start_thread()
            
            self.terminal.write("<b style='color:#8cb854;'>(OK)</b> Dummy: <ins style='color:#8cb854';>ON</ins>")
            self.parent.update_status_bar(f"// DUMMY -> ON <- {self.dummy_update_time}")

    # == Stop Dummy == #
    def stop_dummy(self):
        self.stop_thread()
        self.dummy_enabled = False
        
        self.terminal.write("<b style='color:#8cb854;'>(OK)</b> Dummy: <ins style='color:#a8002a';>OFF</ins>")
        self.parent.update_status_bar("")
        
    # == Set Dummy Time == #
    def set_dummy_time(self, time):
        self.terminal.write(f"<b style='color:#8cb854;'>(OK)</b> Dummy Time updated: <b>{time}</b>")
        self.dummy_update_time = time
        self.parent.update_status_bar(f"// DUMMY -> ON <- {self.dummy_update_time}")
       
    # ================================================================= #
    # == Serial/Dummy Reader == #
    class WorkerThread(QThread):
        
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
        
        def run(self):
            # == DUMMY ENABLED == #
            if self.parent.dummy_enabled == True:
                while self.parent.dummy_enabled:
                    self.parent.dummy_serial()
            
            # == NORMAL CONNECTION == #
            else:
                while self.parent.is_connected:
                    # == IF SERIAL IS OPEN == #
                    if (self.parent.ser.isOpen()):
                        while (self.parent.ser.isOpen()):
                            try:
                                self.parent.read_serial()
                            
                            except serial.SerialException:
                                self.is_unplugged = True
                                self.parent.ser.close()
                        
                    # == DEVICE UNPLUGGED == #
                    else:
                        self.parent.parent.update_status_bar("Unplugged")
                        self.parent.ui.lb_connection_info.setText(
                            "<b style='color:#a8002a;'>UNPLUGGED</b>")
                        
                        self.parent.data_available.emit(
                            self.parent.message_unplugged)

                        while not self.parent.ser.is_open:
                            try:
                                self.parent.ser.open()

                                self.parent.data_available.emit(
                                    self.parent.message_replugged)
                                
                                self.parent.ui.lb_connection_info.setText(
                                    f"<strong style='color:#8cb854'>{self.parent.ser.portstr}</strong>")

                                self.parent.parent.update_status_bar(f"// CONNECTED -> {self.parent.ser.portstr} <- {self.parent.ser.baudrate}")

                                self.is_unplugged = False
                                break

                            except:
                                winsound.Beep(575, 393)
    
    def start_thread(self):
        
        self.worker = self.WorkerThread(self)
        self.worker.start()

    def stop_thread(self):
        self.worker.terminate()
        