a=input("what you want to do (+,-,*,/,%)")
b=int(input("Enter one number "))
c=int(input("Enter second number "))
match(a):
    case '+':
        print("The addition is ",b+c)
    case '-':
        print("The subtraction is ", b - c)
    case '*':
        print("The multiplication is ", b * c)
    case '/':
        print("The division is ", b / c)
    case '%':
        print("The modulo is ", b % c)
    case '_':
        print("Invalid choice ")