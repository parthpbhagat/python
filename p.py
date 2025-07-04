# name = input("enter your name ")
# print(name)


# for i in range(1,10):
#     print(i,end=" ")
# print()



#              parsonal information
# name = input("enter your name ")
# # age = int(input("enter your age "))
# # college_name = (input("enter college name "))
# # print("Hello")
# # print("my name is ",name,"i am ",age)
# # print ("i complited AI/ML course from ",college_name,"my hobbis are coeding")
# # print("my aim is a AI engenear in the future")


# for i in range(0,10):
#       print(name)


# for i in range (0,10):
#     for j in range(1,i+1):
#             print("*",end=" ")
#     print()


# for i in range (1,8):
#       if i == 1:
#             print("********")
#       elif i == 2 or i == 3:
#             print("*")
#       elif i == 4:
#             print("********")
#       elif i == 5 or i == 6:
#             print("*")
#       elif i == 7:
#             print("********")
#       else:
#             print("")




# print("welcome to custumor service center")


# print("please select your language")
# print("1. for gujrati")
# print("2. for hindi")
# print("3. for english")


# language_option = int (input ("enter your option: "))

# if language_option == 1:
#     print ("1. top up rechrge mate 1 dabao")
#     print("2. internet recharge mate 2 dabao")
#     print("3. spectial recharge mate 3 dabao")
#     chouce = int(input("enter your chouce: "))
#     if chouce == 1:
#         print("tamaru top up recharge thai gayu chhe")
#     elif chouce == 2:
#         print("tamaru intarnet recharge thai gayu che ")
#     elif chouce == 3:
#         print("tamaru spectial recharge thai gayu che ")
#     else:
#         print("valide option dabao")
# elif language_option == 2:
#     print("1. top up recharge ke liye 1 dabaye ")
#     print("2. internet recharge ke liye 2 dabaye ")
#     print("3. spectial recharge ke kiye 3 dabaye ")
#     chouce = int(input("enter your chouce: "))

#     if chouce == 1:
#         print("aapka top up recharge ho gaya hai ")
#     elif chouce == 2:
#         print("aapaka internet recharge ho gaya hai ")
#     elif chouce == 3:
#         print("aapaka spectial recharge ho gaya hai")
#     else:
#         print("valide option dabaiye ")
# elif language_option == 3:
#     print("1. for top up recharge press 1")
#     print("2. for internet recharge press 2")
#     print("3. for spectial recharge press 3")
#     chouce = int(input("enter your chouce: "))

#     if chouce == 1:
#         print("your top up recharge is suscessfully done")
#     elif chouce == 2:
#         print("your internet recharge is suscefully done")
#     elif chouce == 3:
#         print("your spectial recharge is suscefully done")
#     else:
#         print("please enter a valid option")
# print("thank you for using our service")
# print("have a nice day")


print("welcome to our restorunt sir/madem")

print("----------menu---------")
print("1. pizza = 120")
print("2. sandwich = 60")
print("3. momos = 150")
print("4. exit ")

pizza_price = 120
sandwich_price = 60
momos_price = 150

total_bil = 0

while True:
  take_order = int(input("enter item number(1 to 4): "))

  if take_order == 1:
    Quantity = int(input("enter quantity for pizza: "))
    total_bil += (pizza_price * Quantity)
    print("pizza added to bill ")
  elif take_order == 2:
    Quantity = int(input("enter quantity for sandwich: "))
    total_bil += (sandwich_price * Quantity)
    print("sandwich added to bill ")
  elif take_order == 3:
    Quantity = int(input("enter quantity for momos: "))
    total_bil += (momos_price * Quantity)
    print("momos added to bill ")
  else:
    print("exit")
    break 
print(("total amount "),total_bil)
discount = int(input("enter discount %: "))
add_discount = (total_bil * discount) / 100
total_paid = total_bil - add_discount
print("total paid: ",total_paid)

gst = int(input("enter GST "))














