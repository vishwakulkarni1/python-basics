def greet():
    print("Hello")
    print("Good Morning")

greet()

def add(x,y):
     c = x+y
     return c

result = add(5,4)
print(result)


def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(5,4)
print(result1, result2)

