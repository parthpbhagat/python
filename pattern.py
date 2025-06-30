



#                 pattern 1
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



#                  pattern 2
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1  
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(j, end=" ")
    print()

#                 pattern 3
# *****

# *   *

# *****

# *

# *
for i in range(1, 6):
    # for j in range(1,i+1):
    if i == 1:
        print("*****")
    elif i == 2:
        print("*   *")
    elif i == 3:
        print("*****")
    elif i == 4:
        print("*")
    else:
        print("*")
    print()
    
    
#                   pattern 
    
    
    
    
#                     pattern 4
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()







                #    pattern 5
# 1234554321
# 1234  4321
# 123    321
# 12      21
# 1        1
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
def print_pattern():
    n = 5
    # Top half
    for i in range(n):
        for j in range(1, n - i + 1):
            print(j, end="")
        print(" " * (2 * i), end="")
        for j in range(n - i, 0, -1):
            print(j, end="")
        print()
    # Bottom half
    for i in range(n):
        for j in range(1, i + 2):
            print(j, end="")
        print(" " * (2 * (n - i - 1)), end="")
        for j in range(i + 1, 0, -1):
            print(j, end="")
        print()


print_pattern()

                        #  pattern 6

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()



#                 pattern 7
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10   
for i in range(1,6):
    for j in range(1,i+6):
        print(j,end=" ")
    print()
    
  
  
  
  
  
  
  
  
#                  pattern 8 
#     1
#    123
#   12345
#  1234567
# 123456789
def full_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print(k, end="")
        print()
full_pyramid(5)


#                 pattern 9
#          *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
for i in range(1,6+1):
    for j in range(6-i):#create spase
        print(" ",end=" ")
    for k in range(1, 2*i):
        print("*",end=" ")
    print()
   
   
    
 #                  pattern 10 
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *  
for i in range(1,6):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print() 
for i in range(6,1,-1):
    for j in range(0,6-i):#create spase
        print(" ",end=" ")
    for k in range(i, 2*i-1):
        print("*",end=" ")    
    for k in range(1,i-1):
        print("*",end=" ")
    print()
    
   
   
   
   
   
   
    
#              pattern 11
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21 
num = 1 
for i in range(1,6+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()
    
    
    
    
    
    
    
    
    
    
#                        pattern 12 
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
for i in range(6,1,-1):
    for j in range(0,6-i):#create spase
        print(" ",end=" ")
    for k in range(i, 2*i-1):
        print("*",end=" ")    
    for k in range(1,i-1):
        print("*",end=" ")
    print()   
for i in range(1,6):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print() 
    
    
    
#                  pattern 13
# *
# *
# *
# *
# *********
for i in range(1,6):
    if i == 1:
        print("*")
    elif i == 2:
        print("*")
    elif i == 3:
        print("*")
    elif i == 4:
        print("*")   
    else:
        print("*********")
print()



                        # pattern 13
# -------
# |     |
# |     |
# -------
# |
for i in range(1,6):
    if i == 1:
        print("-------")
    elif i == 2:
        print("|     |")
    elif i == 3:
        print("|     |")
    elif i == 4:
        print("-------")
    elif i == 5:
        print("|")
    else:
        print("|")
print()


#                     pattern 14
# ************
#  *        *
#   *      *
#    *    *
#     *  *
#      *
#     * *
#    *   *
#   *     *
#  *       *
# *         *
# ***********
# Top half 
for i in range(6):
    print(" " * i, end="")  
    if i == 0:
        print("*" * ((6 - i) * 2))  
    else:
        print("*" + " " * ((6 - i) * 2 - 2) + "*")
# Bottom half
for i in range(1, 6 + 1):
    print(" " * (6 - i), end="")  
    if i == 6:
        print("*" * (i * 2 - 1))  
    else:
        print("*" + " " * (i * 2 - 3) + "*")
        
        
        

