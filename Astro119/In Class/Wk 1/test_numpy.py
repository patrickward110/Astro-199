# -*- coding: utf-8 -*-

"""

script that tests numpy fuctionality

"""

import numpy

N = 10 #number of elements in vector
start = 1
stop = 10 #Stopping number -1
step = 1

aV = numpy.arange(start, stop+1, step)
print(aV)

aV2 = numpy.linspace(start, stop, N, dtype=int)
print (aV2)


