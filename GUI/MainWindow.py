# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Nov 20 12:36:16 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Assassins(object):
    def setupUi(self, Assassins):
        Assassins.setObjectName(_fromUtf8("Assassins"))
        Assassins.resize(595, 206)
        Assassins.setMinimumSize(QtCore.QSize(595, 206))
        Assassins.setMaximumSize(QtCore.QSize(595, 206))
        self.centralwidget = QtGui.QWidget(Assassins)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 501, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.SciezkaLine = QtGui.QLineEdit(self.layoutWidget)
        self.SciezkaLine.setEnabled(False)
        self.SciezkaLine.setReadOnly(True)
        self.SciezkaLine.setObjectName(_fromUtf8("SciezkaLine"))
        self.horizontalLayout.addWidget(self.SciezkaLine)
        self.WybierzButton = QtGui.QPushButton(self.layoutWidget)
        self.WybierzButton.setObjectName(_fromUtf8("WybierzButton"))
        self.horizontalLayout.addWidget(self.WybierzButton)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 140, 501, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.OdpowiedzLine = QtGui.QLineEdit(self.layoutWidget1)
        self.OdpowiedzLine.setEnabled(True)
        self.OdpowiedzLine.setReadOnly(True)
        self.OdpowiedzLine.setObjectName(_fromUtf8("OdpowiedzLine"))
        self.horizontalLayout_2.addWidget(self.OdpowiedzLine)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 20, 501, 26))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.pytanieEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.pytanieEdit.setObjectName(_fromUtf8("pytanieEdit"))
        self.horizontalLayout_3.addWidget(self.pytanieEdit)
        self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 100, 501, 29))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.StartButton = QtGui.QPushButton(self.layoutWidget3)
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.horizontalLayout_6.addWidget(self.StartButton)
        self.progressBar = QtGui.QProgressBar(self.layoutWidget3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_6.addWidget(self.progressBar)
        Assassins.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Assassins)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Assassins.setStatusBar(self.statusbar)

        self.retranslateUi(Assassins)
        QtCore.QMetaObject.connectSlotsByName(Assassins)

    def retranslateUi(self, Assassins):
        Assassins.setWindowTitle(QtGui.QApplication.translate("Assassins", "Assassins Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Assassins", "Ścieżka do teksu:", None, QtGui.QApplication.UnicodeUTF8))
        self.WybierzButton.setText(QtGui.QApplication.translate("Assassins", "Wybierz....", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Assassins", "Odpowiedz:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Assassins", "Pytanie:", None, QtGui.QApplication.UnicodeUTF8))
        self.StartButton.setText(QtGui.QApplication.translate("Assassins", "Start", None, QtGui.QApplication.UnicodeUTF8))

