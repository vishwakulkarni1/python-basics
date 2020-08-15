a = 10


def something():
    global a
    a = 16



    print("in fun ",a)

something()

print("outside ",a)




a = 10
print(id(a))

def something():
    a = 9

    x = globals()['a']
    print(id(x))
    print("in fun ",a)

    globals()['a'] = 15 #changing global variable without affecting local variable



something()

print("outside ",a)