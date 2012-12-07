from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL, QDir, pyqtSignal, QThread, Qt
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
            time.sleep(0.06)
        self.procDone.emit(True)


class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Assassins()
        self.ui.setupUi(self)
        #Progress bar
        self.thread = SleepProgress()
        self.thread.partDone.connect(self.what)
        self.thread.procDone.connect(self.koniec)
        #On startup
        self.ui.pytanieEdit.setFocus()
        #Fast quit
        exitAction = QtGui.QAction(self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        self.addAction(exitAction)
        #Button connecion
        QObject.connect(self.ui.WybierzButton, SIGNAL('clicked()'), self.wybierz)
        QObject.connect(self.ui.StartButton, SIGNAL('clicked()'), self.start)
    def wybierz(self):
        directory = QFileDialog.getOpenFileName(self, QDir.currentPath(), QDir.currentPath())
        if directory:
            self.ui.SciezkaLine.setText(directory)
    def start(self):
        self.presup = True
        self.ui.OdpowiedzLine.setText("")
        self.ui.WnioskowanietextBrowser.setText("")
        self.ui.progressBar.setValue(0)
        pytanie = self.ui.pytanieEdit.text()
        plik = self.ui.SciezkaLine.text()
        open("temp", "w").close() #czyszczyciel pliku
        if pytanie and plik:
            self.thread.start()
            que = Question(pytanie)
            with open(plik) as p:
                textes = p.read().split("\n")
            #textes = open(plik).read().split("\n")
            odmiany_miasta = odmiany_synonimow([que.city])
            odmiany_nazwisk = odmiany_synonimow([que.name])
            for tekst in textes:
                presup_nr = potw_presup(que.name, odmiany_miasta, tekst)
                czas = znajdz_czas(podaj_zdania(tekst))
                if presup_nr > 2:
                    probably_killa = bloody_shot(czas, odmiany_nazwisk, odmiany_miasta)
                    try:
                        killa = whos_da_killa(probably_killa, czas, odmiany_nazwisk, odmiany_miasta)
                        if not killa: continue
                    except IndexError:
                        continue
                    if que.name[-1]!='a': self.ui.OdpowiedzLine.setText("%s został zabity przez %s w %s" % (que.name, killa, que.city))
                    else: self.ui.OdpowiedzLine.setText("%s została zabita przez %s w %s" % (que.name, killa, que.city))
                    break
            else:
                self.presup = False
                QMessageBox.critical(self, "Problem", "Nie można na podstawie podanych tekstów odpowiedzieć na to pytanie!!", QMessageBox.Ok)
            self.ui.WnioskowanietextBrowser.setText(open("temp").read().replace("\\", ''))
        else:
            QMessageBox.critical(self, "Error", "Nie napisałeś pytania lub nie wybrałeś pliku!!", QMessageBox.Ok)
    def what(self, value):
        self.ui.progressBar.setValue(value)
    def koniec(self):
        while self.presup:
            if self.ui.OdpowiedzLine.text() != "": break
        else: self.ui.progressBar.setValue(0)
        if self.presup: self.ui.progressBar.setValue(100)
        
