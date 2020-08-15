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
