a=(10,20,30,40)
b=a[:]
c=list(a)
d=list(b)
d[1]=15

a=tuple(c)
b=tuple(d)
print(b)

print(id(a))
print(id(b))

print(a is b)