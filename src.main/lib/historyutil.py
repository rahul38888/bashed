'''
Created on 12-Jun-2018

@author: rahul.s
'''
from lib.bashutil import bashutil

class historyutil:

    def __init__(self,histFilePath):
        self.histFilePath = histFilePath
        self.historyArray = bashutil.init_history(self.histFilePath)

    def reverse_search(self,patern):
        pass
    
    def add_to_history(self,command):
        self.historyArray.append(command)
    
    def save_to_history_file(self):
        bashutil.write_history(self,self.histFilePath,
                               self.historyArray)
        