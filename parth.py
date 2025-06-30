# import calendar

# year = int(input("enter year:"))
# month = int(input("enter month:"))

# cal = calendar.month(year, month)
# print(cal)


# # symple print function
# print("hello python")


# # # addition
# num1 = float(input("enter the frist number for addition:"))
# num2 = float(input("enter the secound number for addition:"))

# sum_result = num1 + num2
# print(f"sum:{num1}+{num2}={sum_result}")


# # multiplication
# num1 = int(input("enter frist number:"))
# num2 = int(input("enter secound number:"))

# sum_result = num1 * num2
# print(f"multiplication:{num1}*{num2}={sum_result}")


# # division
# num1 = int(input("enter frist number:"))
# num2 = int(input("enter secound number:"))

# sum_result = num1 / num2
# print(f"division:{num1}/{num2}={sum_result}")


# # subtraction
# num1 = int(input("enter frist number:"))
# num2 = int(input("enter secound number:"))

# sum_result = num1 - num2
# print(f"division:{num1}-{num2}={sum_result}")


# #   random number
# import random

# print(f"rendom number:{random.randint(1, 100)}")


# # Odd or even number check
# num = int(input("Enter any number: "))

# if num % 2 == 0:
#     print(f"This is an even number.")
# else:
#     print(f"This is an odd number.")

#     # swapping
# a = 10
# b = 15

# # swapping
# a, b = b, a
# print("after swaping")
# print("a=", a)
# print("b=", b)


# # multiplation table
# num = int(input("multiplation table"))
# for i in range(1, 11):
#     print(f"{num}*{i}={num*i}")

#     # patterns
# print("*")
# print("**")
# print("***")
# print("**")
# print("*")

# # display a formatted massage
# # name = (input("name" ))
# # age = (input("age" ))
# # hobby = (input("hobby" ))
# # print(f"Hello," ,name + "!" "At ",age  ",enjoying" hobby  " sounds fun!")


# for i in range(1, 6):  # Outer loop (rows)
#     for j in range(i):  # Inner loop (columns)
#         print("*", end=" ")
#     print()


# num = int(input("any num:"))
# print("multiplacition table of")
# for i in range(1, 11):
#     print(f"{num}*{i}={num*i}")


# for i in range(1, 6):
#     for j in range(1, i):
#         print("*", end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print(j, end=" ")
#     print()
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# for i in range(1, 6):
#     for k in range(1, i):
#         print(" ", end=" ")
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()
# for i in range(1, 6):
#     for k in range(1, 7 - i):
#         print("", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# # 1234554321
# # 1234  4321
# # 123    321
# # 12      21
# # 1        1
# # 1        1
# # 12      21
# # 123    321
# # 1234  4321
# # 1234554321


# def print_pattern():
#     n = 5

#     # Top half
#     for i in range(n):

#         for j in range(1, n - i + 1):
#             print(j, end="")

#         print(" " * (2 * i), end="")

#         for j in range(n - i, 0, -1):
#             print(j, end="")

#         print()

#     # Bottom half
#     for i in range(n):

#         for j in range(1, i + 2):
#             print(j, end="")

#         print(" " * (2 * (n - i - 1)), end="")

#         for j in range(i + 1, 0, -1):
#             print(j, end="")

#         print()


# print_pattern()


# sDict = {x.upper(): x * 3 for x in "coding"}
# print(sDict)
# sDict = {x.lower(): x * 4 for x in "PARTH"}
# print(sDict)


# # Nested list comprehension
# matrix = [[j for j in range(5)] for i in range(3)]

# print(matrix)
# print(matrix)

# parth = [[j for j in range(1, 5)] for i in range(4)]

# print(parth)
# print(parth)


# list = [charector for charector in "parth"]
# print(list)

# list = []
# for i in range(1, 6):
#     for j in range(1, 6):
#         list.append(j)
# print(list)


# list = [i for i in range(20) if i % 2 == 1]
# print(list)


# list = [i for i in range(2000, 3000) if i % 4 == 0]
# print(list)

# list = [i for i in range(4, 41) if i % 4 == 0]
# print(list)


# for i in range(1, 11):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)


# percentage = int(input("enter your score: "))
# if percentage >= 90:
#     print("excellent work! ")
# elif percentage >= 80:
#     print("well done")
# elif percentage >= 70:
#     print("good job")
# elif percentage >= 60:
#     print("you pass")
# else:
#     print("sorry you fail")


      
        
        
    
    
