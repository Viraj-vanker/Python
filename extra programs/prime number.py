a=int(input("Enter the number you want to see its prime "))
if a==1 or a==0 :
    print("The number is not prime ")
else :
    for i in range(1,a) :
        if a==2 or a==3 or a==5 or a==7:
            print("The number is prime ")
            break
        elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
            print("The number is not prime ")
            break
        else :
            print("The number is prime ")
            break