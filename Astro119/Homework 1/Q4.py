# -*- coding: utf-8 -*-

"""



"""

import math



initial  = 10
time   = 10
halfLife = .1

def N(N0, T, tao, H, verbose = False):
    amount = N0
    H = 1000
    for i in range (H):
        decay = N0*math.e**(-T/tao)
        amount += decay
        if verbose == True:
            print('year:', i)
    return amount

