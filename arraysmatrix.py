#array fun & multi-dimensional array

"""
from numpy import *

arr1 = array([
                 [1,2,3],
                 [4,5,6]

              ])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
#2d array to 1d array
arr2 = arr1.flatten()
print(arr2)
"""

#3d array
"""
from numpy import *
arr1 = array([
                 [1,2,3,6,2,9],
                 [4,5,6,7,5,3]

              ])

arr2 = arr1.flatten()
arr4 = arr1.reshape(3,4)
arr3 = arr1.reshape(2,2,3)
print(arr3)
print(arr4)
"""

#array to matrix
"""

from numpy import *
arr1 = array([
                 [1,2,3,6],
                 [4,5,6,7]

              ])

m = matrix(arr1)
print(m)
"""
#matrix operations
"""
from numpy import *
j = matrix('1 2 3 6 ; 4 5 6 7')
v = matrix('1 2 ; 3 6 ; 4 5 ; 6 7')
m = matrix('1 2 3; 6 4 5;1 6 7')
print(j)
print(v)
print(m)
print(diagonal(m))
print(m.min())
print(m.max())
"""

#matrix addition and multiplication
from numpy import *
m1 = matrix('1 2 3; 6 4 5;1 6 7')
m2 = matrix('1 2 3; 6 8 5;2 6 7')

m3 = m1 + m2
m4 = m1 * m2;

print(m3)
print(m4)