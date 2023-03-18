![](https://i.imgur.com/rLJG0se.png)

# EDVS - Cansat Mission Control Gui - Python 3.11.1

## What's this !??
> * SRC of a "**Mission Control**" or "**Ground Station**" **Full Customizable** GUI built in *Python 3.11.1* with PyQt5 & pyqtgraph. With features like: **simulation mode** with no hardware needed, also can be used as a cooler serial monitor & more things...
[Feature Explanation Video](https://www.youtube.com/@lowgod9010)

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGJiYzQ3NGFjMWI0MmE5ZjEzMjRjYjM5MTI2YTI3YTY4N2Q1YmU4OSZjdD1n/vXACYcx3Jrt4kkuptc/giphy.gif)

## Features
> * [Feature Explanation Video](https://www.youtube.com/@lowgod9010)
 Serial Communication, can be used as a serial monitor for sending and receive data.
>* Full Customization of the graphs, add, change, delete, The Ui file is on the code so you can edit it, also can add more "blocks" on the topbar for displaying data that does not need a graph. 
>* Simulation mode for use without hardware, you can change the time for each update.
>* UnPlug Detection, if you unplug de device without desconecting your computer is going to beep :)
>* Display of the current time, is displayed in CET but you can change that also.

## Contents
> * [Installation](#installation)
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
