# -*- coding: utf-8 -*-

"""

Q1: Earthquake rates, earthquake and well locations in map-view 

"""

import numpy as np
import matplotlib.pyplot as plt

#====================================================
#         a) Import data
#====================================================

injWell = 'injWell_OK.txt'
seism= 'seism_OK.txt'

injData = np.loadtxt(injWell).T
seiData = np.loadtxt(seism).T

#====================================================
#         b) Convert the date-time columns to decimal years
#====================================================

def toYears(YR, MO, DY, HR, MN, SC):
    
    DecYear = YR + (MO-1)/12 + (DY-1)/365.25 
    + HR/(365.25) + MN/(365.25*24*60)+ SC/(365.25*24*3600)
    
    return DecYear

YR    = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (1), dtype = float)
MO    = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (2), dtype = float)
DY    = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (3), dtype = float)
HR    = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (4), dtype = float)
MN    = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (5), dtype = float)
SC    = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (6), dtype = float)


rate = (toYears(YR, MO, DY, HR, MN, SC))
print rate

#====================================================
#         C) Determine earthquake rate
#====================================================

# number of earthquakes
events = len(YR)

YR1   = toYears(YR[0],  MO[0],  DY[0],  HR[0],  MN[0],  SC[0])
YRlst = toYears(YR[-1], MO[-1], DY[-1], HR[-1], MN[-1], SC[-1])

# time span of data (42.20893223819303 years)
YRspan = YRlst-YR1

# rate = events/time
rateMO = events/(YRspan*12)

print 'Average Rate per Month:', rateMO




#x = np.cumsum( np.ones(rate))
#print x



plt.hist(rate, bins = int((YRspan)*12))
plt.show()





















