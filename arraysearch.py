# To search a element in array and print its index number

from array import *

arr = array('i',[])

n = int(input("Enter the length of the array "))

for i in range(n):
    x = int(input("Enter the next value "))
    arr.append(x)

print(arr)

vals=int(input("enter a number you wnant to search "))

k=0
for e in arr:
    if e==vals:
        print(k)
    k=k+1