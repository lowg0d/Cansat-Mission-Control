![](https://i.imgur.com/rLJG0se.png)

# EDVS - Cansat Mission Control Gui - Python 3.11.2

## What's this !??
> * SRC of a "**Mission Control**" or "**Ground Station**" **Full Customizable** GUI built in *Python 3.11.1* with PyQt5 & pyqtgraph. With features like: **simulation mode** with no hardware needed, also can be used as a cooler serial monitor & more things...
[Feature Explanation Video](https://www.youtube.com/watch?v=cgqOD5_pZTY)

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjE5ZGM2ZjhlZjNjNjE3MmE0Njc4NGY2NDU3MDA1ZGU1MmQ5YjFmNyZjdD1n/7VuKns94zZbgkmnfyr/giphy.gif)

## Features
> * [Feature Explanation Video](https://www.youtube.com/watch?v=cgqOD5_pZTY)
 Serial Communication, can be used as a serial monitor for sending and receive data.
>* "Filtering" can set a maximum and minimum threshold for the data, if the data exceeds the maximum or minimum, the maximum or minimum value will be displayed depending on the one that has been exceeded.
>* Full Customization of the graphs, add, change, delete, The Ui file is on the code so you can edit it, also can add more "blocks" on the topbar for displaying data that does not need a graph. 
>* Simulation mode for use without hardware, you can change the time for each update.
>* UnPlug Detection, if you unplug de device without desconecting your computer is going to beep :)
>* Display of the current time, is displayed in CET but you can change that also.
>* It has a burger menu for displaying the connection info, you can hide it when you are not using it.
>* It has keybinds for moving between the pages, F1: terminal, F2: Flight or data plotting, F11: show in fullscreen.

## Contents
> * [Installation](#installation)
> * [How to Use ?](#how-to-use)
> * [Known Bugs](#known-bugs)
> * [Working On](#currently-working)
> * [License](#license)

## Installation
> Clone this repository and then get into the folder. In the terminal write the following command depending on your OS:

* Windows
```shell
python -m venv .venv
.\.venv\Scripts\activate 
```

* Linux
```shell
python -m venv .venv
source .venv/bin/activate
```

> Then install the requirements with (no matter your os):
```shell
pip install -r .\requirements.txt
```

> After this the program should be good to go, to initialize the program type:
```shell
python .\launcher.py
```

## how to use
> Just select the port and the baudrate and connect it !

* **Custom Graphs**
> Modifying the graphs is really easy, go to *./edvs/modules/managers/graph_manager.py*, first create a new object with the class of the graph you want to use in the *set_graph()* function, also you need to add it to a layout, you can use the existing ones as example. Then you need to add the update function of your graph with the respective data into the *update()* function. For modifying the graph objects go to *./edvs/modules/utility/graph_types.py* and have fun!

* **Terminal Commands:**
> Type "*/help*" to show all the command in the terminal line, if the message start with the command prefix (you can change it in the config) the data is not sent, but interpreted as a command.

* **Dummy:**
>* "*/dummy.on*" for starting the simulation
>* "*/dummy.off*" you can guess
>* "*/dummy.time* (time)" change the update time for the data to appear, time need to be a float and in seconds, 0.5 for half a second 1.0 for a second.

* **Unplug Mode:**
> Unplug it !!

* **Saves**
> The record button saves all the data comming from the serial port to a csv file, you can open the folder in config tab or by a typing "/saves" in the terminal.

## Known bugs
>* Graphs Randomly resize depending on the data
>* The full timeline is not shown in the x axis of the graph

## Currently working
> * Fixing Things
> * Flight recontrusction
> * The bugs

## LICENSE:
<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png" /></a><br />

> * Software in this repository is licensed under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) unless otherwise **indicated**.

**WHY NOT MIT??????????????????**
> * I don't want this software or its derivatives to be sold or make a profit, I think it should be free and open source, this software will always be free for anyone who needs it.

## Inspiration:
>* **Mayor inspiration for Graphs:** https://github.com/el-NASA/CanSat-Ground-station
