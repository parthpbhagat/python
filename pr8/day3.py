import numpy as np

class NumpyArrayAnalyzer:
    def __init__(self):
        self.array = None
        self.original_array = None

    def create_1d_array(self):
        try:
            elements = int(input("Enter the number of elements: "))
            elements_list = [int(input(f"Enter element {i+1}: ")) for i in range(elements)]
            self.array = np.array(elements_list)
            self.original_array = self.array.copy()
            print("1D Array created:", self.array)
        except Exception as e:
            print("Error:", e)

    def create_2d_array(self):
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements_list = [int(input(f"Enter element {i+1}: ")) for i in range(rows * cols)]
            self.array = np.array(elements_list).reshape(rows, cols)
            self.original_array = self.array.copy()
            print("2D Array created:", self.array)
        except Exception as e:
            print("Error:", e)

    def create_3d_array(self):
        try:
            rows = int(input("Enter first dimension: "))
            cols = int(input("Enter second dimension: "))
            depth = int(input("Enter third dimension: "))
            total = rows * cols * depth
            elements_list = [int(input(f"Enter element {i+1}: ")) for i in range(total)]
            self.array = np.array(elements_list).reshape(rows, cols, depth)
            self.original_array = self.array.copy()
            print("3D Array created:", self.array)
        except Exception as e:
            print("Error:", e)

    def mean_array(self):
        try:
            print("Mean value:", np.mean(self.original_array))
        except Exception as e:
            print("Error:", e)

    def median_array(self):
        try:
            print("Median value:", np.median(self.original_array))
        except Exception as e:
            print("Error:", e)

    def std_deviation(self):
        try:
            print("Standard Deviation:", np.std(self.original_array))
        except Exception as e:
            print("Error:", e)

    def variance_array(self):
        try:
            print("Variance:", np.var(self.original_array))
        except Exception as e:
            print("Error:", e)

    def search_element(self):
        try:
            value = int(input("Enter value to search: "))
            result = np.where(self.original_array == value)
            print("Found at indices:", result)
        except Exception as e:
            print("Error:", e)

    def filter_even(self):
        try:
            filtered = self.original_array[self.original_array % 2 == 0]
            print("Even values:", filtered)
        except Exception as e:
            print("Error:", e)

    def split_array(self):
        try:
            num_splits = int(input("Enter number of splits: "))
            result = np.array_split(self.original_array, num_splits, axis=0)
            print("Split arrays:", result)
        except Exception as e:
            print("Error:", e)

    def menu(self):
        while True:
            print("""
            ===== NumPy Array Analyzer =====
            1. Create 1D Array
            2. Create 2D Array
            3. Create 3D Array
            4. Calculate Mean
            5. Calculate Median
            6. Standard Deviation
            7. Variance
            8. Search Element
            9. Filter Even Elements
            10. Split Array
            11. Exit
            """)
            choice = input("Enter your choice: ")
            match choice:
                case "1": self.create_1d_array()
                case "2": self.create_2d_array()
                case "3": self.create_3d_array()
                case "4": self.mean_array()
                case "5": self.median_array()
                case "6": self.std_deviation()
                case "7": self.variance_array()
                case "8": self.search_element()
                case "9": self.filter_even()
                case "10": self.split_array()
                case "11": print("Exiting program..."); break
                case _: print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = NumpyArrayAnalyzer()
    app.menu()
