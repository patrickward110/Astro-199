# -*- coding: utf-8 -*-

"""

exoplanet transit

"""
import numpy as np
import matplotlib.pyplot as plt

#====================================================
#               File name and variables
#====================================================

file_in = 'exoplanet_transit.csv'

r_earth = 6378 
r_s = 80*1e3 #km
Np  = 3 


#====================================================
#                    Load data
#====================================================
#                           delimiter: data separated by commas 
#                                           .T: transpose
mData = np.loadtxt(file_in, delimiter = ',', skiprows = 1).T
N     = len(mData[0])
lenPer= int(float(N)/Np)
#compute difference between subsequent samples
aDiff = mData[1][1::] - mData[1][0:-1]


#====================================================
#                Compute depth of transit
#====================================================
aDepth = np.zeros(Np)
for i in range (Np):
    #create index vector
    aID = np.arange(lenPer) + lenPer*i
    selMin = aDiff[aID] == aDiff[aID].min()
    selMax = aDiff[aID] == aDiff[aID].max()
    
    iID_min = aID[selMin][0]
    iID_max = aID[selMax][0]

    # compute mean depth of transit for each period
    aDepth[i] = mData[1, iID_min:iID_max].mean()
    
#compute size of planet
aR_p = np.sqrt(aDepth)*r_s
print(aR_p)
print ('size relative to earth', aR_p/r_earth)

#====================================================
#                       Plotting
#====================================================

# %matplotlib auto
plt.figure(1)
#           2 rows, 1 columb
plt.subplot(211)
#                                   ms: marker size
plt.plot(mData[0], mData[1], 'ko', ms = 2)
plt.xlabel('Transit Time (hr)')
plt.ylabel('Brightness')

plt.subplot(212)
plt.plot(mData[0][0:-1], aDiff, 'ro', ms = 2)
plt.xlabel('Transit Time (hr)')
plt.ylabel('Brightness Difference')

plt.show()


























plt.show()