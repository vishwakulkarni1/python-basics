# Types of variables

class Car:

    wheels = 4  # class variable

    def __init__(self):
        self.mil = 10       # instance variable
        self.com = "BMW"    # instance variable

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 6

print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)