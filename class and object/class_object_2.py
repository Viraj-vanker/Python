#single(simple) inheritance

class cls:
    def __init__(self,b,c):
        self.b=b
        self.c=c
    def result(self):
        print(self.b)
        print(self.c)
class cls1(cls):
    def vv(self):
        print("Viraj")
x=cls1("A","B")
x.result()
x.vv()