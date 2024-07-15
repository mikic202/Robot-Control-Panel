# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RobotData.ui',
# licensing of 'RobotData.ui' applies.
#
# Created: Mon Jul 15 13:56:12 2024
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_RobotDataWindow(object):
    def setupUi(self, RobotDataWindow):
        RobotDataWindow.setObjectName("RobotDataWindow")
        RobotDataWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RobotDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.sensor_output = QtWidgets.QLabel(self.centralwidget)
        self.sensor_output.setObjectName("sensor_output")
        self.verticalLayout.addWidget(self.sensor_output)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.stearing = QtWidgets.QLabel(self.centralwidget)
        self.stearing.setObjectName("stearing")
        self.verticalLayout.addWidget(self.stearing)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        RobotDataWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RobotDataWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        RobotDataWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RobotDataWindow)
        self.statusbar.setObjectName("statusbar")
        RobotDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RobotDataWindow)
        QtCore.QMetaObject.connectSlotsByName(RobotDataWindow)
