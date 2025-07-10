#                     Q1


class Person:
    name = None

    def _init_(self):
        self.name = input("enter your name: ")
        print(f"name = {self.name}")

    def getdata(self):
        print(f"name = {self.name}")


p1 = Person()


# Array of object

class Student:

    name = None
    age = None

    # setter
    def set(self):
        self.name = input("Enter Your Name")
        self.age = int(input("Enter Your Age"))

    # getter
    def get(self):
        print(f"Name = {self.name}  &  Age = {self.age}")


student_data = []


number = int(input("How Many Student ?"))

print(student_data)  # 1

for object in range(number):
    student_data.append(Student())


print(student_data) # 2


for i in range(number):
    student_data[i].set()
    # student_data[i].get()

for i in range(number):
    student_data[i].get()


def outer():
    print("this is a outer function: ")

    def inner_1():
        print("this is a inner function: ")
        def inner_2():
            for i in range(5):
                print("this is a inner function: ")
        inner_2()

    inner_1()
p1 = outer()
print(p1)


class Movies():
    a = "call a"
class Holywood(Movies):
    b = "call b"
class Boliwood(Movies):
    c = " call c"


p1 = Boliwood()
p1 = Holywood()

print(p1.a)
print(p1.b)


        #        override the class and function
class India():
    def parsone(self):
        print("enter your name:")
        print("enter your address: ")
        print("enter your mo no: ")
class Pakistan(India):
    def parsone(self):
        print("enter your name:")
        print("enter your address: ")
        print("enter your mo no: ")
n1 = India()
n1 = Pakistan()
n1.parsone()


# single inheritance
class A:
    name = "parth bhagat"
    school = "NTR"
class B(A):
    age = 27

o1 = B
print(o1.name,o1.school,o1.age)


# mulptipal inheritance
class A:
    name = "bhagat parth"
class B(A):
    school = "NTR"
class C(B):
    age = 27

o1 = C
print(o1.name,o1.school,o1.age)


# hirachical inheritance
class A:
    a = "call a"
class B(A):
    b = "call b"
class C(A):
    c = "call c"
class D(A):
    d = "call d"

o1 = B()
o2 = D()

print(o1.a,o2.d,o1.b,C.c)
print(A.a,B.b,C.c,D.d)


#  oop projrct

while True:
    print("choose an opretion: ")
    print("1. create an person ")
    print("2. create an employe")
    print("3. create a manager")
    print("4. show details")
    print("5. compaire salaries")
    print("6. exit")

    choice = int(input("enter your choice: "))

    class Persone:
        name = None
        age = None

        def setdata(self):
            self.name = input("enter persone name: ")
            self.age = int(input("enter persone age: "))

        def getdata(self):
            print("persone created with name:", self.name, "and age:", self.age)

    class Employee:
        name = None
        age = None
        ID = None
        salary = None

        def setdata(self):
            self.name = input("enter name: ")
            self.age = int(input("enter age: "))
            self.ID = int(input("enter employee ID: "))
            self.salary = int(input("enter salary: "))

        def getdata(self):
            print(
                "employee created with name: ",
                self.name,
                "age: ",
                self.age,
                "ID: ",
                self.ID,
                "and salary:",
                self.salary,
            )

    class Manager:
        name = None
        age = None
        ID = None
        salary = None
        department = None

        def setdata(self):
            self.name = input("enter name: ")
            self.age = int(input("enter age: "))
            self.ID = int(input("enter employee ID: "))
            self.salary = int(input("enter salary: "))
            self.department = input("enter department: ")

        def getdata(self):
            print(
                "manager created with name:",
                self.name,
                "age: ",
                self.age,
                "ID: ",
                self.ID,
                "salary: ",
                self.salary,
                "and department: ",
                self.department,
            )

    match choice:
        case 1:
            p1 = Persone()
            p1.setdata()
            p1.getdata()

        case 2:
            e1 = Employee()
            e1.setdata()
            e1.getdata()

        case 3:
            M1 = Manager()
            M1.setdata()
            M1.getdata()

        case 4:
            while True:
                print("1. person")
                print("2. employee")
                print("3. manager")
                choose = int(input("choose details to show: "))
                match choose:
                    case 1:
                        if p1:
                         print("**person datail** ")
                         print("name: ", p1.name)
                         print("age: ", p1.age)
                        else:
                            print("persone not created ")
                    case 2:
                        if e1:
                         print("**employee datail**")
                         print("name: ", e1.name)
                         print("age: ", e1.age)
                         print("ID: ", e1.ID)
                         print("salary: ", e1.salary)
                        else:
                            print("employee not created ")
                    case 3:
                        if M1:
                         print("**manager datail**")
                         print("name: ", M1.name)
                         print("age: ", M1.age)
                         print("ID: ", M1.ID)
                         print("salary: ", M1.salary)
                         print("department: ", M1.department)
                        else:
                            print("manager not created")
                    case 4:
                        print("invalide opction:")
                        break

        case 5:
            if e1 and M1:
                if e1.salary > M1.salary:
                    print("employee has a higher salary")
                elif e1.salary < M1.salary:
                    print("manager has a higher sallary")
                else:
                    print("both are same salary")
            else:
               print("plase create both employee and maneger frist")

        case 6:
            print("exit thank you ")
            break
