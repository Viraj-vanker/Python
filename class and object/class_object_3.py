#multilevel inheritance

class cls:
    def __init__(self,b,c):
        self.b=b
        self.c=c
    def result(self):
        print(self.b)
        print(self.c)
class cls1(cls):
    print("Vanker")
class cls2(cls1):
    def vv(self):
        print("Viraj")
x=cls2("A","B")
x.result()
x.vv()