# Constructor Self and Compairing Objects

# compare objects

class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()

# c1.name = "Rashi"
# c1.age = 12

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

# c1.update()

print(c1.name)
print(c2.name)