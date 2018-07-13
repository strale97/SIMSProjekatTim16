'''
Created on Jul 13, 2018

@author: marko
'''
from PySide.QtGui import QWidget, QPushButton, QVBoxLayout

class MyWidget4(QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        super(MyWidget4, self).__init__()
        
        vbox = QVBoxLayout()
        
        btnPregledajIzvestaje = QPushButton("Pregledaj izvestaje")
        btnPrijaviKvar = QPushButton("Prijavi kvar")
        btnIzmeniCenu = QPushButton("Izmeni cenu")
        btnNapraviIzvestaj = QPushButton("Napravi izvestaj")
        
        vbox.addWidget(btnPregledajIzvestaje)
        vbox.addWidget(btnPrijaviKvar)
        vbox.addWidget(btnIzmeniCenu)
        vbox.addWidget(btnNapraviIzvestaj)
        
        self.setLayout(vbox)
        
        
        