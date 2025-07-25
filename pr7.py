import math
import random
import string
import uuid

#   ******************date and time oprections********************
import datetime


class CurrentDateTime:
    def __init__(self):
        pass

    def Display_current_datetime(self):
        self.current_datetime = datetime.datetime.now()
        print("-" * 40)
        print(f"current date and time: ",self.current_datetime.strftime("%d-%m-%Y %H:%M:%S"),)
        print("-" * 40)


currentdatetime = CurrentDateTime()


# # difference between two date
# from datetime import datetime

# class DateDifference:
#     def __init__(self, date1_input, date2_input):
#         self.date1_input = date1_input
#         self.date2_input = date2_input

#     def calculate_difference_between_two_dates(self):
#         # Correct usage of strptime
#         self.date1 = datetime.strptime(self.date1_input, "%Y-%m-%d")
#         self.date2 = datetime.strptime(self.date2_input, "%Y-%m-%d")
#         difference = self.date2 - self.date1
#         print(f"The difference between the two dates is: {difference.days} days.")

# # Example usage
# defference = DateDifference("2023-07-20", "2025-07-25")


# stopwatch function
import time


class Stopwatch:
    def __init__(self):
        pass

    def stopwatch(self):
        input("Press Enter to start the stopwatch...")
        self.start_time = time.time()

        input("Press Enter to stop the stopwatch...")
        self.end_time = time.time()

        self.elapsed_time = self.end_time - self.start_time
        print("*" * 40)
        print(f"Elapsed time: {self.elapsed_time:.2f} seconds")
        print("*" * 40)


stopwatch = Stopwatch()


# countdown timer
import time


class Timer:
    def __init__(self):
        pass

    def countdown_timer(self):
        seconds = int(input("Enter time in secound: "))
        while seconds:
            mins, secs = divmod(seconds, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            print(time_format, end="\r")  # '\r' to overwrite the line
            time.sleep(1)
            seconds -= 1
            
        print("*"*40)
        print("00:00\nTime's up!")
        print("*"*40)


timer = Timer()


# custom format
import datetime
class Format:
    def __init__(self):
        pass

    def custome_format(self):
        self.current_datetime = datetime.datetime.now()
        print("*" * 40)
        print(f"current date and time: ",self.current_datetime.strftime("%A, %d %B %Y - %I:%M %p"),)
        print("*" * 40)


format = Format()


#   *******************mathmetical oprections***********************
class Mathematical_opraction:
    def __init__(self):
        pass

    def factorial(self):
        print("*"*40)
        self.number = int(input("enter your number: "))
        self.result = math.factorial(self.number)
        print(f"{self.number},is factorial {self.result}")
        print("*"*40)

    def Trigonometric_calculaction(self):
        self.angle_degree = int(input("enter angle in a degree: "))
        self.angle_radians = math.radians(self.angle_degree)

        self.sine = math.sin(self.angle_radians)
        self.cosine = math.cos(self.angle_radians)
        self.tangent = math.tan(self.angle_radians)
        print("*"*40)
        print(f"sin({self.angle_degree}) = {self.sine}")
        print(f"cos({self.angle_degree}) = {self.cosine}")
        print(f"tan({self.angle_degree}) = {self.tangent}")
        print("*"*40)

    def area_of_trangle(self):
        print("*"*40)
        self.base = int(input("enter trangle base: "))
        self.hight = int(input("enter trangle highat: "))
        self.area = 0.5 * self.base * self.hight
        print("area of trangle: ", self.area)
        print("*"*40)

    def area_of_squre(self):
        print("*"*40)
        self.side = int(input("enter one side of squre: "))
        self.area = self.side * self.side
        print("area of squre: ", self.area)
        print("*"*40)

    def area_of_rectangle(self):
        print("*"*40)
        self.width = int(input("enter width: "))
        self.length = int(input("enteer length: "))
        self.area = self.length * self.width
        print("area of rectangle: ", self.area)
        print("*"*40)

    def area_of_circle(self):
        print("*"*40)
        self.radius = float(input("enter radius: "))
        self.area = math.pi * self.radius * self.radius
        print(self.area)
        print("*"*40)


mo = Mathematical_opraction()


#  ************random data  genraction*******************
class Random_data_genrater:
    def __init__(self):
        pass

    def random_number(self):
        print("*"*40)
        self.num = random.randint(1, 100)
        print(self.num)
        print("*"*40)

    # def random_list(self):
    #     self.list = []
    #     for _ in range(10):
    #         self.number = random.randint(1, 100)
    #         self.list.append(self.number)
    #         print("random number list: ", self.list)

    def create_random_password(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(self.characters) for _ in range(6))
        print("*"*40)
        print(password)
        print("*"*40)

    def generate_random_otp(self):
        length = 6
        otp = "".join(random.choice("0123456789") for _ in range(length))
        print("*"*40)
        print("Generated OTP:", otp)
        print("*"*40)


r = Random_data_genrater()

#  ******************generate uniq identifiers(UUID)*******************
def generate_uniq_identifiers():
    print("the random genarate UUID: ",uuid.uuid1())

# ******************file oprection*********************************
class File_oprection:
    def __init__(self):
        self.file_name = ""
    def create_file(self):
        self.file_name = input("enter the file name(e.g xyz.txt): ")
        with open(f"{self.file_name}","w")as f:
            print(f"file'{self.file_name}'created sussfully")

    def write_to_file(self):
        content = input("\nEnter the content to write to the file: ""\n")
        with open(self.file_name, "w") as f:
            f.write(content)
        print(f"Content written to '{self.file_name}' successfully.")
        
    def read_file(self):
        try:
            with open(self.file_name, "r") as f:
                content = f.read()
                print("File content:")
                print(content)
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")
    def append_to_file(self):
        self.content = input("Enter the content to append to the file: ")
        with open(self.file_name, "a") as f:
            f.write(self.content + "\n")
        print(f"\nContent appended to '{self.file_name}' successfully.")

fo = File_oprection()   
#   main menu
while True:
    print("************ Welcome To A Multi Utility Toolkit*********")
    print("1. Datetime and time oprations")
    print("2. Mathematical opractions ")
    print("3. Random Data generations ")
    print("4. Generate uniq identifiers(UUID) ")
    print("5. File oprations ")
    print("6. Explore module attributes ")
    print("7. Exit ")

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            while True:
                print("**********Datetime and time oprations**********")
                print("1. Display current datetime")
                print("2. Calculate difference bitween two date")
                print("3. Format date into custom format")
                print("4. Stopwatch")
                print("5. countdown timer")
                print("6. Back to main menu")
                Subchoice = input("enter your choice: ")
                match Subchoice:
                    case "1":
                        currentdatetime.Display_current_datetime()
                    case "2":
                        #    defference.calculate_difference_between_two_dates()
                        pass
                    case "3":
                        format.custome_format()
                    case "4":
                        stopwatch.stopwatch()
                    case "5":
                        timer.countdown_timer()
                    case "6":
                        print("Back to main menu")
                        break
        case "2":
            while True:
                print("************Mathemetical opraction**********")
                print("1. Calculate factorial")
                print("2. Solve compound interest")
                print("3. Trigonometric calculaction")
                print("4. Area of Geometric shaps")
                print("5. Back to main menu")
                subchoice = input("enter your choice: ")
                match subchoice:
                    case "1":
                        mo.factorial()
                    case "2":
                        pass
                    case "3":
                        mo.Trigonometric_calculaction()
                    case "4":
                        while True:
                            print("----------Area of Geometric shaps-----------")
                            print("1. Trangle shaps")
                            print("2. Square shaps")
                            print("3. Rectangle shaps")
                            print("4. Circle shaps")
                            print("5. Back to main menu")
                            subchoice = input("enter your choice: ")
                            match subchoice:
                                case "1":
                                    mo.area_of_trangle()
                                case "2":
                                    mo.area_of_squre()
                                case "3":
                                    mo.area_of_rectangle()
                                case "4":
                                    mo.area_of_circle()
                                case "5":
                                    print("Back to main menu")
                                    break
                    case "5":
                        print("Back to main menu")
                        break
        case "3":
            while True:
                print("************random data genrection**********")
                print("1. Generate random number")
                print("2. Generate random list")
                print("3. create random password")
                print("4. Generate random OTP ")
                print("5. Back to main menu")
                subchoice = input("enter your choice: ")
                match subchoice:
                    case "1":
                        r.random_number()
                    case "2":
                        # r.random_list()
                        pass
                    case "3":
                        r.create_random_password()
                    case "4":
                        r.generate_random_otp()
                    case "5":
                        print("Back to main menu")
                        break

        case "4":
            print("Generate uniq identifiers")
            generate_uniq_identifiers()
            break
        case "5":
            while True:
                print("---------File oprection-----------")
                print("1. Create a new file")
                print("2. Write to a file")
                print("3. Read to a file")
                print("4. Append to a file")
                print("5. Back to main menu")
                
                subchoice = input("enter your choice: ")
                match subchoice:
                    case "1":
                        fo.create_file()   
                    case "2":
                        fo.write_to_file()
                    case "3":
                        fo.read_file()                             
                    case "4":
                        fo.append_to_file()                
                    case "5":
                        print("Back to main menu")
                        break
        case "6":
            print("explore module attributes")
            break
        case "7":
            print("exit Goodby.......")
            break
        case _:
            print("invalide choice")
