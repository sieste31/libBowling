# -*- coding: utf-8 -*-
'''
Created on 2013/03/30

@author: yusuke
'''

FRAME_1 = 0
FRAME_2 = 1
FRAME_3 = 2
FRAME_4 = 3
FRAME_5 = 4
FRAME_6 = 5
FRAME_7 = 6
FRAME_8 = 7
FRAME_9 = 8
FRAME_10 = 9

BALL_1 = 0
BALL_2 = 1
BALL_3 = 2

STRIKE = 10

class Frame(object):
    def __init__(self, num, f, s, t):
        self.ball = [f, s, t]
        self.num = num
        
    def isStrike(self):
        if self.sum(1) == STRIKE:
            return True
        else:
            return False
        
    def isSpare(self):
        if not self.isStrike() and self.sum() == STRIKE:
            return True
        else:
            return False
        
    #num投目までの投球の合計
    def sum(self, num = 3):
        s = sum(self.ball[:num])
        return s
    
    def score(self, next_frame = None, nextnext_frame = None):
        s = 0
        #ストライクの場合,次のフレーム＋（次のフレームがストライクなら次の次の一投目）
        if self.isStrike() and next_frame is not None:
            if nextnext_frame is not None:
                s = next_frame.sum(2) + (nextnext_frame.sum(1) if next_frame.isStrike() else 0)
            else:
                s = next_frame.sum(2)

        #スペアの場合、次のフレームの一投目
        if self.isSpare():
            s = next_frame.sum(1)
        s += self.sum()
        return s

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
        self.frames = [Frame(FRAME_1, 0, 0, 0),
                       Frame(FRAME_2, 0, 0, 0),
                       Frame(FRAME_3, 0, 0, 0),
                       Frame(FRAME_4, 0, 0, 0),
                       Frame(FRAME_5, 0, 0, 0),
                       Frame(FRAME_6, 0, 0, 0),
                       Frame(FRAME_7, 0, 0, 0),
                       Frame(FRAME_8, 0, 0, 0),
                       Frame(FRAME_9, 0, 0, 0),
                       Frame(FRAME_10, 0, 0, 0),
                       ]
            
    def score(self):
        s = 0;
        length = len(self.frames)
        for i, frame in enumerate(self.frames):
            s += frame.score(self.frames[i+1] if i+1 < length else None,
                             self.frames[i+2] if i+2 < length else None)
        return s
            
    def set(self, frame, f, s = 0, t = 0):
        self.frames[frame].ball = [f, s, t]