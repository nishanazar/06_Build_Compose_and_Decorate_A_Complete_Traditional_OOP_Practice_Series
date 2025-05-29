class A():
    def show(self):
        print("Hello A")

class B(A):
    def show(self):
        print("Hello B")

class C(A):
    def show(self):
        print("Hello C")

class D(B, C):
    pass

d = D()
print(D.mro())
d.show()