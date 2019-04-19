# -*- coding: utf-8 -*-

"""
while loop, find max height

"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g  = 9.81
n  = 2000 # total time steps, just has to be high enough
#time
a_t = np.linspace(0,1,n)

#computation
y   = v0*a_t - 0.5*g*a_t**2

# find max height in while loop
i = 1
## side note y[-1] last entry in array
while y[i] > y [i-1]:
    largest_height = y[i]
    i += 1
    
print ('max height:%10.2f'%(largest_height))

plt.plot(a_t, y)
plt.show()

## USEFULLL use "%matplotlib auto" in console to get interactive plot