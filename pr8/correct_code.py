import numpy as np


class NumpyArrayAnalyzer:
    def __init__(self):
        self.array = None
        self.original_array = None

    def create_1D_array(self):
        try:
            elements = input("Enter elements (space-separated): ")
            self.array = np.array(list(map(int, elements.split())))
            print("1D array created:", self.array)
        except ValueError:
            print("Error: Please enter valid integers.")

    def create_2D_array(self):
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements = input(f"Enter {rows * cols} elements (space-separated): ")
            data = list(map(int, elements.split()))
            if len(data) != rows * cols:
                print("Error: Incorrect number of elements.")
                return
            self.original_array = np.array(data).reshape(rows, cols)
            self.array = self.original_array  # Set array reference
            print("2D array created:\n", self.original_array)
        except ValueError:
            print("Error: Please enter valid integers.")

    def create_3D_array(self):
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            layers = int(input("Enter number of layers: "))
            total = rows * cols * layers
            elements = input(f"Enter {total} elements (space-separated): ")
            data = list(map(int, elements.split()))
            if len(data) != total:
                print(f"Error: You must enter exactly {total} elements.")
                return
            self.array = np.array(data).reshape(rows, cols, layers)
            print("3D array created:\n", self.array)
        except ValueError:
            print("Error: Please enter valid integers.")

    def mean(self):
        if self.array is not None:
            print("Mean:", np.mean(self.array))

    def median(self):
        if self.array is not None:
            print("Median:", np.median(self.array))

    def std_dev(self):
        if self.array is not None:
            print("Standard deviation:", np.std(self.array))

    def variance(self):
        if self.array is not None:
            print("Variance:", np.var(self.array))

    def sum(self):
        if self.original_array is not None:
            print("Sum:", np.sum(self.original_array))

    def sort(self):
        if self.original_array is not None:
            print("Sorted array:\n", np.sort(self.original_array, axis=None))

    def filter_even(self):
        if self.array is not None:
            print("Even numbers:", self.array[self.array % 2 == 0])

    def search(self):
        if self.original_array is not None:
            try:
                value = int(input("Enter a value to search: "))
                result = np.where(self.original_array == value)
                print(f"Value found at: {result}")
            except ValueError:
                print("Please enter a valid integer.")

    def split_array(self):
        if self.original_array is not None:
            try:
                num = int(input("Enter the number of splits: "))
                splits = np.array_split(self.original_array, num)
                print("Array split into:")
                for i, s in enumerate(splits):
                    print(f"Part {i + 1}:")
                    print(s)
            except ValueError:
                print("Please enter a valid number.")

    def combine_vertical(self):
        try:
            elements = input("Enter elements to stack vertically (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.original_array.shape)
            combined = np.vstack((self.original_array, new_array))
            print("Vertically combined array:\n", combined)
        except Exception as e:
            print("Error:", e)

    def combine_horizontal(self):
        try:
            elements = input("Enter elements to stack horizontally (space-separated): ")
            new_array = np.array(list(map(int, elements.split()))).reshape(self.original_array.shape)
            combined = np.hstack((self.original_array, new_array))
            print("Horizontally combined array:\n", combined)
        except Exception as e:
            print("Error:", e)
            
    def addition_array(self):
        try:
            elements = input("Enter elements to add (space-separated): ")
            new_array = np.array(list(map(int, elements.split())))
            if new_array.shape != self.array.shape:
                print("Error: Arrays must be the same shape.")
                return
            result = self.array + new_array
            print("Addition result:", result)
        except Exception as e:
            print("Error:", e)

    def subtraction_array(self):
        try:
            elements = input("Enter elements to subtract (space-separated): ")
            new_array = np.array(list(map(int, elements.split())))
            if new_array.shape != self.array.shape:
                print("Error: Arrays must be the same shape.")
                return
            result = self.array - new_array
            print("Subtraction result:", result)
        except Exception as e:
            print("Error:", e)

    def multiplication_array(self):
        try:
            elements = input("Enter elements to multiply (space-separated): ")
            new_array = np.array(list(map(int, elements.split())))
            if new_array.shape != self.array.shape:
                print("Error: Arrays must be the same shape.")
                return
            result = self.array * new_array
            print("Multiplication result:", result)
        except Exception as e:
            print("Error:", e)

    def divided_array(self):
        try:
            elements = input("Enter elements to divide (space-separated): ")
            new_array = np.array(list(map(int, elements.split())))
            if new_array.shape != self.array.shape:
                print("Error: Arrays must be the same shape.")
                return
            result = self.array / new_array
            print("Division result:", result)
        except Exception as e:
            print("Error:", e)

            
ca = NumpyArrayAnalyzer()

print("Welcome to the NumPy Analyzer!")
print("=" * 40)
while True:
    print("Select an sub_option:")
    print("1. Create NumPy array")
    print("2. Perform mathematical operation")
    print("3. Combine or split array")
    print("4. Search, sort, or filter array")
    print("5. Compute aggregate and statistics")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    match option:
        case 1:
            while True:
                print("Select the type of array to create:")
                print("1. 1D array")
                print("2. 2D array")
                print("3. 3D array")
                print("4. Go to main menu")

                sub_option = int(input("Enter your sub_option: "))

                match sub_option:
                    case 1:
                        ca.create_1D_array()
                    case 2:
                        ca.create_2D_array()
                    case 3:
                        ca.create_3D_array()
                    case 4:
                        break
        case 2:
            while True:
                print("Perform mathematical operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Go to main menu")

                sub_option = int(input("Enter your sub_option: "))

                match sub_option:
                    case 1:
                        ca.addition_array()
                    case 2:
                        ca.subtraction_array()
                    case 3:
                        ca.multiplication_array()
                    case 4:
                        ca.divided_array()
                    case 5:
                        break

        case 3:
            while True:
                print("Combine and split array:")
                print("1. Combine the array")
                print("2. Split the array")
                print("3. Go to main menu")

                sub_option = int(input("Enter your sub_option: "))

                match sub_option:
                    case 1:
                        while True:
                            print("Combine the array:")
                            print("1. Vertically concatenate")
                            print("2. Horizontally concatenate")
                            print("3. Go to main menu")

                            sub_option = int(input("Enter your sub_option: "))

                            match sub_option:
                                case 1:
                                    ca.combine_vertical()
                                case 2:
                                    ca.combine_horizontal()
                                case 3:
                                    break
                    case 2:
                        print("Split the array:")
                        ca.split_array()
                    case 3:
                        break

        case 4:
            while True:
                print("Search, sort, and filter array:")
                print("1. Search the array")
                print("2. Sort the array")
                print("3. Filter the array")
                print("4. Go to main menu")

                sub_option = int(input("Enter your sub_option: "))

                match sub_option:
                    case 1:
                        print("Search the array:")
                        ca.search()
                    case 2:
                        print("Sort the array:")
                        ca.sort()
                    case 3:
                        print("Filter the array:")
                        ca.filter_even()
                    case 4:
                        break
        case 5:
            while True:
                print("Compute aggregate and statistics:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard deviation")
                print("5. Variance")
                print("6. Go to main menu")

                sub_option = int(input("Enter your choice: "))

                match sub_option:
                    case 1:
                        print("Sum")
                        ca.sum()
                    case 2:
                        print("Mean")
                        ca.mean()
                    case 3:
                        print("Median")
                        ca.median()
                    case 4:
                        print("Standard deviation")
                        ca.std_dev()
                    case 5:
                        print("Variance")
                        ca.variance()
                    case 6:
                        break

        case 6:
            print("Thank you for using NumPy Analyzer! Goodbye.")
            break
# def switch_main_menu(choice, ca):
#     match choice:
#         case '1':
#             sub = input("1. 1D Array\n2. 2D Array\n3. 3D Array\nChoose an sub_option: ")
#             match sub:
#                 case '1': ca.create_1D_array()
#                 case '2': ca.create_2D_array()
#                 case '3': ca.create_3D_array()
#                 case _: print("Invalid sub-sub_option.")

#         case '2':
#             sub = input("1. Mean\n2. Median\n3. Std Dev\n4. Variance\n5. Sum\nChoose an sub_option: ")
#             match sub:
#                 case '1': ca.mean()
#                 case '2': ca.median()
#                 case '3': ca.std_dev()
#                 case '4': ca.variance()
#                 case '5': ca.sum()
#                 case _: print("Invalid sub-sub_option.")

#         case '3':
#             sub = input("1. Vertical Combine\n2. Horizontal Combine\n3. Split\nChoose an sub_option: ")
#             match sub:
#                 case '1': ca.combine_vertical()
#                 case '2': ca.combine_horizontal()
#                 case '3': ca.split_array()
#                 case _: print("Invalid sub-sub_option.")

#         case '4':
#             sub = input("1. Search\n2. Sort\n3. Filter Even\nChoose an sub_option: ")
#             match sub:
#                 case '1': ca.search()
#                 case '2': ca.sort()
#                 case '3': ca.filter_even()
#                 case _: print("Invalid sub-sub_option.")

#         case '5':
#             ca.mean()
#             ca.median()
#             ca.std_dev()
#             ca.variance()
#             ca.sum()

#         case '6':
#             print("Exiting. Goodbye!")
#             return False

#         case _:
#             print("Invalid choice. Please try again.")
#     return True


# if __name__ == "__main__":
#     ca = NumpyArrayAnalyzer()
#     while True:
#         print("\nMain Menu:")
#         print("1. Create Arrays")
#         print("2. Perform Math Operations")
#         print("3. Combine/Split Arrays")
#         print("4. Search/Sort/Filter")
#         print("5. Statistics")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#         if not switch_main_menu(choice, ca):
#             break