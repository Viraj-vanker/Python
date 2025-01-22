#hierararchical inheritance

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
x=C("A","B")
y=B("A","B")
x.result()
y.result()
x.vv()