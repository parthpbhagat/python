   #file handaling in pythone(employee manegment system)

def Employee():
    with open("parth.txt","a")as f:
        id = (input("enter employee id: "))
        name = (input("enter employee name: "))
        mo_no = (input("mobile number: "))
        f.write("ID: "+ id + "\n")
        f.write("name: "+ name + "\n")
        f.write("mobile number: "+ mo_no + "\n")
        f.close()
        
def Maneger():
    with open("parth.txt","a")as f:
        id = (input("enter maneger id: "))
        name = (input("enter name: "))
        mo_no = (input("enter mobile number: "))
        department = (input("department "))
        f.write("ID: "+ id + "\n")
        f.write("maneger name: "+ name + "\n")
        f.write("mobile number: "+ mo_no + "\n")
        f.write("department: "+ department + "\n")
        f.close()
        
while True:
    print("--------employee manegment system----------")
    print("1. input employee data: ")
    print("2. enter maneger data: ")
    print("3. show all data: ")
    print("4. delete all data: ")
    print("5. exit ")
    
    option = int(input("enter your option:(1/2/3/4/5): "))
    match option:
        case 1:
            Employee()
        case 2:
            Maneger()
        case 3:
            with open("parth.txt","r")as f:
                data = f.read()
                print(data)
        case 4:
              while True:
                conform = input("are you sure to all data clear(yes/no): ")
                if conform == "yes":
                   open("parth.txt","w").close()
                   print("all data cleared ")
                   break
                else:
                   print("opretion cancelled ")
                   break
        case 5:
            print("exit!")
            break
                
