'''
Created on 12-Jun-2018

@author: rahul.s
'''

class bashutil:
    def init_history(self,histFilePath):
        history=[]
        with open(histFilePath, 'r') as f:
            for line in f:
                history.append(line)

        return history
    
    def write_history(self,histFilePath,historyArray):
        for line in historyArray:
            with open(histFilePath,'a') as f:
                f.write(line)
        