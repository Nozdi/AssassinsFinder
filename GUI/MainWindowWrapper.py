from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL, QDir, pyqtSignal, QThread
from .MainWindow import Ui_Assassins
from finder.question import Question
from finder.finder import *

import time

class SleepProgress(QThread):
    procDone = pyqtSignal(bool)
    partDone = pyqtSignal(int)
    
    def run(self):
        for a in range(1, 40+1):
            self.partDone.emit(float(a)/40.0*99)
            time.sleep(0.03)
        self.procDone.emit(True)


class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Assassins()
        self.ui.setupUi(self)
        self.thread = SleepProgress()
        self.thread.partDone.connect(self.what)
        self.thread.procDone.connect(self.koniec)
        self.presup = True
        QObject.connect(self.ui.WybierzButton, SIGNAL('clicked()'), self.wybierz)
        QObject.connect(self.ui.StartButton, SIGNAL('clicked()'), self.start)
    def wybierz(self):
        directory = QFileDialog.getOpenFileName(self, QDir.currentPath(), QDir.currentPath())
        if directory:
            self.ui.SciezkaLine.setText(directory)
    def start(self):
        self.presup = True
        self.ui.OdpowiedzLine.setText("")
        self.ui.progressBar.setValue(0)
        pytanie = self.ui.pytanieEdit.text()
        plik = self.ui.SciezkaLine.text()
        if pytanie and plik:
            self.thread.start()
            que = Question(pytanie)
            textes = open(plik).read().split("\n")
            for tekst in textes:
                czas = znajdz_czas(podaj_zdania(tekst))
                presup_nr = potw_presup(que.name, que.city, czas)
                if presup_nr>2:
                    odmiany_nazwisk = odmiany_synonimow([que.name])
                    odmiany_miasta = odmiany_synonimow([que.city])
                    probably_killa = bloody_shot(czas, odmiany_nazwisk, odmiany_miasta)
                    killa = whos_da_killa(probably_killa, czas)
                    if presup_nr == 3: self.ui.OdpowiedzLine.setText("%s został zabity przez %s w %s" % (que.name, killa, que.city))
                    elif presup_nr == 2: self.ui.OdpowiedzLine.setText("%s został zabity przez %s w ?%s?" % (que.name, killa, que.city))
                    break;
                    #else: self.ui.OdpowiedzLine.setText("?%s? został zabity przez %s w %s" % (que.name, killa, que.city))
                    self.ui.progressBar.setValue(100)
            else:
                self.presup = False
                QMessageBox.critical(self, "Problem", "Presupozycja nie może zostać potwierdzona!!", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error", "Nie napisałeś pytania lub nie wybrałeś pliku!!", QMessageBox.Ok)
        #self.ui.OdpowiedzLine.setText("Zginał pan %s w %s"%(que.name, que.city))
    def what(self, value):
        self.ui.progressBar.setValue(value)
    def koniec(self):
        while self.presup:
            if self.ui.OdpowiedzLine.text() != "": break
        else: self.ui.progressBar.setValue(0)
        if self.presup: self.ui.progressBar.setValue(100)
        
