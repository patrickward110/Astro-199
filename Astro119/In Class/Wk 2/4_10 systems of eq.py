# -*- coding: utf-8 -*-

"""



"""


import numpy as np

## coeficient matrix , A

mA = np.array([[3,1],
               [1,2]])

#solution vector
a_b = np.array([9,8])

#solove for A-1 dot B

a_x = np.dot(np.linalg.inv(mA), a_b)
print(a_x)


#using .solve
a_x2 = np.linalg.solve(mA, a_b)
print(a_x2)

