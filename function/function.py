def arithmatic():

    print("ARITHATIC OPERATOR")

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    """print("the addition is ",a+b)
    print("the subtraction is ",a-b)
    print("the multiplication is ",a*b)
    print("the division is ",a/b)
    print("the modulo is ",a%b)"""
    # print("The multiply multiple ",a**b)
    print("The divide divide ", a // b)
def assignment():

    print("ASSIGNMENT OPERATOR")

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    """a+=b
    print("the addition is ",a)

    a-=b
    print("the subtraction is ",a)

    a*=b
    print("the multiplication is ",a)

    a/=b
    print("the division is ",a)

    a%=b
    print("the modulo is ",a)
    """
    # a**=b
    # print("The multiply multiple ",a)

    a //= b
    print("The divide divide ", a)
def bitwise():

    print("BITWISE OPERATOR")

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    # print("the bitwise and is ",a&b)
    # print("the bitwise or is ",a|b)
    # #print("the bitwise xor is ",a^b)
    # print("the bitwise left swift is ",a<<b)
    # print("the bitwise right swift is ",a>>b)
    print("The bitwise not operator ", ~a)
def identity():

    print("iDENTITY OPERATOR")

    a = [10, 20, 30]
    b = [10, 20, 30]
    c = a

    print(a == b)
    print(a == c)

    print(a is b)
    print(a is c)

    print(a is not b)
    print(a is not c)
def logical():

    print("LOGICAL OPERATOR")

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    print(a == b and a == b)
    print(a == b and a != b)
    print(a != b and a != b)

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    print(a == b or a == b)
    print(a == b or a != b)
    print(a != b or a != b)

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    print(not (a == b and a == b))
    print(not (a == b and a != b))
    print(not (a != b and a != b))
def membership():

    print("MEMBERSHIP OPERATOR")

    a = "vanker viraj"
    b = "viraj"

    print(a in b)
    print(b in a)

    print(a not in b)
    print(b not in a)
def relational():

    print("RELATIONAL OPERATOR")

    # arithmatic operator Hhhh..

    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    print("the less than ", a < b)
    print("the greater than ", a > b)
    print("the less than equals ", a <= b)
    print("the greater than equals ", a >= b)
    print("the equals equal to ", a == b)
    print("the not equal to ", a != b)

def main():
    print("hi")
    arithmatic()
    assignment()
    bitwise()
    identity()
    logical()
    membership()
    relational()
main()