class cls:
    a=10
    def __init__(self,b):
        self.b=b
        print(b)
x=cls(10)
print(x.a+x.b)
print(cls.a)