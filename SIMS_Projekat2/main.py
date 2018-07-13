'''
Created on Jul 12, 2018

@author: marko
'''
import sys

from PySide import QtGui, QtCore 
from PySide.QtCore import QFile
from PySide.QtGui import QApplication, QMainWindow, QDialog

from loginWindow import LoginDialog
from NaplatnoMestoWindow import NaplatnoMestoWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not QFile(".\\users.cfg").exists():
        newfile = open(".\\users.cfg", "wb")
        newfile.close()
    
    login = LoginDialog()
    
    if login.exec_() == QDialog.Accepted:
        app.currentUser = login.getUser()
    else:
        sys.exit()
      
    app.mainWindow = NaplatnoMestoWindow()
    app.mainWindow.show()
    
    sys.exit(app.exec_())
    