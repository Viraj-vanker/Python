a=[10,20,30,40]
#b=a
b=a[:]
b[1]=15
print(b)

print(id(a))
print(id(b))

print(a is b)