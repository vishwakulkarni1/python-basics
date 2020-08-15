#normal fun
x=int(input("enter no "))
def square(a):
    return a * a
result = square(x)
print(result)

#lambda fun
#square of a number

f = lambda a: a*a
result = f(5)
print(result)


#adding two numbers

f = lambda a,b : a+b
result = f(5,6)
print(result)