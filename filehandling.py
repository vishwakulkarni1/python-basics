# File Handling
"""
f = open('MyData','r')
#print(f.read())
#print(f.readline(),end="")
f1 = open('micky','a')
f1.write("Something\n")
f1.write("People\n")
f1.write('Mobile')



# Copying data of on file to other

f = open('MyData','r')
f1 = open('abc','w')

for data in f:
    f1.write(data)

"""

# for image read and write 

f = open('mumbai.jpg','rb')
f1 = open('Mumbaii.jpg','wb')

for i in f:
    f1.write(i)