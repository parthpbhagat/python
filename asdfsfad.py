# pr2.
print("welcome to pattern creater and number analyzer")
print("1. pattern creater")
print("2. number analyzer")     
print("3. exit")
choice = int(input("select option : "))
match choice:
    case 1:
        print("\nPattern Creater")
        row = int(input("Enter the number of rows: "))
        if row <= 0:
            print("Number of rows must be positive.")
        else:
            for i in range(0, row + 1):
                print("* " * i)
    
    case 2:
        print("\nNumber Analyzer")
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start >= end:
            print("Start must be less than end.")
        else:
            for i in range(start, end):
                if i % 2 == 1:
                    print(f"Number {i} is odd")
                else:
                    print(f"Number {i} is even")
            total = sum(range(start, end))
            print(f"Sum of all numbers from {start} to {end} is: {total}")
    
    case 3:
        print("Exiting the program. GOODBYE!")
    
    case _:
        print("Invalid option. Please select 1, 2, or 3.")     