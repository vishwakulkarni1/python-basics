#prime or not -for else

num = int(input("enter no: "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")