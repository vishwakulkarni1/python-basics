#ways of creating arrays

#using array function
"""
from numpy import *
arr = array([1,2,3,4,5],float)
print(arr.dtype)
print(arr)

"""

#using linspace function
"""
from numpy import *
arr = linspace(0, 15,16)
print(arr)

"""

#using arange function
"""
from numpy import *
arr = arange(0, 15,2)
print(arr)

"""

#using logspace function
"""
from numpy import *
arr = logspace(1,40,5)
print('%.2f' %arr[4])
print(arr)

"""

#using ones function
"""
from numpy import *
arr = ones(5,int)
print(arr)

"""

#using zeros function
from numpy import *
arr = zeros(5,int)
print(arr)