from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL, QDir
from .MainWindow import Ui_Assassins
from finder.question import Question
from finder.finder import *

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Assassins()
        self.ui.setupUi(self)
        QObject.connect(self.ui.WybierzButton, SIGNAL('clicked()'), self.wybierz)
        QObject.connect(self.ui.StartButton, SIGNAL('clicked()'), self.start)
    def wybierz(self):
        directory = QFileDialog.getOpenFileName(self, QDir.currentPath(), QDir.currentPath())
        if directory:
            self.ui.SciezkaLine.setText(directory)
    def start(self):
        progess = 0
        pytanie = self.ui.pytanieEdit.text()
        que = Question(pytanie)
        plik = self.ui.SciezkaLine.text()
        self.ui.progressBar.setValue(10)
        if pytanie and plik:
            tekst = podaj_zdania(open(plik).read())
            self.ui.progressBar.setValue(24)
            if potw_presup(que.name, que.city, tekst):
                czas = znajdz_czas(tekst)
                self.ui.progressBar.setValue(34)
                odmiany_nazwisk = odmiany_synonimow([que.name])
                self.ui.progressBar.setVaule(43)
                odmiany_miasta = odmiany_synonimow([que.city])
                self.ui.progress.setValue(66)
                probably_killa = bloody_shot(czas, odmiany_nazwisk, odmiany_miasta)
                self.ui.progress.setValue(99)
                self.ui.OdpowiedzLine.setText("%s został zabity przez %s w %s" % (que.name, whos_da_killa(probably_killa), que.city))
                self.ui.progressBar.setValue(0)
            else:
                QMessageBox.critical(self, "Problem", "Presupozycja nie może zostać potwierdzona!!", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error", "Nie napisałeś pytania lub nie wybrałeś pliku!!", QMessageBox.Ok)
        #self.ui.OdpowiedzLine.setText("Zginał pan %s w %s"%(que.name, que.city))
