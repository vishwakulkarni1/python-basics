# Method Overriding

class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
        
a1=B()
a1.show()
