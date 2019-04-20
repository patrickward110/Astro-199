# -*- coding: utf-8 -*-

"""

Q1: Earthquake rates, earthquake and well locations in map-view 

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap


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
#print rate

#====================================================
#         c) Determine earthquake rate
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


length = np.ones((len(rate)))
cSum = np.cumsum( (length))



fig1 = plt.figure(1)
ax1  = plt.subplot(211)
ax1.hist(rate, bins = int((YRspan)*12))
#ax1.setx_label('time')

ax2  = plt.subplot(212)
ax2  = plt.plot(rate, cSum)
#ax2.setx_label('time')




#====================================================
#         d) Plot active wells and earthquakes within Dt = 6 months
#====================================================


xmin, xmax  = -93, -104
ymin, ymax  = 32, 39

#print xmin, xmax
#print ymin, ymax

aYr = toYears(YR, MO, 0, 0, 0, 0)




aYr  = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (1), dtype = float).T
mLoc = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (7, 8), dtype = float).T
mLoc = np.genfromtxt( seism, skip_header = 1, 
                       usecols = (7, 8, 10), dtype = float).T
                     
sort_id = aYr.argsort()
aYr = aYr[sort_id]
mLoc= mLoc.T[sort_id].T



for it in np.unique( aYr):
    #if (rate[it]-rate[it-1]>.4):
    
    sel_eq = it == aYr
    print( 'Year', it, '#Number of Events: ', sel_eq.sum())
    plt.figure( 3)
    plt.cla()
    plt.title( str( it))
    lon_0, lat_0 = .5*( xmin + xmax), .5*( ymin + ymax)

    m = Basemap(projection = 'cyl',
                llcrnrlon = xmin, urcrnrlon=xmax,
                llcrnrlat = ymin, urcrnrlat=ymax,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawcoastlines()
    m.drawstates(linewidth=0.5)

    aX_eq, aY_eq = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])

    plot1 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))

    cbar  = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_label( 'Magnitude')

    #plt.savefig(  file_out, dpi = 150)

    plt.pause( .05)
    #plt.show()
    plt.clf()












