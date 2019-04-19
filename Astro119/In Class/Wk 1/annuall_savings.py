# -*- coding: utf-8 -*-

"""

annual return on $10,000 with intrest 10% over 30 years

"""

#================================================
starting_invest = 1e4
intrest_rate    = .1
years           = 30
#================================================



def annual_return(starting_invest,intrest_rate,years):
    """
    compute annual savings
    input:
        starting_invest = 1e4
        intrest_rate    = .1
        years           = 30

    output:
        savings in last year (years)
        
    """
    
    
    currInvest = starting_invest
    for i in range(years):
        fGrowth = currInvest*intrest_rate
        print('Year', i +1, 'savings', currInvest, 'intrest per year', fGrowth)
        currInvest += fGrowth
    return currInvest   
#add function call
print (annual_return(starting_invest, intrest_rate, years))
