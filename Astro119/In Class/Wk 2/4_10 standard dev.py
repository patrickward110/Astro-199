# -*- coding: utf-8 -*-

"""

create well pressure in time series
compute mean in each well
compute standard dev

"""
import numpy as np
import matplotlib.pyplot as plt


#===========================================
    #Parameters
#===========================================
    
iWell = 10
iMeas  = 12

#===========================================
    #create synthetic data
#===========================================
    
a_mu_syn = np.random.random_integers(20, 40, iWell)
a_std_syn = np.random.random_integers (1, 10, iWell)*.1
m_Data = np.array([])
for i in range (iWell):
    if i ==0:
        m_Data = a_mu_syn[i] + a_std_syn[i]*np.random.randn(iMeas)
    else:
        m_Data = np.vstack ( ( m_Data, a_mu_syn[i] + a_std_syn[i]*np.random.rand(iMeas)))
        
#===========================================
    #statistics
#===========================================
    
a_mean = np.dot(m_Data, np.ones( iMeas, dtype = float).reshape(iMeas, 1)
#test code performance
print('syn results', np.round(a_mu_syn, 2))
print('computed meas', np.round(a_mean.flatten(), 2))
