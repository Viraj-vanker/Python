import numpy as np
a=np.array([[50,10,20],[60,40,30],[90,70,80]])
print(a.argmax(axis=1))
print(a.argmin(axis=1))

print()

print(a.argmax(axis=0))
print(a.argmin(axis=0))