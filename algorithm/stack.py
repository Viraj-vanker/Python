class stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack=[x]+self.stack
    def pop(self):
        return self.stack.pop(0)
s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.stack)
print(s.pop())
print(s.stack)