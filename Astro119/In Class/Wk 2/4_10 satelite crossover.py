# -*- coding: utf-8 -*-

"""

Satelite crossover between two functions
    as for loop then as vectorized

"""
import numpy as np
import matplotlib.pyplot as plt

#===========================================
    #Parameters
#===========================================

tmin, tmax = -10, 10
iN         = 1000
dt         = float(tmax-tmin)/iN

t0 = 2.5
c  = 1.1
A  = 9
eps= 0.1


#===========================================
    #Function definition
#===========================================

def ft(t, c, t0):
    return c*(t-t0)**2

def gt(t, A):
    return A*t+t0


#===========================================
    #Find crossover point
#===========================================
    
##A## for loop 
    
curr_t = tmin
for i in range(iN-1):
    curr_t += dt
    curr_ft = ft (curr_t, c, t0)
    curr_gt = gt (curr_t, A)
    if abs(curr_ft-curr_gt) < eps:
        print ('Crossover point at t=%.2f, f(t) = %.2f, g(t) = %.2f'%(curr_t, curr_ft, curr_gt))
        
        
##B## Vectorized solution
a_t = np.linspace(tmin, tmax, iN)
    #evaluate functions
a_ft = ft (a_t, c, t0)
a_gt = gt(a_t, A)
    #find crossover
sel = abs (a_ft - a_gt) < eps
print 'crossover points' , a_t[sel], a_ft[sel], a_gt[sel], abs(a_ft[sel]-a_gt[sel])

#===========================================
    #Plots
#===========================================
    # use %matplotlib auto in console
    
plt.plot(a_t, a_ft, 'ro', ms = 2)
plt.plot(a_t, a_gt, 'bo', ms = 2)