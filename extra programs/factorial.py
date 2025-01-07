import math
from math import factorial

a=int(input("Enter the number you want factorial "))
f=1
for i in range(1,a+1):
   f=f*i
print(f)
b=int(input("Enter the number you want factorial "))
print(factorial(b))