import numpy as np

class NumpyArrayAnalyzer:
    def __init__(self):
        self.array = None
        self.original_array = None

    def _get_input_array(self, prompt, shape=None):
        try:
            data = list(map(int, input(prompt).split()))
            if shape:
                return np.array(data).reshape(*shape)
            return np.array(data)
        except Exception as e:
            print("Error:", e)
            return None

    def create_array(self, dims):
        try:
            shape = tuple(int(input(f"Enter {x} dimension: ")) for x in ['rows', 'columns'][:dims] + (['layers'] if dims == 3 else []))
            total = np.prod(shape)
            arr = self._get_input_array(f"Enter {total} elements: ", shape)
            if arr is not None and arr.size == total:
                self.original_array = arr
                self.array = arr.copy()
                print(f"{dims}D array created:\n", arr)
        except:
            print("Invalid input.")

    def stat_ops(self, op):
        if self.array is not None:
            func = {"mean": np.mean, "median": np.median, "std": np.std, "var": np.var, "sum": np.sum}[op]
            target = self.original_array if op == "sum" else self.array
            print(f"{op.title()}: {func(target)}")

    def sort_array(self):
        if self.original_array is not None:
            print("Sorted array:\n", np.sort(self.original_array, axis=None))

    def filter_even(self):
        if self.array is not None:
            print("Even numbers:", self.array[self.array % 2 == 0])

    def search_value(self):
        if self.original_array is not None:
            try:
                val = int(input("Enter value to search: "))
                print("Found at:", np.where(self.original_array == val))
            except:
                print("Invalid value.")

    def split_array(self):
        if self.original_array is not None:
            try:
                n = int(input("Number of splits: "))
                for i, part in enumerate(np.array_split(self.original_array, n)):
                    print(f"Part {i+1}:\n{part}")
            except:
                print("Invalid number.")

    def combine_array(self, mode):
        if self.original_array is None:
            print("Create array first.")
            return
        arr = self._get_input_array("Enter elements to combine: ", self.original_array.shape)
        if arr is not None:
            combined = np.vstack((self.original_array, arr)) if mode == "v" else np.hstack((self.original_array, arr))
            print(f"Combined array:\n{combined}")

    def arithmetic(self, op):
        if self.array is None:
            print("Create array first.")
            return
        arr = self._get_input_array("Enter elements: ", self.array.shape)
        if arr is not None:
            result = {"add": self.array + arr, "sub": self.array - arr, "mul": self.array * arr, "div": self.array / arr}[op]
            print(f"{op.title()} result:\n{result}")


# ===================== MENU DRIVER =====================
def menu():
    ca = NumpyArrayAnalyzer()

    def main_menu():
        print("\n1. Create array\n2. Math ops\n3. Combine/Split\n4. Search/Sort/Filter\n5. Stats\n6. Exit")
        return input("Choose: ")

    def create_menu():
        sub_options = { "1": 1, "2": 2, "3": 3 }
        while (c := input("\n1. 1D\n2. 2D\n3. 3D\n4. Back\nChoose: ")) != "4":
            if c in sub_options: ca.create_array(sub_options[c])

    def math_menu():
        while (c := input("\n1.Add 2.Sub 3.Mul 4.Div 5.Back\nChoose: ")) != "5":
            ops = { "1": "add", "2": "sub", "3": "mul", "4": "div" }
            if c in ops: ca.arithmetic(ops[c])

    def combine_split_menu():
        while (c := input("\n1.Combine\n2.Split\n3.Back\nChoose: ")) != "3":
            if c == "1":
                mode = input("1.Vertical\n2.Horizontal\nChoose: ")
                ca.combine_array("v" if mode == "1" else "h")
            elif c == "2":
                ca.split_array()

    def search_sort_filter_menu():
        while (c := input("\n1.Search\n2.Sort\n3.Filter even\n4.Back\nChoose: ")) != "4":
            if c == "1": ca.search_value()
            elif c == "2": ca.sort_array()
            elif c == "3": ca.filter_even()

    def stats_menu():
        while (c := input("\n1.Sum\n2.Mean\n3.Median\n4.Std\n5.Var\n6.Back\nChoose: ")) != "6":
            ops = { "1": "sum", "2": "mean", "3": "median", "4": "std", "5": "var" }
            if c in ops: ca.stat_ops(ops[c])

    print("Welcome to NumPy Analyzer!")
    actions = {
        "1": create_menu,
        "2": math_menu,
        "3": combine_split_menu,
        "4": search_sort_filter_menu,
        "5": stats_menu
    }

    while True:
        choice = main_menu()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()

menu()
