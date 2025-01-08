import numpy as np

x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)

#a=a.sum(axis=1)
a=a.sum(axis=0)
print(a)