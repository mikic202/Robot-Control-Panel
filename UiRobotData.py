# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RobotData.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.ReadingsNumber = QtWidgets.QSpinBox(self.centralwidget)
        self.ReadingsNumber.setObjectName("ReadingsNumber")
        self.verticalLayout_2.addWidget(self.ReadingsNumber)
        self.readings_checkbox = QtWidgets.QVBoxLayout()
        self.readings_checkbox.setObjectName("readings_checkbox")
        self.verticalLayout_2.addLayout(self.readings_checkbox)
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

    def retranslateUi(self, RobotDataWindow):
        _translate = QtCore.QCoreApplication.translate
        RobotDataWindow.setWindowTitle(_translate("RobotDataWindow", "MainWindow"))
        self.label.setText(_translate("RobotDataWindow", "Wejścia"))
        self.sensor_output.setText(_translate("RobotDataWindow", "TextLabel"))
        self.label_4.setText(_translate("RobotDataWindow", "Sterowanie"))
        self.stearing.setText(_translate("RobotDataWindow", "TextLabel"))
