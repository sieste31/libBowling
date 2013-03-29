'''
Created on 2013/03/29

@author: yusuke
'''

class Analyzer():
    
    
    def __init__(self, f):
        self.lines = f.read().splitlines()
    
    def isValid(self):
        if len(self.lines) == 10:
            print self.lines
            return True
        else:
            print self.lines
            return False

    