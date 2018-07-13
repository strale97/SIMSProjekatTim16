'''
Created on Jul 13, 2018

@author: marko
'''
from PySide.QtGui import QWidget, QGridLayout, QHBoxLayout, QPushButton, \
    QVBoxLayout, QGroupBox


class MyWidget2(QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MyWidget2, self).__init__()
        self.resize(100, 100)
        
        
        mainLayout = QVBoxLayout()
        
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        
        korisnik = QGroupBox()
        btnRegistracijaKorsnika = QPushButton("Registracija korisnika")
        btnBrisanjeKorisnika = QPushButton("Brisanje korisnika")
        btnIzmenaKorisnika = QPushButton("Izmena korisnika")
        hbox1.addWidget(btnRegistracijaKorsnika)
        hbox1.addWidget(btnBrisanjeKorisnika)
        hbox1.addWidget(btnIzmenaKorisnika)
        korisnik.setLayout(hbox1)
        
        deonica = QGroupBox()
        btnDodavanjeDeonice = QPushButton("Dodavanje deonice")
        btnBrisanjeDeonice = QPushButton("Brisanje deonice")
        btnIzmenaDeonice = QPushButton("Izmena deonice")
        hbox2.addWidget(btnDodavanjeDeonice)
        hbox2.addWidget(btnBrisanjeDeonice)
        hbox2.addWidget(btnIzmenaDeonice)
        deonica.setLayout(hbox2)
        
        naplatnoMesto = QGroupBox()
        btnDodavanjeNapatnogMesta = QPushButton("Dodavanje naplatnog mesta")
        btnBrisanjeNaplatnihMesta = QPushButton("Brisanje naplatnog mesta")
        btnIzmenaNaplatnihMesta = QPushButton("Izmena naplatnog mesta")
        hbox3.addWidget(btnDodavanjeNapatnogMesta)
        hbox3.addWidget(btnBrisanjeNaplatnihMesta)
        hbox3.addWidget(btnIzmenaNaplatnihMesta)
        naplatnoMesto.setLayout(hbox3)
        
        mainLayout.addWidget(korisnik)
        mainLayout.addWidget(deonica)
        mainLayout.addWidget(naplatnoMesto)
        
        self.setLayout(mainLayout)
        