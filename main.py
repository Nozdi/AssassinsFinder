#!/usr/bin/env python3.2

import sys
from PyQt4 import QtGui
from GUI.MainWindowWrapper import MainWindowWrapper

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindowWrapper()
    main_window.show()
    sys.exit(app.exec_())
    
