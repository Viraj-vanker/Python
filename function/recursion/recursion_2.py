def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        ss = fact(n-1)+fact(n-2)
        return ss
v=int(input("Enter the number you want the fibonacci of "))
print(fact(v))