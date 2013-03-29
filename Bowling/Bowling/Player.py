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
        for i, r in enumerate(self.ret):
            #ストライク判定
            if self._isStrike(i):
                s += self._next(i, BALL_1) + self._nextnext(i, BALL_1)
            s += r[0] + r[1]
        return s
    
    def _next(self, frame, ball):
        #１０フレーム目は特殊
        if frame == FRAME_10:
            #1投目の場合、２投目をさす
            if ball == BALL_1:
                return self.ret[frame][BALL_2]
            #２投目の場合、３投目を指す
            elif ball == BALL_2:
                return self.ret[frame][BALL_3]
            #３投目の場合、0を返す
            else:
                return 0
        # １０フレーム目以外
        else:
            #１投目の場合、ストライクの場合は次のフレームを返し、
            # ストライクでなければ２投目を指す
            if ball == BALL_1:
                if self.ret[frame][ball] == STRIKE:
                    return self.ret[frame+1][BALL_1]
                else:
                    return self.ret[frame][BALL_2]
            # ２投目の場合、次のフレームの１投目をさす
            elif ball == BALL_2:
                return self.ret[frame+1][BALL_1]
            # それ以外（不正パス）は0を返す
            else:
                return 0
            
    def _nextnext(self, frame, ball):
        #10フレーム目は特殊
        if frame == FRAME_10:
            #１投目の場合、３投目をさす
            if ball == BALL_1:
                return self.ret[frame][BALL_3]
            #２投目、３投目は0を返す
            else:
                return 0
        #10フレーム目以外の場合
        else:
            #１投目の場合、ストライクの場合は次のフレームの次の投球を返す
            if ball == BALL_1:
                if self.ret[frame][BALL_1] == STRIKE:
                    return self._next(frame+1, BALL_1)
                else:
                    return self._next(frame, BALL_2)
            #２投目の場合、次のフレーム１投目の次の投球をさす
            elif ball == BALL_2:
                return self.next(frame+1, BALL_1)
            else:
                return 0
            
    #指定のフレームがストライクか調べる
    def _isStrike(self, frame):
        if self.ret[frame][0] == STRIKE:
            return True
        else:
            return False
    
    #指定のフレームがスペアか調べる
    def _isSpare(self, frame):
        #総和が10の場合
        if self._sumFrame(frame) == STRIKE:
            #最大値が10の場合
            if max(self.ret[frame]) == STRIKE:
                return False
            else:
                return True
        else:
            return False
            

    def _sumFrame(self, frame):
        return sum(self.ret[frame])
            
    def set(self, lane, ret):
        self.ret[lane-1] = ret