# Exception handling

a = int(input())
b = int(input())

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number "))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero:" , e)

except ValueError as e:
    print("Invalid Input:",e)

except Exception as e:
    print("Something went Wrong...:",e)

finally:
    print("resource Closed")