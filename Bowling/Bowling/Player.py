# -*- coding: utf-8 -*-
'''
Created on 2013/03/30

@author: yusuke
'''

class Player(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.reset()

    def reset(self):
        self.ret = [[0, 0],     # 1レーン
                    [0, 0],     # 2レーン
                    [0, 0],     # 3レーン
                    [0, 0],     # 4レーン
                    [0, 0],     # 5レーン
                    [0, 0],     # 6レーン
                    [0, 0],     # 7レーン
                    [0, 0],     # 8レーン
                    [0, 0],     # 9レーン
                    [0, 0, 0] ] # 10レーン        
    
    def score(self):
        s = 0;
        for r in self.ret:
            s += r[0] + r[1]
        return s
    
    def set(self, lane, ret):
        self.ret[lane-1] = ret