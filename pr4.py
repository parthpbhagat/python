
#                   PR 4 functional treat


data = []
data_2d = []

def input_array():
    global data
    list1 = input("Enter elements of array (space-separated): ").split()
    data = [int(num) for num in list1]
    return data

def input_2d_array():
    global data_2d
    rows = int(input("Enter number of rows for 2D array: "))
    cols = int(input("Enter number of columns: "))
    data_2d = []
    for i in range(rows):
        row = input(f"Enter elements for row {i+1} (space-separated): ").split()
        if len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            return input_2d_array()
        data_2d.append([int(num) for num in row])
    return data_2d

def display_data_summary():
    if not data:
        print("No data to summarize.\n")
        return
    print("Data Summary:")
    print("Count:", len(data))
    print("Sum:", sum(data))
    print("Max:", max(data))
    print("Min:", min(data))
    print("Average:", sum(data) / len(data))

def display_2d_data_summary():
    flat_data = [num for row in data_2d for num in row]
    if not flat_data:
        print("No 2D data to summarize.\n")
        return
    print("2D Data Summary:")
    print("Count:", len(flat_data))
    print("Sum:", sum(flat_data))
    print("Max:", max(flat_data))
    print("Min:", min(flat_data))
    print("Average:", sum(flat_data) / len(flat_data))

def calculate_factorial():
    import math
    num = int(input("Enter a number: "))
    print("Factorial is:", math.factorial(num))

def filter_data():
    if not data:
        print("No data to filter.")
        return
    filtered = list(filter(lambda x: x > 10, data))
    print("Filtered data (greater than 10):", filtered)

def sort_data():
    if not data:
        print("No data to sort.")
        return
    print("Sorted data:", sorted(data))

def display_dataset():
    print("Current dataset:", data)

# MAIN MENU
while True:
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("Main Menu:")
    print("1. Input data")
    print("2. Display data summary (built-in function)")
    print("3. Calculate factorial")
    print("4. Filter data (lambda function)")
    print("5. Sort data")
    print("6. Display dataset")
    print("7. Exit program")

    try:
        choice = int(input("Please enter your choice: "))
        match choice:
            case 1:
                print("Input Data")
                print("1. 1D array")
                print("2. 2D array")
                c = int(input("Enter your sub choice: "))
                if c == 1:
                    array = input_array()
                    print("Stored 1D array:", array)
                elif c == 2:
                    array = input_2d_array()
                    print("Stored 2D array:", array)
                else:
                    print("Invalid sub choice!")
            case 2:
                print("Display Data Summary")
                print("1. 1D array")
                print("2. 2D array")
                c = int(input("Enter your sub choice: "))
                if c == 1:
                    display_data_summary()
                elif c == 2:
                    display_2d_data_summary()
                else:
                    print("Invalid sub choice!")
            case 3:
                calculate_factorial()
            case 4:
                filter_data()
            case 5:
                sort_data()
            case 6:
                display_dataset()
            case 7:
                print("Exiting program. Thank you!")
                break
            case _:
                print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number.")






