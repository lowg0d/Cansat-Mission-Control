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

from PyQt5 import QtWidgets

import edvs.modules.managers.configuration_manager as config 
import requests
import json

file_id = "1Bg01rpEaLpgDt1DA0Nggs78-1LWj_xEe"
drive_link = "https://drive.google.com/uc?id="

# ============================================================== #

def check_version():
    
    # = get the lastet version from the file in drive
    response = requests.get(drive_link+file_id)
    cloud_version = json.loads(response.content)

    # = setup instances
    current = config.get('version.version')
    lastest = cloud_version["version"]
    
    if lastest > current:
        new_status = cloud_version["status"]
        resturn_str = f"{new_status}-{lastest}" 
        return resturn_str
    
    else:
        return False
    
class DownloadUpdateManager(QtWidgets.QMainWindow):
    def __init__(self):
        pass
    
    def download(self, cloud_version, lastet_version):
        
        new_status = cloud_version["status"]
        new_version_download = cloud_version["download"]
        print(lastet_version + new_status + new_version_download)