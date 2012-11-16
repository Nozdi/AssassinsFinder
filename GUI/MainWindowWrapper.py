from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow, QFileDialog
from PyQt4.QtCore import QObject, SIGNAL, QDir
from .MainWindow import Ui_Assassins

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Assassins()
        self.ui.setupUi(self)
        QObject.connect(self.ui.WybierzButton, SIGNAL('clicked()'), self.wybierz)
    def wybierz(self):
        directory = QFileDialog.getOpenFileName(self, QDir.homePath(), QDir.homePath())
        if directory:
            self.ui.SciezkaLine.setText(directory)
