# -*- coding: utf-8 -*-

'''
Created on April 15th, 2019


    - plot an animated map of global earthquake activity


@author: tgoebel
'''
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

#------------my modules-----------------------
#import data.seis_utils as seis_utils

#===================================================================================
#                         files, variables
#===================================================================================
eqFile      = 'seism_OK.txt'
xmin, xmax  = -93, -104
ymin, ymax  = 32, 39

print xmin, xmax
print ymin, ymax

#===================================================================================
#                         load data
#===================================================================================

aYr  = np.genfromtxt( eqFile, skip_header = 1, 
                       usecols = (1), dtype = float).T
mLoc = np.genfromtxt( eqFile, skip_header = 1, 
                       usecols = (7, 8), dtype = float).T
mLoc = np.genfromtxt( eqFile, skip_header = 1, 
                       usecols = (7, 8, 10), dtype = float).T
                     
sort_id = aYr.argsort()
aYr = aYr[sort_id]
mLoc= mLoc.T[sort_id].T

#===================================================================================
#                        basemap plotting
#===================================================================================
for it in np.unique( aYr):
    sel_eq = it == aYr
    print( 'current year', it, '#no. of events: ', sel_eq.sum())
    plt.figure( 1)
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
