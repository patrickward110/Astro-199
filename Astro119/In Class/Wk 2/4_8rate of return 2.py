#!python2.7
"""
Write a script that computes the annual rate of return and the absolute return on an investment of $1,000 at 10% over 30 years
 - lessons in compounding interest

"""
#===================================================================================
#                                params
#===================================================================================
#getinput from user
f_iniInvest = float(raw_input('Initial investment:' ))
f_interest  = float(raw_input('Interest rate:' ))
f_income =    float(raw_input('Desired monthly income:' ))
i_Years    = 30
 
new_variable = 1

#===================================================================================
#                                calculation
#===================================================================================

def annual_savings( f_money0, f_int, N, verbose = False):
    """
    - compute annual return on toal savings - f_money0
    :input
        f_money0  - total savings in year 0
        f_int     - interest rate
        N         - total years
    :return float() - savings in year N
    """
    currSave = f_money0
    for i in range( N):
        growth    = currSave*.1
        currSave += growth
        if verbose == True:
            print( 'Year: %i, abs savings: %8.2f, rate of ini.: %4.3f'%( i+1, currSave, (growth)/f_int))
    return currSave

def retirement( f_money0, f_int, f_income, verbose = False):
    """
    - compute annual return on toal savings - f_money0
    :input
        f_money0  - total savings in year 0
        f_int     - interest rate
        f_income         - desired retirement earnings
    :return float() - savings in year N
    """
    
    N = 1000
    currSave = f_money0
    for i in range( N):
        growth    = currSave*.1
        currSave += growth
        if growth >= (f_income*12):
            retire_year = i
            break
    return retire_year


    #    if verbose == True:
    #       print( 'Year: %i, abs savings: %8.2f, rate of ini.: %4.3f'%( i+1, currSave, (growth)/f_int))
    #return retire_year


totSav1 = annual_savings( f_iniInvest, f_interest, i_Years, verbose = True)

# here is the easier formila to get total savings in year n
totSav2 = (1 + f_interest)**i_Years*f_iniInvest
print( 'total savings after {y:.0f} years: {x:.2f}'.format( x=totSav2, y=i_Years), round( totSav1, 2))
#print( 'total savings after %10.2f} years: %i' %(totSav2, i_Years) ????????
## 2. computation 

print('retirement age:' , retirement(f_iniInvest, f_interest, f_income))