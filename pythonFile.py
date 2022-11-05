import sys

x = 10
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))

print('--------------------------------------------------------------')

x = 10.55
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))



import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8, 10]
y1 = [10, 20, 30, 40, 99]

plt.plot(x1, y1)
plt.show()



x = "10.55"
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))


