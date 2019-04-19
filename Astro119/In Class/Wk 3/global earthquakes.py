# -*- coding: utf-8 -*-

"""

animation of global earthquakes locatiopns from 2000-2019
plotted annually

"""
import numpy as np
import matplotlib as plt
from mlp_toolkit.basemat import Basemap as Basemap


#===================================================
#                   files and parameters
#===================================================
file_eq = 'globalEqs.txt'



#===================================================
#                   load data
#===================================================
#                                   
aYr    = np.genfromtxt( file_eq, skip_header = 1, 
                       usecols = (0), delimiter = '-', dtype = int)
print (np.unique(aYr))

mLoc   = np.genfromtxt( file_eq, skip_header = 1, 
                       usecols = (2,1), delimiter = '-', dtype = float).T


#===================================================
#                   plot eq map using basemap
#===================================================
for it in np.unique(aYr):
    sel_eq = it == aYr
    print( ' no of eq in %i: %i' %(it, sel_eq.sum()))
    
    
    plt.figure(1)
    plt.title(str(it))
    
    m = Basemap()
    m.drawcoastlines()

    a_x, a_y = m(mLoc[0], mLoc[1])


    plt.plot (a_x, a_y, 'ro', ms = 5, mew = 1.5, mfc = 'none')
    
    plt.pause(.5)
    #plt.clf()


















