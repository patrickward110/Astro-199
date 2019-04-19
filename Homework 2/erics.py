# -*- coding: utf-8 -*-

"""
119 HW.2, problem one.
Importing data to create animated plots showing increase in seismic
activity
"""

# always import the good stuff =================================================
import numpy as np
import matplotlib.pyplot as plt

# importing data sets ==========================================================
Well_data = "injWell_OK.txt"
Seismic_data = "seism_OK.txt"
S_D = np.loadtxt(Seismic_data).T
W_D = np.loadtxt(Well_data).T

# converting to decimal years ==================================================
YR = S_D[1]
MO = S_D[2]
DY = S_D[3]
HR = S_D[4]
MN = S_D[5]
SC = S_D[6]
DecYear = YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25) + MN/(365.25*24*60)
+ SC/(365.25*24*3600)
print(DecYear)
#%matplotlib inline
plt.hist(DecYear, normed = True, bins = 1000)
plt.show()