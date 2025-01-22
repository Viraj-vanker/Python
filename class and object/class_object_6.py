class A:
    def __init__(self,b,c):
        self.b=b
        self.c=c
    def result(self):
        print(self.b)
        print(self.c)
class B(A):
    print("vanker")
class C(A):
    def vv(self):
        print("Viraj")
class D(B,C):
    print("Hello")
x=C("A","B")
y=B("A","B")
z=D("A","B")
x.result()
y.result()
z.result()
x.vv()