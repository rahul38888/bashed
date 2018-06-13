'''
Created on 12-Jun-2018

@author: rahul.s
'''

import os
import sys

print "Before - " + os.getcwd()

if sys.argv.__len__() is 1:
    os.chdir(os.getenv('HOME'))
elif not os.access(sys.argv[1],os.F_OK):
        print sys.argv[1]+" : " + os.strerror(2)
elif not os.path.isdir(sys.argv[1]):
    print sys.argv[1]+" : Not a directory"
elif not os.access(sys.argv[1],os.R_OK):
    print sys.argv[1]+" : " + os.strerror(1)
else:
    os.chdir(sys.argv[1])

print "After - "+os.getcwd()
