

### This is the Master File
# Create the Functions
# Keep the Functions Open Ended with some Return type


# Finding Even Odd

def even_odd(n) :  # num
    result = "Even" if n%2 == 0 else "Odd" 
    return  result   # "Even" if num%2 == 0 else "Odd" 

"""
print( even_odd(10) )
print( even_odd(1) )
"""


## Area
def findArea(l, b) : 
    return l * b

"""
print(  f" Area of Rectangle = {findArea(14, 10)}" )
"""


## Current Time

def currentTime() : 
    import datetime

    currenttime = datetime.datetime.now()
    myTime = currenttime.strftime("%H : %M AM")
    return myTime

"""
print( currentTime() )
"""






