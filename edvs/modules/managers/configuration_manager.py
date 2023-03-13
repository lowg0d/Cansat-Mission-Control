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

import sys
import json

configuration_file_path = "./edvs/config/config.json"
message_file_path = "./edvs/config/messages.json"

# ============================================================== #

# get data from the configuration or message file, default file is 1, config.
def get(index, file_index=1):
    
    # set the file
    if file_index == 1:
        path = configuration_file_path
   
    else:
        path = message_file_path
        
    # Open The File
    with open(path) as f:
        config = json.load(f)
    
    # get the value
    for key in index.split('.'):
        if key not in config:
            sys.exit(f"[CONFIG] '{key}' is not a valid key")
        config = config[key]
    
    # return the value
    return config

# ============================================================== #

# edit data from the configuration or message file, default file is 1, config.
def edit(index, value, file_index=1):
    
    # set the file
    if file_index == 1:
        path = configuration_file_path
   
    else:
        path = message_file_path
    
    # open the file on read mode
    with open(path, 'r') as file:
        config_file = json.load(file)

    # localize the key and update the value
    keys = index.split('.')
    current = config_file
    for key in keys[:-1]:
        if key not in current:
            sys.exit(f"[CONFIG] '{key}' is not a valid key")
        current = current[key]
    current[keys[-1]] = value

    # overwrite the json with the new value
    with open(path, 'w') as file:
        json.dump(config_file, file, indent=4)
