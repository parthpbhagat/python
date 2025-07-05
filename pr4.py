

#                  PR 4

data = []
def input_array():
    global data
    data = list(map(int, input("Enter elements separated by space: ").split()))
    return data


def display_data_summary():
    print("data summary:")
    print("count: ", len(data))
    print("sum of all elements: ", sum(data))
    print("maximum: ", max(data))
    print("minimum: ", min(data))
    print("avrage: ", sum(data) / len(data))


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
            array = input_array()
            print("stored 1d array:", array)
        case 2:
            display_data_summary()
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
