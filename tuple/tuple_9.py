a=(10,20,30)
x=list(a)
b=x*5
y=list(b)

a=tuple(x)
b=tuple(y)
print(b)
print(len(b))

b=(1,2,3,4,5,6,7,8,9)
y=list(b)

y.pop()
y.pop(0)
y.remove(3)
del y[0]

b=tuple(y)
print(b)
del a
#print(a)