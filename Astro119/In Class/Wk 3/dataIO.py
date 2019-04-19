# -*- coding: utf-8 -*-

import numpy as np
import os
#======================================================
#                       Create Data
#======================================================
file_out = 'dataIO.txt'


N = 10
aX = np.arange(N)
aY = aX**2




#======================================================
#                methods to load and save data
#======================================================

# shows where it's saving
print(os.getcwd())

#                                               4 spaces
np.savetxt(file_out, np.array([aX, aY]).T, fmt = ' %4.0f%4.0f ' ,
           header = 'x, x^2')

mData = np.loadtxt(file_out).T
print mData

# read file line by line
with open(file_out, 'r') as file_obj:
    #ignore first line
    file_obj.next()
    
    for line in file_obj:
        lStr = line.split(' ')
        print(lStr)
        #for my_str in lStr:
            #print(int(float(my_str)))
            
            
#read and writwe binary data
import scipy.io
scipy.io.savemat(file_out.replace('txt', 'mat'), 
                 {'x' :aX, 'y' : aY}, do_compression = True)

dicData = scipy.io.loadmat(file_out.replace('txt', 'mat'))

print(dicData['x'])
print(dicData['y'])