

#           #Q
set = {"parth","purushottam","bhagat","chetan"}
print(set)


#           #Q2
information = {
    "name": "parth",
    "age" : 27,
    "city" : "ahemdabad"
}
information.setdefault("mobile_number",9011494385)#add new key and value
information.pop("age")#removed age item
print(information)


#             @Q3
#  "multi-line" Strings

mystring = """Hello

This is
Stechies
for,
Tech tutorials."""

# Print string
print(mystring)



string = "Hello\n" \
"this is \n" \
"stechies\n" \
"for\n" \
"teach tutorials."
print(string)



list = ["1","2","3","4","5","6"]
list.insert(6,7) #insert opretion
print(list)


list1 = [1,2,3,4,5,6]
print(list1[::-1])#reverse list





frist_name = input("enter your name:")
last_name = input("enter your last name:")
print("hello",last_name,frist_name)


