def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
a=fact(5)
print(f"The factorial is {a}")