def a(n):
    b,c = 0,1
    for i in range(n):
        print(b, end=" ")
        b,c = c, b + c
v=int(input("Enter the number you want fibonaci of "))
a(v)