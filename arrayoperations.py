"""
#array increment
from numpy import *

arr3=array([1,2,3,4,5])
arr3=arr3+5
print(arr3)

#adding two arrays
arr4 = array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])
arr = arr4 + arr2
print(arr)


#array operations
arr1 = array([1,2,3,4,5])
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))

#concatenation of array
arr5 = array([1,2,3,4,5])
arr6 = array([6,1,9,3,2])
print(concatenate([arr5,arr6]))

# copying one array to other
arr7 = array([2,6,8,1,3])
arr8 = arr7
print(arr7)
print(arr8)
print(id(arr7))
print(id(arr8))

"""

# copying of array
from numpy import *
arr1 = array([2,6,8,1,3])
#arr2 = arr1.view() #shallow copy
arr2 = arr1.copy() #deep copy

arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
