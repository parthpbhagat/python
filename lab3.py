

#        #Q1
frist_name=(input("frist name: "))
last_name=(input("last name: "))
print(f"Hallo,[{last_name}],[{frist_name}]")


#       #Q2
s1 = "The price of {iteam} is {prise} doller." 
print(s1) 
print(s1.format(iteam="apple",prise="5.50"))


#              #Q3
s1 = (input(""))
print(s1)
print(s1[::-1]) #reverse the sentance


#                     #Q4
s1 = (input(""))
print(s1.lower()) #lower case 
print(s1.upper())  #upper case
print(s1.title())  #title case

#                   #Q5
list1 = ["1","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[10]"]
(list1.append("[11]"))#append function
print(list1)#print updated list

#                 #Q6
list1 = input("").split()
list1 = [int(num)for num in list1]
largest = max(list1)
smallest = min(list1)
print("largest number:",largest)
print("smallest number is:",smallest)

#                #Q8
list1 = [1,2,4,5,6]
list1.insert(2,3)
print(list1)

list1 = [1,2,4,5,6]
list1.remove(6)
print(list1)

list1 = [1,2,4,5,6]
list1.index(5)
print(list1)



#           #Q10
list1 = [1,2,3,4,5,6,7,8,9,10]
list1.insert(12,11)
print(list1)

list1 = [1,2,3,4,5,6,7,8,9,10]
list1.remove(10)
print(list1)

list1 = [1,2,3,4,5,6,7,8,9,10]
del list1[3]
print(list1)

list1 = [1,2,3,4,5,6,7,8,9,10]
list1.insert(0,0)
print(list1)

#          @Q11
list1 = [1,2,3,4,5]
list2 = ["parth","jay","arpit"]
list3 = ["A","B","C"]

add = (list1,list2,list3)
print(add)


#                  #Q12
a = 5
b = 6

#swaping and store data thard variable
c = a
a = b
b = c

print("a =", a)
print("b =", b)

# #                  #Q13
a = 5
b = 6

#swaping without using store thard veriable
a , b=b, a

print("a =", a)
print("b =", b)


