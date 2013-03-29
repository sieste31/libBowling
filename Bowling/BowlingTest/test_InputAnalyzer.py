# -*- coding: utf-8 -*-

'''
Created on 2013/03/29

@author: yusuke
'''

import unittest
import Bowling.Input
from StringIO import StringIO


class Test(unittest.TestCase):


    def setUp(self):
        self.infile = StringIO()
        self.input = ["10","1 9" ,"10","2 8","10","3 7","10","4 6","10","5 5 10"]


    def tearDown(self):
        self.infile.close()


    def testIsValid(self):
        # case1  行数 10行でなければならない
        for line in self.input:
            self.infile.write(line + "\n")
        self.infile.seek(0)
        analyzer = Bowling.Input.Analyzer(self.infile)
        self.assertTrue(analyzer.isValid(), "case1_line ")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInputAnalyze']
    unittest.main()