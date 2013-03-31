# -*- coding: utf-8 -*-
'''
Created on 2013/03/30

@author: yusuke
'''
import unittest
import Bowling.Player


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testScore(self):
        # 最初の状況でスコアは0
        player = Bowling.Player.Player()
        self.assertEqual(player.score(), 0, "CASE1")
        
        # 一レーン目をセットしてスコアが10になること
        player.set(Bowling.Player.FRAME_1, 10, 0)
        self.assertEqual(player.score(), 10, "CASE2")
        
        player.set(Bowling.Player.FRAME_1, 5, 5)
        self.assertEqual(player.score(), 10, "CASE3")
        
        # 一レーン目をセットしてスコアが5になること
        player.set(Bowling.Player.FRAME_1, 5, 0)
        self.assertEqual(player.score(), 5, "CASE4")
        player.set(Bowling.Player.FRAME_1, 0, 5)
        self.assertEqual(player.score(), 5, "CASE5")
        
        # ストライクを取ったら次の２投を加算する
        player.set(Bowling.Player.FRAME_1, 10, 0)
        player.set(Bowling.Player.FRAME_2, 1, 0)
        self.assertEqual(player.score(), 12, "CASE6")

        player.set(Bowling.Player.FRAME_1, 10, 0)
        player.set(Bowling.Player.FRAME_2, 10, 0)
        player.set(Bowling.Player.FRAME_3, 1, 0)
        self.assertEqual(player.score(), 33, "CASE7")

        player.set(Bowling.Player.FRAME_1, 10, 0)
        player.set(Bowling.Player.FRAME_2, 10, 0)
        player.set(Bowling.Player.FRAME_3, 10, 0)        
        player.set(Bowling.Player.FRAME_4, 10, 0)
        player.set(Bowling.Player.FRAME_5, 10, 0)
        player.set(Bowling.Player.FRAME_6, 10, 0)
        player.set(Bowling.Player.FRAME_7, 10, 0)
        player.set(Bowling.Player.FRAME_8, 10, 0)
        player.set(Bowling.Player.FRAME_9, 10, 0)
        player.set(Bowling.Player.FRAME_10, 10, 10, 10)
        self.assertEqual(player.score(), 300, "CASE8 =" +str(player.score()))
        
        #スペアの確認
        player.reset()
        player.set(Bowling.Player.FRAME_1, 5, 5)
        player.set(Bowling.Player.FRAME_2, 4, 0)
        player.set(Bowling.Player.FRAME_3, 1, 0)
        self.assertEqual(player.score(), 19, "CASE9")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testScore']
    unittest.main()