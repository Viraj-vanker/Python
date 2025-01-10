a=(10,20,30,40,50)
b=list(a)
b[1:3]=[80,90]
a=tuple(b)
print(a)