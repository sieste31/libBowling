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
        player.set(1, [10, 0])
        self.assertEqual(player.score(), 10, "CASE2")
        player.set(1, [5, 5])
        self.assertEqual(player.score(), 10, "CASE3")
        
        # 一レーン目をセットしてスコアが5になること
        player.set(1, [5, 0])
        self.assertEqual(player.score(), 5, "CASE4")
        player.set(1, [0, 5])
        self.assertEqual(player.score(), 5, "CASE5")
        
        # ストライクを取ったら次の２投を加算する
        player.set(1, [10, 0])
        player.set(2, [1, 0])
        self.assertEqual(player.score(), 12, "CASE6")

        player.set(1, [10, 0])
        player.set(2, [10, 0])
        player.set(3, [1, 0])
        self.assertEqual(player.score(), 33, "CASE7")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testScore']
    unittest.main()