'''
Created on Jul 13, 2018

@author: marko
'''
from PySide.QtGui import QWidget, QPushButton, QTextEdit, QVBoxLayout

class MyWidget3(QWidget):


    def __init__(self):
        super(MyWidget3, self).__init__()
        
        vbox = QVBoxLayout()
        
        btnIzaberiIzvestaj = QPushButton("Izaberi izvestaj")
        textEdit = QTextEdit()
        vbox.addWidget(btnIzaberiIzvestaj)
        vbox.addWidget(textEdit)
        
        self.setLayout(vbox)
        
        
            