def manager():
    print("Name is Rahul")
    print("can access faculty and student ")
def faculty_1():
    print("name is sanidhy")
    print("can access only student")
def faculty_2():
    print("name is hardik")
    print("can access only student")
def student_1():
    print("name is viraj")
    print("can only access his")
def student_2():
    print("name is jatin")
    print("can only access his")
def student_3():
    print("name is dhruv")
    print("can only access his")
a=input("Enter the ID")
if a=="rahul":
    b=input("Enter password")
    if b=="123":
        manager()
        faculty_1()
        faculty_2()
        student_1()
        student_2()
        student_3()
    else:
        print("wrong password")
elif a=="sanidhy":
    b = input("Enter password")
    if b =="123":
        faculty_1()
        faculty_2()
        student_1()
        student_2()
        student_3()
    else:
        print("wrong password")
elif a=="viraj":
    b = input("Enter password")
    if b == "123":
        student_1()
    else:
        print("wrong password")
elif a=="jatin":
    b = input("Enter password")
    if b == "123":
        student_2()
    else:
        print("wrong password")
elif a=="dhruv":
    b = input("Enter password")
    if b == "123":
        student_3()
    else:
        print("wrong password")
else:
    print("invalid id")