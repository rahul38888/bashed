'''
Created on 12-Jun-2018

@author: rahul.s
'''
from lib.bashutil import bashutil

class historyutil:

    def __init__(self,histFilePath):
        self.historyArray = bashutil.init_history(histFilePath)

    def rev_search(self):
        pass