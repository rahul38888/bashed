'''
Created on 12-Jun-2018

@author: rahul.s
'''

import os

class bashutil:
    def init_history(self,histFilePath):
        f=os.open(histFilePath, os.O_RDONLY)
        fl=os.fdopen(f)

        history=[]
        for cmd in fl:
            history.append(cmd.rstrip())

        os.close(f)
        print history
        return history
        