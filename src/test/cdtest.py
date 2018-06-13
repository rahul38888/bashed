'''
Created on 12-Jun-2018

@author: rahul.s
'''
import unittest
import sys


class Test(unittest.TestCase):

    def testName(self):
        sys.argv = ['..']
        execfile("../../src.main/bin/cd.py")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()