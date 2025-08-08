import numpy as np

class CreateArray:
    def __init__(self):
        pass

    def create_1D_array(self):
        try:
            element = input("Enter the elements of the array, separated by space: ")
            elements_list = list(map(int, element.split()))
            self.array = np.array(elements_list)
            print("Array created successfully")
            print("1D array:", self.array)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def create_2D_array(self):
        try:
            self.rows = int(input("Enter the number of rows: "))
            self.columns = int(input("Enter the number of columns: "))
            total_elements = self.rows * self.columns
            element = input(f"Enter {total_elements} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            if len(elements_list) != total_elements:
                print("Error: Incorrect number of elements.")
                return
            self.original_array = np.array(elements_list).reshape(self.rows, self.columns)
            print("2D array created successfully")
            print("2D array:\n", self.original_array)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def addition_array(self):
        try:
            element = input(f"Enter {self.rows * self.columns} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            second_array = np.array(elements_list).reshape(self.rows, self.columns)
            result = self.original_array + second_array
            print("Result of addition:\n", result)
        except Exception as e:
            print(f"Error: {e}")

    def subtraction_array(self):
        try:
            element = input(f"Enter {self.rows * self.columns} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            second_array = np.array(elements_list).reshape(self.rows, self.columns)
            result = self.original_array - second_array
            print("Result of subtraction:\n", result)
        except Exception as e:
            print(f"Error: {e}")

    def multiplication_array(self):
        try:
            element = input(f"Enter {self.rows * self.columns} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            second_array = np.array(elements_list).reshape(self.rows, self.columns)
            result = self.original_array * second_array
            print("Result of multiplication:\n", result)
        except Exception as e:
            print(f"Error: {e}")

    def divided_array(self):
        try:
            element = input(f"Enter {self.rows * self.columns} elements separated by space: ")
            elements_list = list(map(float, element.split()))
            second_array = np.array(elements_list).reshape(self.rows, self.columns)
            result = self.original_array / second_array
            print("Result of division:\n", result)
        except Exception as e:
            print(f"Error: {e}")

    def combine_array_vertically(self):
        try:
            element = input(f"Enter {self.rows * self.columns} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            second_array = np.array(elements_list).reshape(self.rows, self.columns)
            combined = np.concatenate((self.original_array, second_array), axis=0)
            print("Combined array (vertical):\n", combined)
        except Exception as e:
            print(f"Error: {e}")

    def combine_array_horizontally(self):
        try:
            element = input(f"Enter {self.rows * self.columns} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            second_array = np.array(elements_list).reshape(self.rows, self.columns)
            combined = np.concatenate((self.original_array, second_array), axis=1)
            print("Combined array (horizontal):\n", combined)
        except Exception as e:
            print(f"Error: {e}")

    def sort_the_array(self):
        try:
            sorted_array = np.sort(self.original_array, axis=None)
            print("Sorted array (flattened):\n", sorted_array)
        except Exception as e:
            print(f"Error: {e}")

    def sum_of_the_array(self):
        try:
            total = np.sum(self.original_array)
            print("Sum of array elements:", total)
        except Exception as e:
            print(f"Error: {e}")

    def create_3D_array(self):
        try:
            self.rows = int(input("Enter number of rows: "))
            self.columns = int(input("Enter number of columns: "))
            total_elements = self.rows * self.columns * 2
            element = input(f"Enter {total_elements} elements separated by space: ")
            elements_list = list(map(int, element.split()))
            if len(elements_list) != total_elements:
                print(f"Error: You need to enter exactly {total_elements} elements.")
                return
            array = np.array(elements_list).reshape(self.rows, self.columns, 2)
            print("3D array created successfully:\n", array)
        except Exception as e:
            print(f"Error: {e}")
            
ca = CreateArray()

print("welcome to the numpy anylizer!")
print("=" * 40)
while True:
    print("select an sub_option: ")
    print("1. create numpy array")
    print("2. parform mathemeticle oprection")
    print("3. combine or split array")
    print("4. search, sort, or filtter array")
    print("5. compute aggrigate and statastic")
    print("6. exit")

    sub_option = int(input("enter your choice: "))

    match sub_option:
        case 1:
            while True:
                print("select the type of array to create: ")
                print("1. 1D array")
                print("2. 2D array")
                print("3. 3D array")
                print("4. Go to main menu")

                sub_option = int(input("enter your sub_option: "))

                match sub_option:
                    case 1:
                        ca.create_1D_array()
                    case 2:
                        ca.create_2D_array()
                    case 3:
                        ca.create_3D_array()
                    case 4:
                        pass
                        break
        case 2:
            while True:
                print("Perform mathemetical oprection: ")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. division")
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
                        pass
                        break

        case 3:
            while True:
                print("combine and split array")
                print("1. combine the array")
                print("2. split the array")
                print("3. Go to the main menu")

                sub_option = int(input("Enter your sub_option: "))

                match sub_option:
                    case 1:
                        while True:

                            print("Combine the array")
                            print("1. vertical Concatinate")
                            print("2. horizentaly Concatinate")
                            print("3. Go to main menu")

                            sub_option = int(input("Enter your sub_option: "))

                            match sub_option:
                                case 1:
                                    ca.combine_array_horizontally()
                                case 2:
                                    ca.combine_array_vertically()
                                case 3:
                                    pass
                                    break

                    case 2:
                        print("split the array: ")

                    case 3:
                        pass
                        break


        case 4:
            while True:
                print("search, sort, and filtter array")
                print("1. search the array")
                print("2. sort the array")
                print("3. filter the array")
                print("4. Go to the main menu")

                sub_option = int(input("enter your sub_option: "))

                match sub_option:
                    case 1:
                        pass
                    case 2:
                        print("sort the array: ")
                        ca.sort_the_array()
                    case 3:
                        pass
                    case 4:
                        pass
                        break
        case 5:
            while True:

                print("compute aggrigate and statastic")
                print("1. sum")
                print("2. mean")
                print("3. midian")
                print("4. standerd deveaction ")
                print("5. veriance")
                print("6. Go to main menu")

                sub_option = int(input("Enter your choice: "))

                match sub_option:
                    case 1:
                        ca.sum_of_the_array()
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                        break


        case 6:
            print("Thank you for using numpy anylizer! Goodby")
            break
