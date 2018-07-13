'''
Created on Jul 13, 2018

@author: marko
'''
from tkinter import Grid

from PySide.QtCore import Qt
from PySide.QtGui import QWidget, QLabel, QGridLayout, QComboBox, QRadioButton, \
    QIcon, QGroupBox, QHBoxLayout, QLineEdit, QPushButton
from pysideuic.Compiler.qtproxies import QtCore

from Deonice import Deonice


class MyWidget1(QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MyWidget1, self).__init__()
        gridlayout = QGridLayout()
        
        label1 = QLabel("KATEGORIJA")
        label2 = QLabel("DEONICA")
        label3 = QLabel("VALUTA")
        
        
        kategorija = QGroupBox()
        hbox = QHBoxLayout()
        
        iakat = QRadioButton("Ia")
        iakat.setChecked(True)
        #lakat.setIcon(QIcon("lakat.png"))
        ikat = QRadioButton("I")
        iikat = QRadioButton("II")
        iiikat = QRadioButton("III")
        ivkat = QRadioButton("IV")
        hbox.addWidget(iakat)
        hbox.addWidget(ikat)
        hbox.addWidget(iikat)
        hbox.addWidget(iiikat)
        hbox.addWidget(ivkat)
        kategorija.setLayout(hbox)
        
        deonica = QComboBox()
        deonica.setEditable(False)
        
        deonica.addItems(Deonice().listaDeonica)
        
        
        valuta = QGroupBox()
        hbox1 = QHBoxLayout()
        eur = QRadioButton("EUR")
        rsd = QRadioButton("RSD")
        rsd.setChecked(True)
        cenaRsd = QLineEdit()
        cenaRsd.setReadOnly(True)
        cenaEur = QLineEdit()
        cenaEur.setReadOnly(True)
        hbox1.addWidget(rsd)
        hbox1.addWidget(cenaRsd)
        hbox1.addWidget(eur)
        hbox1.addWidget(cenaEur)
        valuta.setLayout(hbox1)
        
        btnNaplati = QPushButton("\nNAPLATI\n")
        btnNaplati.clicked.connect(self.naplatiAction)

        btnPodigni = QPushButton("\nPODIGNI RAMPU\n")
        btnPodigni.clicked.connect(self.podigniAction)
    
        btnSpusti = QPushButton("\nSPUSTI RAMPU\n")
        btnSpusti.clicked.connect(self.spustiAction)
        
        
        gridlayout.addWidget(label1, 0, 0, 2, 3, int(Qt.AlignCenter))
        gridlayout.addWidget(label2, 2, 0, 2, 3, int(Qt.AlignCenter))
        gridlayout.addWidget(label3, 4, 0, 2, 3, int(Qt.AlignCenter))
        
        gridlayout.addWidget(kategorija, 0, 3, 2, 6)
        
        gridlayout.addWidget(deonica, 2, 3, 2, 6)
        
        gridlayout.addWidget(valuta, 4, 3, 2, 6)
        
        gridlayout.addWidget(btnNaplati, 6, 0, 2, 10)
        
        gridlayout.addWidget(btnPodigni, 8, 0, 2, 5)
        gridlayout.addWidget(btnSpusti, 8, 5, 2, 5)
        
        
        
        
        self.setLayout(gridlayout)
        
    def naplatiAction(self):
        print("Naplata izvrsena")
    
    def podigniAction(self):
        print("Rampa podignuta")
    
    def spustiAction(self):
        print("Rampa spustena")
        