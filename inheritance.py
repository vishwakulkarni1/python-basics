#single level inheritance : A->B

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")



a1 = A()

a1.feature1()
a1.feature2()


b1 = B()

b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()
