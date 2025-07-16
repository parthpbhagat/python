# #    multiplatcation table

# num = int(input("enter number: "))
# for i in range (0,11):
#     print(f"{num} * {i} = {num * i}")


#   #  facorial

# import math
# num = int(input("enter number: "))
# print(math.factorial(num))


# # any number skiped using loop
# for i in range (1,10):
#     if i == 4 or i == 6:
#         continue
#     print(i)


#   fibonacci series


# a = 0
# b = 1


# turn = int(input("enter number of turn: "))
# for i in range(turn):
#     print(a)
#     c = a + b
#     a = b
#     b = c


# # angle finder

# frist_angle = int(input("enter frist angle: "))
# secound_angle = int(input("enter secound angle: "))
# thard_angle = 180-(frist_angle+secound_angle)
# print(thard_angle)

# #  sum of list
# sum = 0
# for i in range(1,10):
#     sum += i
#     print(sum)

#           list
# list = [1,2,4,5,6,7,8,9,10]
# list.insert(2,3)
# print(list)

# list.remove(9)
# print(list)

# list.index(5)
# print(list)


# a = 5
# b = 6

# a,b=b,a
# print(a)
# print(b)


# a = 5
# b = 6
# a,b=b,a
# print(a)
# print(b)


# class Person:
#     def __init__(self):
#      self.name = None
#      self.age = None
#      self.address = None

#     def setdata(self):
#      self.name = (input("enter your name: "))
#      self.age = (input("enter your age: "))
#      self.address = (input("enter your address:"))

#     def getdata(self):
#      print("name:", self.name)
#      print("age: ", self.age)
#      print("address: ", self.address)


# p1 = Person()
# p1.setdata()
# p1.getdata()


# class Person:
#     name = None
#     age = None
#     address = None
#     def setdata(self):
#         self.name = input("enter your name: ")
#         self.age = int(input("enter your age: "))
#         self.address = input("enter your address: ")

#     def getdata(self):
#         print("name: ",self.name)
#         print("age: ",self.age)
#         print("address: ",self.address)

# p1 = Person()
# p1.setdata()
# p1.getdata()


# class Person:
#     name = None
#     age = None
#     address = None

#     def setdata(self):
#         self.name = input("enter name")
#         self.age = input("enter age: ")
#         self.address = input("enter address: ")

#     def getdata(self):
#         print("name: ", self.name)
#         print("age: ", self.age)
#         print("address: ", self.address)


# class Maneger:
#     name = None
#     age = None
#     address = None
#     sallary = None

#     def setdata(self):
#         self.name = input("enter name: ")
#         self.age = input("enter age: ")
#         self.address = input("enter address: ")
#         self.sallary = int(input("enter maneger sallery: "))

#     def getdata(self):
#         print("name: ", self.name)
#         print("age: ", self.age)
#         print("address: ", self.address)
#         print("sallary: ", self.sallary)


# class Employee(Maneger):
#     def setdata(self):
#         return super().setdata()

#     def getdata(self):
#         return super().getdata()


# p1 = Person()
# m1 = Maneger()
# e1 = Employee()

# p1.setdata()
# m1.setdata()
# e1.setdata()

# print("-----show data------")
# print("*******person information***********")
# p1.getdata()
# print("*******maneger information********** ")
# m1.getdata()
# print("*******employee information********* ")
# e1.getdata()



# value = 2+3*4/2
# print(value)


# value = 5+2*3
# print(value)

# import time
# current_time = time.time()
# print(current_time)


# import time
# current_time = time.strftime("%H:%M:%S")
# print(current_time)

from datetime import datetime
now = datetime.now()
print("current date time", now)
