'''
Created on 2013/03/30

@author: yusuke
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testScore(self):
        # 最初の状況でスコアは0
        player = Bowling.Player()
        self.assertEqual(player.score(), 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testScore']
    unittest.main()