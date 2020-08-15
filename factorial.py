#factorial without recursion

x=int(input("enter no: "))
def fact(n):

    f = 1

    for i in range(1,n+1):
        f = f * i
    return f


result = fact(x)


print(result)