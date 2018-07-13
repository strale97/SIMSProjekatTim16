'''
Created on Jul 13, 2018

@author: marko
'''

class User(object):
    '''
    classdocs
    '''


    def __init__(self, username, password, role):
        '''
        Constructor
        '''
        self.username = username
        self.password = password
        self.role = role
    
        