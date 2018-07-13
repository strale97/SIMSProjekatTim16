'''
Created on Jul 13, 2018

@author: marko
'''
from PySide.QtGui import QMainWindow, QLabel, QRadioButton, \
    QGridLayout, QMessageBox, QWidget, QApplication

from MyWidget1 import MyWidget1
from MyWidget2 import MyWidget2
from MyWidget3 import MyWidget3
from MyWidget4 import MyWidget4


class NaplatnoMestoWindow(QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        
        super(NaplatnoMestoWindow, self).__init__()
        self.resize(800,600)

        user = QApplication.instance().currentUser
        
        if user.role == "Radnik na naplatnom mestu":
            widget = MyWidget1()
        elif user.role == "Admin":
            widget = MyWidget2()
        elif user.role == "Radnik u centrali":
            widget = MyWidget3()
        elif user.role == "Sef stanice":
            widget = MyWidget4()
            
        
        self.setCentralWidget(widget)
        
        
        
        
        
        
        
        
        
        
        