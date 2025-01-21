# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,x):
#         self.stack=self.stack+[x]
#     def pop(self):
#         return self.stack.pop(0)
# s=stack()
# s.push(10)
# s.push(20)
# s.push(30)
# print(s.stack)
# print(s.pop())
# print(s.stack)
# s.push(40)
# print(s.stack)

class queue:
    def __init__(self):
        self.queue=[]
    def push(self,x):
        self.queue.append(x)
    def pop(self):
        return self.queue.pop(0)
s=queue()
s.push(10)
s.push(20)
s.push(30)
print(s.queue)
print(s.pop())
print(s.queue)
s.push(40)
print(s.queue)