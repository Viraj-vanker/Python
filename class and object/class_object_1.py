class cls:
    a=10
    def __init__(self,b):
        self.b=b
        print(b)
    def __del__(self):
        print("called")
x=cls(10)
