# Object Oriented Programming
# class and object
"""
class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

x = 9
print(type(x))
a = '8'
print(type(a))
com1 = Computer()

print(type(com1))


"""
class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()
