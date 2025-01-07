for i in range(1,101):
    if i==1 or i==0 :
        print(f"{i} is the prime number ")
    else :
        for j in range(1, i):
            if i == 2 or i==3 or i==5 or i==7:
                print(f"{i} is the prime number ")
                break
            elif i % 2 == 0 or i%3==0 or i%5==0 or i%7==0:
                print(f"{i} is not prime number ")
                break
            else:
                print(f"{i} is the prime number ")
                break