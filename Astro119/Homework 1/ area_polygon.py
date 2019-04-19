# -*- coding: utf-8 -*-

"""
Question 2

Write a function to compute the area of a polygon with five vertices 
in Cartesian coordinates: (1,1); (3,1); (4,2); (3.5, 5); (2,4). 

A	=	½|(x1y2 +	x2y3 +	…	xn-1yn +	xny1)	- (y1x2 +	y2x3 +	…	+	yn-1xn +	ynx1)|

"""

## rectangle
#xi = [0, 0, 2, 2]
#yi = [2, 0, 0, 2]


## triangle
#xi = [0, 0, 2]
#yi = [2, 0, 0]


## Irregular polygon
xi = [1,  3, 4, 3.5,  2]
yi = [1,  1, 2, 5  ,  4]

arr = [ [1.,1.], [3.,1.], [4.,2.], [3.5, 5.], [2.,4.]]

points = len(xi)

term1 = 0
term2 = 0

"""
for i in range (1, points):
    

    term1i = xi[i-1]*yi[i] + xi[i]*yi[0]
    term1 = term1 + term1i
    
    term2i = yi[i-1]*xi[i] + yi[i]*xi[0]
    term2 = term2 + term2i

    
    A = 0.5* abs(term1 - term2)
    
    print A
   #print "Area of polygon:", A
"""
    
t1 = 0
def area(xn, yn, xn_1, yn_1):
    for i in range (points):
    
        xn   = xi[i]
        yn   = yi[i]   
       
    
    for i in range (1, points):

        xn_1 = xi[i-1]
        yn_1 = yi[i-1]
    
   # t1i = xn_1*yn + xn*yi[0] 
    #t1 += t1i
    
    
    
    print xn_1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    