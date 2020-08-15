#new array from existing

"""
from array import *
vals=array('i',[5,9,-8,4,2])
newArr=array(vals.typecode,(a for a in vals))
for e in newArr:
    print(e)

"""

# assign square of frst array element to new array

from array import *

vals = array('i', [5, 9, -8, 4, 2])
print(vals)
newArr = array(vals.typecode, (a*a for a in vals))
for e in newArr:
    print(e)


