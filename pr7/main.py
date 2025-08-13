from datetime_tool import CurrentDateTime, DateDifference, Stopwatch, Timer, Format
from math_tool import MathematicalOperations
from random_tool import RandomDataGenerator
from file_tool import FileOperations
import uuid

# Instances
currentdatetime = CurrentDateTime()
stopwatch = Stopwatch()
timer = Timer()
formatter = Format()
math_op = MathematicalOperations()
random_gen = RandomDataGenerator()
file_op = FileOperations()

def generate_unique_identifiers():
    print("Generated UUID:", uuid.uuid1())

# Main menu
while True:
    print("************ Welcome To A Multi Utility Toolkit ************")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Module Attributes")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            while True:
                print("\n--- Datetime and Time Operations ---")
                print("1. Display Current Datetime")
                print("2. Calculate Date Difference")
                print("3. Custom Format")
                print("4. Stopwatch")
                print("5. Countdown Timer")
                print("6. Back to Main Menu")
                sub = int(input("Enter your choice: "))
                match sub:
                    case 1:
                        currentdatetime.Display_current_datetime()
                    case 2:
                        d1 = input("Enter first date (YYYY-MM-DD): ")
                        d2 = input("Enter second date (YYYY-MM-DD): ")
                        diff = DateDifference(d1, d2)
                        diff.calculate_difference_between_two_dates()
                    case 3:
                        formatter.custome_format()
                    case 4:
                        stopwatch.stopwatch()
                    case 5:
                        timer.countdown_timer()
                    case 6:
                        break
        case 2:
            while True:
                print("\n--- Mathematical Operations ---")
                print("1. Factorial")
                print("2. Compound Interest")
                print("3. Trigonometry")
                print("4. Area Calculations")
                print("5. Back to Main Menu")
                sub_choice = int(input("Enter your choice: "))
                match sub_choice:
                    case 1:
                        math_op.factorial()
                    case 2:
                        math_op.compound_interest()
                    case 3:
                        math_op.trigonometric_calculation()
                    case 4:
                        while True:
                            print("\n--- Area Calculations ---")
                            print("1. Triangle")
                            print("2. Square")
                            print("3. Rectangle")
                            print("4. Circle")
                            print("5. Back")
                            s = int(input("Enter your choice: "))
                            match s:
                                case 1:
                                    math_op.area_of_triangle()
                                case 2:
                                    math_op.area_of_square()
                                case 3:
                                    math_op.area_of_rectangle()
                                case 4:
                                    math_op.area_of_circle()
                                case 5:
                                    break
                    case 5:
                        break
        case 3:
            while True:
                print("\n--- Random Data Generation ---")
                print("1. Random Number")
                print("2. Random List")
                print("3. Random Password")
                print("4. Random OTP")
                print("5. Back to Main Menu")
                sub_choice = int(input("Enter your choice: "))
                match sub_choice:
                    case 1:
                        random_gen.random_number()
                    case 2:
                        random_gen.random_list()
                    case 3:
                        random_gen.create_random_password()
                    case 4:
                        random_gen.generate_random_otp()
                    case 5:
                        break
        case 4:
            generate_unique_identifiers()
        case 5:
            while True:
                print("\n--- File Operations ---")
                print("1. Create File")
                print("2. Write to File")
                print("3. Read File")
                print("4. Append to File")
                print("5. Back to Main Menu")
                sub_choice = int(input("Enter your choice: "))
                match sub_choice:
                    case 1:
                        file_op.create_file()
                    case 2:
                        file_op.write_to_file()
                    case 3:
                        file_op.read_file()
                    case 4:
                        file_op.append_to_file()
                    case 5:
                        break
        case 6:
            module_name = input("Enter module name (e.g., math): ")
            try:
                mod = __import__(module_name)
                print(f"Attributes of {module_name}:")
                print(dir(mod))
            except ModuleNotFoundError:
                print(f"Module '{module_name}' not found.")
        case 7:
            print("Goodbye!")
            break
