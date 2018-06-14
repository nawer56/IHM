# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_interface.ui'
#
# Created: Thu Jun 14 15:03:57 2018
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(945, 667)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ANALOG_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.ANALOG_checkbox.setObjectName(_fromUtf8("ANALOG_checkbox"))
        self.gridLayout_2.addWidget(self.ANALOG_checkbox, 3, 0, 1, 1)
        self.I2C_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.I2C_checkbox.setObjectName(_fromUtf8("I2C_checkbox"))
        self.gridLayout_2.addWidget(self.I2C_checkbox, 2, 0, 1, 1)
        self.SPI_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.SPI_checkbox.setObjectName(_fromUtf8("SPI_checkbox"))
        self.gridLayout_2.addWidget(self.SPI_checkbox, 4, 0, 1, 1)
        self.UART_checkbox = QtGui.QCheckBox(self.centralwidget)
        self.UART_checkbox.setObjectName(_fromUtf8("UART_checkbox"))
        self.gridLayout_2.addWidget(self.UART_checkbox, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.perso_button = QtGui.QPushButton(self.centralwidget)
        self.perso_button.setObjectName(_fromUtf8("perso_button"))
        self.gridLayout.addWidget(self.perso_button, 1, 0, 1, 1)
        self.input_text = QtGui.QTextBrowser(self.centralwidget)
        self.input_text.setObjectName(_fromUtf8("input_text"))
        self.gridLayout.addWidget(self.input_text, 0, 3, 1, 1)
        self.Compass = QwtCompass(self.centralwidget)
        self.Compass.setLineWidth(4)
        self.Compass.setObjectName(_fromUtf8("Compass"))
        self.gridLayout.addWidget(self.Compass, 2, 0, 1, 1)
        self.pota = QwtKnob(self.centralwidget)
        self.pota.setObjectName(_fromUtf8("pota"))
        self.gridLayout.addWidget(self.pota, 2, 1, 1, 1)
        self.RUN_button = QtGui.QPushButton(self.centralwidget)
        self.RUN_button.setObjectName(_fromUtf8("RUN_button"))
        self.gridLayout.addWidget(self.RUN_button, 1, 1, 1, 1)
        self.qwtPlot = QwtPlot(self.centralwidget)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.gridLayout.addWidget(self.qwtPlot, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QT interface", None))
        self.ANALOG_checkbox.setText(_translate("MainWindow", "ANALOG", None))
        self.I2C_checkbox.setText(_translate("MainWindow", "I2C", None))
        self.SPI_checkbox.setText(_translate("MainWindow", "SPI", None))
        self.UART_checkbox.setText(_translate("MainWindow", "UART", None))
        self.perso_button.setText(_translate("MainWindow", "PERSONNALISATION", None))
        self.RUN_button.setText(_translate("MainWindow", "OK", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from qwt_knob import QwtKnob
from qwt_plot import QwtPlot
from qwt_compass import QwtCompass
