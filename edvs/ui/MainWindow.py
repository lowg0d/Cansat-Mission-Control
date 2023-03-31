# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
import edvs.ui.resources.src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1105, 664)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"QWidget{\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QStatusBar{\n"
"	color: rgba(255, 255, 255,0.5);\n"
"	\n"
"	font:7.5pt \"Arame Mono\";\n"
"	border-top: 1px solid rgba(20, 20, 20, 0.9);;\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QSizeGrip{\n"
"	border-top: 1px solid rgba(20, 20, 20, 0.9);;\n"
"	background-color: rgba(0, 0, 0, 0.0);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"	margin: 0 1;	\n"
"	image: url(:/src/icons/grip_icon.png);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Arame Mono"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.NoAntialias)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"font: 9pt \"Arame Mono\";")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fr_top_bar = QFrame(self.centralwidget)
        self.fr_top_bar.setObjectName(u"fr_top_bar")
        self.fr_top_bar.setMaximumSize(QSize(16777215, 35))
        self.fr_top_bar.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.3)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(205, 205, 205, 0.3)\n"
"}")
        self.fr_top_bar.setFrameShape(QFrame.NoFrame)
        self.fr_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_togle_menu = QPushButton(self.fr_top_bar)
        self.btn_togle_menu.setObjectName(u"btn_togle_menu")
        sizePolicy.setHeightForWidth(self.btn_togle_menu.sizePolicy().hasHeightForWidth())
        self.btn_togle_menu.setSizePolicy(sizePolicy)
        self.btn_togle_menu.setMinimumSize(QSize(50, 35))
        self.btn_togle_menu.setMaximumSize(QSize(45, 35))
        self.btn_togle_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_togle_menu.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(39, 39, 39);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(59, 59, 59);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(155, 155, 155, 0.2)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/src/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_togle_menu.setIcon(icon)
        self.btn_togle_menu.setIconSize(QSize(29, 29))

        self.horizontalLayout.addWidget(self.btn_togle_menu)

        self.line_3 = QFrame(self.fr_top_bar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(1, 0))
        self.line_3.setMaximumSize(QSize(1, 45))
        self.line_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.time_label = QLabel(self.fr_top_bar)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(149, 0))
        self.time_label.setStyleSheet(u"color: rgba(255, 255, 255, 0.2);\n"
"background-color: rgb(39, 39, 39);")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.time_label)

        self.line_hide_4 = QFrame(self.fr_top_bar)
        self.line_hide_4.setObjectName(u"line_hide_4")
        self.line_hide_4.setMinimumSize(QSize(1, 0))
        self.line_hide_4.setMaximumSize(QSize(1, 45))
        self.line_hide_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.line_hide_4.setFrameShape(QFrame.HLine)
        self.line_hide_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_hide_4)

        self.lb_countdown = QLabel(self.fr_top_bar)
        self.lb_countdown.setObjectName(u"lb_countdown")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_countdown.sizePolicy().hasHeightForWidth())
        self.lb_countdown.setSizePolicy(sizePolicy1)
        self.lb_countdown.setMinimumSize(QSize(95, 35))
        self.lb_countdown.setMaximumSize(QSize(95, 35))
        self.lb_countdown.setStyleSheet(u"QLabel{\n"
"color: rgba(255, 255, 255, 0.2);\n"
"background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgba(255, 255, 255, 0.2);\n"
"}")
        self.lb_countdown.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_countdown)

        self.line_hide_3 = QFrame(self.fr_top_bar)
        self.line_hide_3.setObjectName(u"line_hide_3")
        self.line_hide_3.setMinimumSize(QSize(1, 0))
        self.line_hide_3.setMaximumSize(QSize(1, 45))
        self.line_hide_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.line_hide_3.setFrameShape(QFrame.HLine)
        self.line_hide_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_hide_3)

        self.lb_ping = QLabel(self.fr_top_bar)
        self.lb_ping.setObjectName(u"lb_ping")
        sizePolicy1.setHeightForWidth(self.lb_ping.sizePolicy().hasHeightForWidth())
        self.lb_ping.setSizePolicy(sizePolicy1)
        self.lb_ping.setMinimumSize(QSize(80, 35))
        self.lb_ping.setMaximumSize(QSize(95, 35))
        self.lb_ping.setStyleSheet(u"QLabel{\n"
"color: rgba(255, 255, 255, 0.2);\n"
"background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgba(255, 255, 255, 0.2);\n"
"}")
        self.lb_ping.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_ping)

        self.line_hide_5 = QFrame(self.fr_top_bar)
        self.line_hide_5.setObjectName(u"line_hide_5")
        self.line_hide_5.setMinimumSize(QSize(1, 0))
        self.line_hide_5.setMaximumSize(QSize(1, 45))
        self.line_hide_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.line_hide_5.setFrameShape(QFrame.HLine)
        self.line_hide_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_hide_5)

        self.lb_state = QLabel(self.fr_top_bar)
        self.lb_state.setObjectName(u"lb_state")
        sizePolicy1.setHeightForWidth(self.lb_state.sizePolicy().hasHeightForWidth())
        self.lb_state.setSizePolicy(sizePolicy1)
        self.lb_state.setMinimumSize(QSize(100, 35))
        self.lb_state.setMaximumSize(QSize(120, 35))
        self.lb_state.setStyleSheet(u"QLabel{\n"
"color: rgba(255, 255, 255, 0.2);\n"
"background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgba(255, 255, 255, 0.2);\n"
"}")
        self.lb_state.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_state)

        self.line_hide_6 = QFrame(self.fr_top_bar)
        self.line_hide_6.setObjectName(u"line_hide_6")
        self.line_hide_6.setMinimumSize(QSize(1, 0))
        self.line_hide_6.setMaximumSize(QSize(1, 45))
        self.line_hide_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.line_hide_6.setFrameShape(QFrame.HLine)
        self.line_hide_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_hide_6)

        self.top_bar_spacer = QSpacerItem(797, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.top_bar_spacer)

        self.btn_minimize = QPushButton(self.fr_top_bar)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(55, 35))
        self.btn_minimize.setMaximumSize(QSize(55, 35))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/src/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QSize(29, 29))

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_normalize = QPushButton(self.fr_top_bar)
        self.btn_normalize.setObjectName(u"btn_normalize")
        sizePolicy.setHeightForWidth(self.btn_normalize.sizePolicy().hasHeightForWidth())
        self.btn_normalize.setSizePolicy(sizePolicy)
        self.btn_normalize.setMinimumSize(QSize(55, 35))
        self.btn_normalize.setMaximumSize(QSize(55, 35))
        self.btn_normalize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_normalize.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/src/icons/notfullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_normalize.setIcon(icon2)
        self.btn_normalize.setIconSize(QSize(29, 29))

        self.horizontalLayout.addWidget(self.btn_normalize)

        self.btn_maximize = QPushButton(self.fr_top_bar)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy)
        self.btn_maximize.setMinimumSize(QSize(55, 35))
        self.btn_maximize.setMaximumSize(QSize(55, 35))
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximize.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/src/icons/fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon3)
        self.btn_maximize.setIconSize(QSize(29, 29))

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.fr_top_bar)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(55, 35))
        self.btn_close.setMaximumSize(QSize(55, 35))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(170, 0, 0,0.8);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(150, 0, 0,0.7);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/src/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(29, 29))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_5.addWidget(self.fr_top_bar)

        self.fr_content = QFrame(self.centralwidget)
        self.fr_content.setObjectName(u"fr_content")
        self.fr_content.setMinimumSize(QSize(0, 0))
        self.fr_content.setMaximumSize(QSize(16777215, 16777215))
        self.fr_content.setStyleSheet(u"")
        self.fr_content.setFrameShape(QFrame.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fr_menu = QFrame(self.fr_content)
        self.fr_menu.setObjectName(u"fr_menu")
        self.fr_menu.setMinimumSize(QSize(200, 0))
        self.fr_menu.setMaximumSize(QSize(0, 16777215))
        self.fr_menu.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px;\n"
"	color: rgba(255, 255, 255, 0.6);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgba(255, 255, 255, 0.9);\n"
"	background-color: rgba(255, 255, 255, 0.1)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(155, 155, 155, 0.2)\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgba(255, 255, 255, 0.8);\n"
"}")
        self.fr_menu.setFrameShape(QFrame.NoFrame)
        self.fr_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_5 = QFrame(self.fr_menu)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(200, 1))
        self.line_5.setMaximumSize(QSize(1, 1))
        self.line_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.fr_connection = QFrame(self.fr_menu)
        self.fr_connection.setObjectName(u"fr_connection")
        self.fr_connection.setMinimumSize(QSize(200, 80))
        self.fr_connection.setMaximumSize(QSize(200, 80))
        self.fr_connection.setStyleSheet(u"QComboBox{\n"
"	padding-left: 2px;\n"
"	border: 1px solid;\n"
"	border-color: rgb(30, 30, 30);\n"
"	color: rgba(255, 255, 255, 0.6);\n"
"	background-color: rgb(20, 20, 20);\n"
"	border-radius: 1px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	background-color: rgb(22, 22, 22);\n"
"}\n"
"\n"
"QComboBox:drop-down{\n"
"	border: 0px solid;\n"
"	color: rgba(255, 255, 255, 0.6);\n"
"}\n"
"\n"
"QComboBox QAbstractItem{\n"
"    selection-background-color:  rgba(0, 0, 0,0);\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	border-radius: 0;\n"
"	font: 700 9pt \"Arame Mono\";\n"
"}\n"
"\n"
"QListView{\n"
"	color: rgba(255, 255, 255, 0.6);\n"
"	border: 0px;\n"
"}\n"
"")
        self.fr_connection.setFrameShape(QFrame.NoFrame)
        self.fr_connection.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_connection)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_ports = QFrame(self.fr_connection)
        self.fr_ports.setObjectName(u"fr_ports")
        self.fr_ports.setMinimumSize(QSize(200, 40))
        self.fr_ports.setMaximumSize(QSize(200, 40))
        self.fr_ports.setStyleSheet(u"")
        self.fr_ports.setFrameShape(QFrame.NoFrame)
        self.fr_ports.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_ports)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.lb_Ports = QLabel(self.fr_ports)
        self.lb_Ports.setObjectName(u"lb_Ports")
        self.lb_Ports.setMinimumSize(QSize(0, 30))
        self.lb_Ports.setMaximumSize(QSize(16777215, 30))
        self.lb_Ports.setLayoutDirection(Qt.LeftToRight)
        self.lb_Ports.setStyleSheet(u"")
        self.lb_Ports.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_Ports)

        self.cb_ports = QComboBox(self.fr_ports)
        self.cb_ports.setObjectName(u"cb_ports")
        self.cb_ports.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_ports.setStyleSheet(u"border-radius: 1px;")
        self.cb_ports.setPlaceholderText(u"")

        self.horizontalLayout_4.addWidget(self.cb_ports)


        self.verticalLayout_2.addWidget(self.fr_ports)

        self.fr_bauds = QFrame(self.fr_connection)
        self.fr_bauds.setObjectName(u"fr_bauds")
        self.fr_bauds.setMinimumSize(QSize(200, 40))
        self.fr_bauds.setMaximumSize(QSize(200, 40))
        self.fr_bauds.setStyleSheet(u"")
        self.fr_bauds.setFrameShape(QFrame.NoFrame)
        self.fr_bauds.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_bauds)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.lb_Baudrate = QLabel(self.fr_bauds)
        self.lb_Baudrate.setObjectName(u"lb_Baudrate")
        self.lb_Baudrate.setMinimumSize(QSize(0, 30))
        self.lb_Baudrate.setMaximumSize(QSize(16777215, 30))
        self.lb_Baudrate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_Baudrate)

        self.cb_bauds = QComboBox(self.fr_bauds)
        self.cb_bauds.setObjectName(u"cb_bauds")
        self.cb_bauds.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_bauds.setStyleSheet(u"border-radius: 1px;")
        self.cb_bauds.setPlaceholderText(u"")

        self.horizontalLayout_3.addWidget(self.cb_bauds)


        self.verticalLayout_2.addWidget(self.fr_bauds)


        self.verticalLayout_3.addWidget(self.fr_connection)

        self.line_6 = QFrame(self.fr_menu)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(200, 1))
        self.line_6.setMaximumSize(QSize(1, 1))
        self.line_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.fr_connection_btn = QFrame(self.fr_menu)
        self.fr_connection_btn.setObjectName(u"fr_connection_btn")
        self.fr_connection_btn.setMinimumSize(QSize(200, 30))
        self.fr_connection_btn.setMaximumSize(QSize(200, 30))
        self.fr_connection_btn.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(155, 155, 155, 0.1)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(155, 155, 155, 0.2)\n"
"}\n"
"")
        self.fr_connection_btn.setFrameShape(QFrame.NoFrame)
        self.fr_connection_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_connection_btn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_connect_serial = QPushButton(self.fr_connection_btn)
        self.btn_connect_serial.setObjectName(u"btn_connect_serial")
        sizePolicy.setHeightForWidth(self.btn_connect_serial.sizePolicy().hasHeightForWidth())
        self.btn_connect_serial.setSizePolicy(sizePolicy)
        self.btn_connect_serial.setMinimumSize(QSize(100, 30))
        self.btn_connect_serial.setMaximumSize(QSize(100, 30))
        self.btn_connect_serial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect_serial.setStyleSheet(u"QPushButton{\n"
"color: rgb(168, 0, 42);\n"
"border: 0.5px solid;\n"
"border-color: rgb(168, 0, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:  rgb(140, 184, 84);\n"
"border: 0.5px solid;\n"
"border-color:  rgb(140, 184, 84);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_connect_serial.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_connect_serial)

        self.btn_update_ports = QPushButton(self.fr_connection_btn)
        self.btn_update_ports.setObjectName(u"btn_update_ports")
        sizePolicy.setHeightForWidth(self.btn_update_ports.sizePolicy().hasHeightForWidth())
        self.btn_update_ports.setSizePolicy(sizePolicy)
        self.btn_update_ports.setMinimumSize(QSize(100, 30))
        self.btn_update_ports.setMaximumSize(QSize(100, 30))
        self.btn_update_ports.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_ports.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_update_ports)


        self.verticalLayout_3.addWidget(self.fr_connection_btn)

        self.line_7 = QFrame(self.fr_menu)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(200, 1))
        self.line_7.setMaximumSize(QSize(1, 1))
        self.line_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_7)

        self.fr_util_btn = QFrame(self.fr_menu)
        self.fr_util_btn.setObjectName(u"fr_util_btn")
        self.fr_util_btn.setMinimumSize(QSize(200, 30))
        self.fr_util_btn.setMaximumSize(QSize(200, 30))
        self.fr_util_btn.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(155, 155, 155, 0.1)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(155, 155, 155, 0.2)\n"
"}\n"
"")
        self.fr_util_btn.setFrameShape(QFrame.NoFrame)
        self.fr_util_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fr_util_btn)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_togle_log = QPushButton(self.fr_util_btn)
        self.btn_togle_log.setObjectName(u"btn_togle_log")
        sizePolicy.setHeightForWidth(self.btn_togle_log.sizePolicy().hasHeightForWidth())
        self.btn_togle_log.setSizePolicy(sizePolicy)
        self.btn_togle_log.setMinimumSize(QSize(100, 30))
        self.btn_togle_log.setMaximumSize(QSize(100, 30))
        self.btn_togle_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_togle_log.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"color: rgb(140, 184, 84);\n"
"border: 0.5px solid;\n"
"border-color: rgb(140, 184, 84);\n"
"}\n"
"")
        self.btn_togle_log.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.btn_togle_log)

        self.btn_clear = QPushButton(self.fr_util_btn)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QSize(100, 30))
        self.btn_clear.setMaximumSize(QSize(100, 30))
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.btn_clear)


        self.verticalLayout_3.addWidget(self.fr_util_btn)

        self.line_9 = QFrame(self.fr_menu)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(200, 1))
        self.line_9.setMaximumSize(QSize(1, 1))
        self.line_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_9)

        self.btn_menu_1 = QPushButton(self.fr_menu)
        self.btn_menu_1.setObjectName(u"btn_menu_1")
        sizePolicy.setHeightForWidth(self.btn_menu_1.sizePolicy().hasHeightForWidth())
        self.btn_menu_1.setSizePolicy(sizePolicy)
        self.btn_menu_1.setMinimumSize(QSize(200, 40))
        self.btn_menu_1.setMaximumSize(QSize(200, 40))
        self.btn_menu_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_1.setStyleSheet(u"")
        self.btn_menu_1.setCheckable(False)
        self.btn_menu_1.setChecked(False)

        self.verticalLayout_3.addWidget(self.btn_menu_1)

        self.line_12 = QFrame(self.fr_menu)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMinimumSize(QSize(200, 1))
        self.line_12.setMaximumSize(QSize(1, 1))
        self.line_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_12)

        self.btn_menu_2 = QPushButton(self.fr_menu)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        sizePolicy.setHeightForWidth(self.btn_menu_2.sizePolicy().hasHeightForWidth())
        self.btn_menu_2.setSizePolicy(sizePolicy)
        self.btn_menu_2.setMinimumSize(QSize(200, 40))
        self.btn_menu_2.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamilies([u"Arame Mono"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.btn_menu_2.setFont(font1)
        self.btn_menu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_2.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_menu_2)

        self.line_8 = QFrame(self.fr_menu)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(200, 1))
        self.line_8.setMaximumSize(QSize(1, 1))
        self.line_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_8)

        self.verticalSpacer = QSpacerItem(20, 366, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.line_11 = QFrame(self.fr_menu)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(200, 1))
        self.line_11.setMaximumSize(QSize(200, 1))
        self.line_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_11)

        self.btn_menu_config = QPushButton(self.fr_menu)
        self.btn_menu_config.setObjectName(u"btn_menu_config")
        sizePolicy.setHeightForWidth(self.btn_menu_config.sizePolicy().hasHeightForWidth())
        self.btn_menu_config.setSizePolicy(sizePolicy)
        self.btn_menu_config.setMinimumSize(QSize(200, 40))
        self.btn_menu_config.setMaximumSize(QSize(200, 40))
        self.btn_menu_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_config.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_menu_config)


        self.horizontalLayout_5.addWidget(self.fr_menu)

        self.stackedWidget = QStackedWidget(self.fr_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QTextBrowser{\n"
"background-color: rgba(20,21,22,255);\n"
"}\n"
"QScrollBar{\n"
"	border:none;\n"
"	background-color: rgb(32, 32, 32);\n"
"	width:14px;\n"
"	margin:15px 0 15px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color: rgb(50, 52, 54);\n"
"	min-height: 30px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical:hover{\n"
"	\n"
"	background-color: rgb(73, 75, 78);\n"
"}\n"
"\n"
"QScrollBar::sub-line{\n"
"	border: none;\n"
"	background-color: rgb(50, 52, 54);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(50, 52, 54);\n"
"	height: 15px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(73, 75, 78);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(50, 52, 54);\n"
"	height: 15px;\n"
""
                        "	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(73, 75, 78);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page_1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.terminal = QTextBrowser(self.page_1)
        self.terminal.setObjectName(u"terminal")
        sizePolicy.setHeightForWidth(self.terminal.sizePolicy().hasHeightForWidth())
        self.terminal.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Arame Mono"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.terminal.setFont(font2)
        self.terminal.setStyleSheet(u"QTextBrowser{\n"
"	color:rgba(77, 235, 220, 0.8);\n"
"	border: 0px solid;\n"
"	font: 10pt \"Arame Mono\";\n"
"	text-align: left;\n"
"}\n"
"\n"
"\n"
"")
        self.terminal.setFrameShape(QFrame.NoFrame)
        self.terminal.setFrameShadow(QFrame.Plain)
        self.terminal.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.terminal.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.terminal.setAutoFormatting(QTextEdit.AutoNone)
        self.terminal.setDocumentTitle(u"")
        self.terminal.setLineWrapMode(QTextEdit.NoWrap)
        self.terminal.setMarkdown(u"")
        self.terminal.setOverwriteMode(False)
        self.terminal.setOpenLinks(False)

        self.verticalLayout_4.addWidget(self.terminal)

        self.fr_command_input = QFrame(self.page_1)
        self.fr_command_input.setObjectName(u"fr_command_input")
        self.fr_command_input.setMinimumSize(QSize(0, 30))
        self.fr_command_input.setMaximumSize(QSize(16777215, 30))
        self.fr_command_input.setLayoutDirection(Qt.LeftToRight)
        self.fr_command_input.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.fr_command_input.setFrameShape(QFrame.NoFrame)
        self.fr_command_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.fr_command_input)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.terminal_input = QLineEdit(self.fr_command_input)
        self.terminal_input.setObjectName(u"terminal_input")
        self.terminal_input.setMinimumSize(QSize(0, 30))
        self.terminal_input.setMaximumSize(QSize(16777215, 30))
        self.terminal_input.setStyleSheet(u"font: 10pt \"Arame Mono\";\n"
"color: rgba(255, 255, 255, 0.8);\n"
"background-color: rgb(49, 49, 49);\n"
"border: 0px solid;")

        self.horizontalLayout_7.addWidget(self.terminal_input)

        self.line_10 = QFrame(self.fr_command_input)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(1, 30))
        self.line_10.setMaximumSize(QSize(1, 30))
        self.line_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_10)

        self.btn_send = QPushButton(self.fr_command_input)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setMinimumSize(QSize(60, 30))
        self.btn_send.setMaximumSize(QSize(60, 30))
        self.btn_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(65,65, 65, 0.5);\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.btn_send)


        self.verticalLayout_4.addWidget(self.fr_command_input)

        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"background-color: rgba(20,21,22,255);\n"
"border: 0px solid;")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.fr_config = QFrame(self.page_3)
        self.fr_config.setObjectName(u"fr_config")
        self.fr_config.setStyleSheet(u"Line{\n"
"	background-color:rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	border: 1px solid;\n"
"	border-color: rgb(220,220,220);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgba(115, 175, 160, 0.9);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover{\n"
"	background-color: rgba(115, 175, 160, 0.9);\n"
"}\n"
"\n"
"QCheckBox::indicator:hover{\n"
"	background-color: rgba(240,240,240,0.1);\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"	color: rgb(250,250,250);\n"
"}\n"
"")
        self.fr_config.setFrameShape(QFrame.NoFrame)
        self.fr_config.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fr_config)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fr_config_buttons = QFrame(self.fr_config)
        self.fr_config_buttons.setObjectName(u"fr_config_buttons")
        self.fr_config_buttons.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: rgb(220,220,220);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(155, 155, 155, 0.1)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(155, 155, 155, 0.2)\n"
"}\n"
"")
        self.fr_config_buttons.setFrameShape(QFrame.StyledPanel)
        self.fr_config_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.fr_config_buttons)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_refresh = QPushButton(self.fr_config_buttons)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMinimumSize(QSize(70, 25))
        self.btn_refresh.setMaximumSize(QSize(60, 25))
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"border-radius: 2px;")

        self.horizontalLayout_12.addWidget(self.btn_refresh)

        self.btn_opn_logs = QPushButton(self.fr_config_buttons)
        self.btn_opn_logs.setObjectName(u"btn_opn_logs")
        self.btn_opn_logs.setMinimumSize(QSize(100, 25))
        self.btn_opn_logs.setMaximumSize(QSize(60, 25))
        self.btn_opn_logs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_opn_logs.setStyleSheet(u"border-radius: 2px;")

        self.horizontalLayout_12.addWidget(self.btn_opn_logs)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addWidget(self.fr_config_buttons)

        self.fr_config_default_bauds = QFrame(self.fr_config)
        self.fr_config_default_bauds.setObjectName(u"fr_config_default_bauds")
        self.fr_config_default_bauds.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid;\n"
"	border-left: 0px;\n"
"	border-color: rgb(220,220,220);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	background-color: rgb(22, 22, 22);\n"
"}\n"
"\n"
"QComboBox QAbstractItem{\n"
"    selection-background-color:   rgb(47, 175, 178);\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox:QAbstractItem:hover{\n"
"    color:rgba(52, 175, 160, 0.9);\n"
"}\n"
"\n"
"\n"
"QListView{\n"
"	color: rgba(255, 255, 255, 0.6);\n"
"	border: 0px;\n"
"}\n"
"")
        self.fr_config_default_bauds.setFrameShape(QFrame.StyledPanel)
        self.fr_config_default_bauds.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.fr_config_default_bauds)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.config_default_bauds_label = QLabel(self.fr_config_default_bauds)
        self.config_default_bauds_label.setObjectName(u"config_default_bauds_label")
        self.config_default_bauds_label.setMinimumSize(QSize(0, 19))
        self.config_default_bauds_label.setMaximumSize(QSize(16777215, 19))
        self.config_default_bauds_label.setStyleSheet(u"border: 1px solid;\n"
"border-right: 0px;\n"
"border-color: rgb(220,220,220);")
        self.config_default_bauds_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.config_default_bauds_label)

        self.config_default_bauds = QComboBox(self.fr_config_default_bauds)
        self.config_default_bauds.setObjectName(u"config_default_bauds")
        self.config_default_bauds.setMinimumSize(QSize(80, 0))
        self.config_default_bauds.setCursor(QCursor(Qt.PointingHandCursor))
        self.config_default_bauds.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.config_default_bauds)

        self.horizontalSpacer_6 = QSpacerItem(745, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addWidget(self.fr_config_default_bauds)

        self.btn_start_max = QCheckBox(self.fr_config)
        self.btn_start_max.setObjectName(u"btn_start_max")
        self.btn_start_max.setMaximumSize(QSize(150, 16777215))
        self.btn_start_max.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_max.setStyleSheet(u"border-radius: 25px;")

        self.verticalLayout_6.addWidget(self.btn_start_max)

        self.btn_auto_update = QCheckBox(self.fr_config)
        self.btn_auto_update.setObjectName(u"btn_auto_update")
        self.btn_auto_update.setMaximumSize(QSize(16777215, 16777215))
        self.btn_auto_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_auto_update.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_auto_update)

        self.btn_set_full_screen = QCheckBox(self.fr_config)
        self.btn_set_full_screen.setObjectName(u"btn_set_full_screen")
        self.btn_set_full_screen.setMaximumSize(QSize(16777215, 16777215))
        self.btn_set_full_screen.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_set_full_screen.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_set_full_screen)

        self.verticalSpacer_2 = QSpacerItem(20, 615, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addWidget(self.fr_config)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget{\n"
"	color:rgba(77, 235, 220, 0.8);\n"
"	background-color: rgba(20,21,22,255);\n"
"	border: 0px solid;\n"
"}\n"
"QGroupBox{\n"
"border: 1px solid rgba(255, 255, 255, 0.0);\n"
"color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_flight = QFrame(self.page_2)
        self.fr_flight.setObjectName(u"fr_flight")
        self.fr_flight.setStyleSheet(u"QVBoxLayout{\n"
"border: 0px solid;\n"
"}")
        self.fr_flight.setFrameShape(QFrame.NoFrame)
        self.fr_flight.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fr_flight)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.TelemetryGroup = QGroupBox(self.fr_flight)
        self.TelemetryGroup.setObjectName(u"TelemetryGroup")
        self.TelemetryGroup.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Arame Mono"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.TelemetryGroup.setFont(font3)
        self.TelemetryGroup.setStyleSheet(u"font: 9pt \"Arame Mono\";\n"
"")
        self.TelemetryGroup.setAlignment(Qt.AlignCenter)
        self.TelemetryGroup.setFlat(False)
        self.TelemetryGroup.setCheckable(False)
        self.TelemetryGroup.setChecked(False)
        self.verticalLayout_9 = QVBoxLayout(self.TelemetryGroup)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 2, 2)
        self.telemetry_graphs = QVBoxLayout()
        self.telemetry_graphs.setSpacing(0)
        self.telemetry_graphs.setObjectName(u"telemetry_graphs")
        self.telemetry_graphs.setSizeConstraint(QLayout.SetMaximumSize)
        self.telemetry_graphs.setContentsMargins(0, 9, 0, 0)

        self.verticalLayout_9.addLayout(self.telemetry_graphs)


        self.verticalLayout_8.addWidget(self.TelemetryGroup)


        self.verticalLayout.addWidget(self.fr_flight)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_5.addWidget(self.stackedWidget)

        self.stackedWidget.raise_()
        self.fr_menu.raise_()

        self.verticalLayout_5.addWidget(self.fr_content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 13))
        self.statusBar.setMaximumSize(QSize(16777215, 13))
        font4 = QFont()
        font4.setFamilies([u"Arame Mono"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        self.statusBar.setFont(font4)
        self.statusBar.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_togle_menu.setText("")
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lb_countdown.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lb_ping.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lb_state.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.btn_minimize.setText("")
        self.btn_normalize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.lb_Ports.setText(QCoreApplication.translate("MainWindow", u"PORT:", None))
        self.lb_Baudrate.setText(QCoreApplication.translate("MainWindow", u"BAUDRATE:", None))
        self.cb_bauds.setCurrentText("")
        self.btn_connect_serial.setText(QCoreApplication.translate("MainWindow", u"disconnected", None))
        self.btn_update_ports.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_togle_log.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_menu_1.setText(QCoreApplication.translate("MainWindow", u"TERMINAL", None))
        self.btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"FLIGHT", None))
        self.btn_menu_config.setText(QCoreApplication.translate("MainWindow", u"CONFIG", None))
        self.terminal.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arame Mono'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.terminal.setPlaceholderText("")
        self.terminal_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u">_", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"RELOAD", None))
#if QT_CONFIG(tooltip)
        self.btn_opn_logs.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_opn_logs.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_opn_logs.setText(QCoreApplication.translate("MainWindow", u"open saves ", None))
        self.config_default_bauds_label.setText(QCoreApplication.translate("MainWindow", u"Default Bauds:", None))
        self.config_default_bauds.setCurrentText("")
        self.config_default_bauds.setPlaceholderText("")
        self.btn_start_max.setText(QCoreApplication.translate("MainWindow", u"start maximized", None))
        self.btn_auto_update.setText(QCoreApplication.translate("MainWindow", u"UPDATE PORTS ON START", None))
        self.btn_set_full_screen.setText(QCoreApplication.translate("MainWindow", u"FULL SCREEN", None))
        self.TelemetryGroup.setTitle(QCoreApplication.translate("MainWindow", u"FLY TELEMETRY", None))
    # retranslateUi

