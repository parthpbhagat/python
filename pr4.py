#                  PR 4

data = []
data_2d = []


def input_array():
    global data
    list1 = input("element of array: ").split()
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
    print("data summary:")
    print("count: ", len(data))
    print("sum of all elements: ", sum(data))
    print("maximum: ", max(data))
    print("minimum: ", min(data))
    print("avrage: ", sum(data) / len(data))


def display_2d_data_summary():
    flat_data = []
    for row in data_2d:
        for num in row:
            flat_data.append(num)
    print("data summary:")
    print("count: ", len(flat_data))
    print("sum of all elements: ", sum(flat_data))
    print("maximum: ", max(flat_data))
    print("minimum: ", min(flat_data))
    print("avrage: ", sum(flat_data) / len(flat_data))


def calclulate_factorial():
    import math

    num = int(input("Enter a number: "))
    print("Factorial is:", math.factorial(num))


def filter_data():
    filtered = list(filter(lambda x: x > 10, data))
    print("Filtered data (greater than 10):", filtered)
    return


def short_data():
    print("sorted data:", sorted(data))


def display_dataset():
    print("curent dataset: ", (data))


while True:
    print("Welcome to the data analyazer and tranforer  programe")
    print("main menu:")
    print("1. input data")
    print("2. display data summery(built in function)")
    print("3. calculate factorial (recursion)")
    print("4. filter data(lambda function)")
    print("5. short data")
    print("6. display dataset")
    print("7. exit programe")

    choice = int(input("plase enter your choice: "))
    match choice:
        case 1:
            print("input data")
            print("1. 1d array")
            print("2. 2d array")
            c = int(input("enter your sub choice: "))
            if c == 1:
                array = input_array()
                print("stored 1d array:", array)
            elif c == 2:
                array = input_2d_array()
                print("stored 2d array:", array)
                print("invalide sub choice! ")
        case 2:
            print("display data summary: ")
            print("1. 1d array")
            print("2. 2d array")
            c = int(input("enter your sub choice: "))
            if c == 1:
                display_data_summary()
            elif c == 2:
                display_2d_data_summary()
            else:
                print("invalide sub choice! ")
        case 3:
            calclulate_factorial()
        case 4:
            filter_data()
        case 5:
            short_data()
        case 6:
            display_dataset()
        case 7:
            print("exit programe")
            break
        case _:
            print("invalide choice! ")





