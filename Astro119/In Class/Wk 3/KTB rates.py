# -*- coding: utf-8 -*-

"""
google Matploltlib galaries for all sorts of graphs

compute temporal earthquake rate of change
 for KTB fluid injection experiment


"""
import numpy as np
import matplotlib as plt


#===================================================
#                   function def
#===================================================
def comp_rate(a_t, k):
    """
    compute rate change for time vector a_t
    :input 
        a_t   - timevector
        k     - sample wimdow - controlls smoothness
        
    :output a_bin, a_rate
    """
    
    aS     = np.arange(0, a_t.shape[0]-k, 1)
    a_bin  = np.zeros(aS.shape[0])
    a_rate = np.zeros(aS.shape[0])    
    iS     = 0
    
    for s_step in aS:
        i1, i2     = s_step, s_step+k
        a_rate[iS] = k/(a_t[i2] - a_t[i1])
        a_bin[iS]  = .5*(a_t[i1] +a_t[i2])
        
        iS += 1
    return a_bin, a_rate


#===================================================
#               parametres and files
#===================================================
file_inj = 'data/KTB_inject.txt'
file_eq = 'data/KTB_mag.txt'

#sample window
k_win   = 100

t0      = float() #starting time for plotting
aT_eq   = np.array([]) #timing of the earthquakes
aMag    = np.array([])

aT_imj  = np.array([])
aV      = np.array([])

#===================================================
#                   load data and 
#===================================================
mData = np.loadtxt(file_eq).T
aT_eq = mData[0]
aMag  = mData[1]

mData = np.loadtxt(file_inj).T
aT_inj= mData[0]
aV    = mData[1]

#select
sel   = aV > 0
aT_inj= aT_inj[sel]

#shift time vectors and change to hr
t0    = aT_inj[0]
aT_inj -= t0
aT_eq -= t0
aT_inj = aT_inj/3600
aT_eq = aT_eq/3600



#compute rq rates
a_tbin, a_rate = comp_rate(aT_eq, k_win)

#===================================================
#                   plots
#===================================================
"""
fig1 = plt.figure(1)
ax1  = plt.subplot(211)
ax1.plot(aT_inj, aV, 'b-')
ax1.set_ylabel( 'cumul inj rate')

ax2  = plt.subplot(212)
twinx2 = ax2.twinx()
ax2.plot(aT_eq, aMag, 'r-')
twinx2.plot (sorted(aT_eq), np.cumsum(np.ones)       aT_eq.shape0[])), 'g-'
ax2.setx_label('time')


ax2.ser_xlim(ax1.get_xlim())
plt.show()
"""

print aT_eq


































