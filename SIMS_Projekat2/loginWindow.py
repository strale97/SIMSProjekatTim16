'''
Created on Jul 12, 2018

@author: marko
'''
from PySide.QtCore import Qt
from PySide.QtGui import QDialog, QFormLayout, QLineEdit, \
    QDialogButtonBox, QPushButton, QMessageBox, QPalette, QIcon, \
    QLabel, QPixmap, QComboBox
from pickle import UnpicklingError
import pickle
from User import User

class LoginDialog(QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(LoginDialog, self).__init__()
        formLayout = QFormLayout()
        
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)

        self.input3 = QLineEdit()
        self.input3.setEchoMode(QLineEdit.EchoMode.Password)    
        
        self.cb = QComboBox()
        self.cb.addItems(["Sef stanice", "Radnik u centrali", "Radnik na naplatnom mestu", "Admin"])
        
        palete = QPalette()
        palete.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palete)
        self.setWindowTitle("Login")
        self.resize(370, 100)
        
        label2 = QLabel("<font color='White'>Username</font>")
        label3 = QLabel("<font color='White'>Password</font>")
        label4 = QLabel("<font color='White'>Registration key</font>")
        label5 = QLabel("<font color='White'>Role</font>")
        
        formLayout.addRow(label2, self.input1)
        formLayout.addRow(label3, self.input2)
    
        
        btnOK = QPushButton("Login")
        btnOK.clicked.connect(self.loginAction)
        btnCancel = QPushButton("Cancel")
        btnCancel.clicked.connect(self.reject)
        btnRegister = QPushButton("Register")
        btnRegister.clicked.connect(self.registerAction)
        
        
        group = QDialogButtonBox()
        group.addButton(btnOK, QDialogButtonBox.AcceptRole)
        group.addButton(btnCancel, QDialogButtonBox.RejectRole)
        
        
        formLayout.addRow(group)
        formLayout.addRow(label4, self.input3)
        formLayout.addRow(label5, self.cb)
        formLayout.addWidget(btnRegister)
        
        self.result = None
        self.setLayout(formLayout)
        
    def loginAction(self):
        self.result = [self.input1.text(), self.input2.text()]
        users = []
        infile = open(".\\users.cfg", "rb")
        while True:
            try:
                user = pickle.load(infile)
                users.append(user)
            except (EOFError, UnpicklingError):
                break
        infile.close()
        for user in users:
            if user.username == self.result[0] and user.password == self.result[1]:
                self.setUser(user)
                self.accept()
                return
        message = QMessageBox()
        message.setText("Username or password is incorrect")
        message.exec_()
        
        
    def registerAction(self):
        '''
        Dodaje korisnika sa unetim imenom i lozinkom u listu postojecih korisnika.
        '''
        self.result = [self.input1.text(), self.input2.text()]
        if "" in self.result:
            message3 = QMessageBox()
            message3.setText("Incorrect input")
            message3.exec_()
        else:
            users = []
            infile = open(".\\users.cfg", "rb")
            while True:
                try:
                    user = pickle.load(infile)
                    users.append(user)
                except (EOFError, UnpicklingError):
                    break
            infile.close()
            indicator = False
            for user in users:
                if user.username == self.result[0]:
                    indicator = True;
            if indicator:
                message1 = QMessageBox()
                message1.setText("Username already exists")
                message1.exec_()
            else:
                if self.input3.text() == "admin":
                    user1 = User(self.result[0], self.result[1], self.cb.currentText())
                    users.append(user1)
                    message2 = QMessageBox()
                    message2.setText("The user was successfully created")
                    message2.exec_()
                else:
                    message3 = QMessageBox()
                    message3.setText("Registration code is incorrect")
                    message3.exec_()
            out = open(".\\users.cfg", "wb")
            for user in users:
                pickle.dump(user, out)
            out.close()
            
    def result(self):
        return self.result
    
    def setUser(self, user):
        self.user = user
        
    def getUser(self):
        return self.user
    
    
        