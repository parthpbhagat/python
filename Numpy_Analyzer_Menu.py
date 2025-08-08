# NumPy Array Analyzer - Menu Driven Program

import ca  # Assuming 'ca' is a custom module with all required functions

print("Welcome to the NumPy Analyzer!")
print("=" * 40)

# Start the main loop
while True:
    # Display main menu options
    print("Select an option:")
    print("1. Create NumPy array")
    print("2. Perform mathematical operation")
    print("3. Combine or split array")
    print("4. Search, sort, or filter array")
    print("5. Compute aggregate and statistics")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    # Main menu switch-case structure
    match option:
        case 1:
            # Sub-menu for creating arrays
            while True:
                print("Select the type of array to create:")
                print("1. 1D array")
                print("2. 2D array")
                print("3. 3D array")
                print("4. Go to main menu")

                option = int(input("Enter your option: "))

                match option:
                    case 1:
                        ca.create_1D_array()  # Create 1D array
                    case 2:
                        ca.create_2D_array()  # Create 2D array
                    case 3:
                        ca.create_3D_array()  # Create 3D array
                    case 4:
                        break  # Exit to main menu

        case 2:
            # Sub-menu for performing arithmetic operations
            while True:
                print("Perform mathematical operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Go to main menu")

                option = int(input("Enter your option: "))

                match option:
                    case 1:
                        ca.addition_array()  # Perform addition
                    case 2:
                        ca.subtraction_array()  # Perform subtraction
                    case 3:
                        ca.multiplication_array()  # Perform multiplication
                    case 4:
                        ca.divided_array()  # Perform division
                    case 5:
                        break  # Exit to main menu

        case 3:
            # Sub-menu for combining or splitting arrays
            while True:
                print("Combine and split array:")
                print("1. Combine the array")
                print("2. Split the array")
                print("3. Go to main menu")

                option = int(input("Enter your option: "))

                match option:
                    case 1:
                        while True:
                            print("Combine the array:")
                            print("1. Vertically concatenate")
                            print("2. Horizontally concatenate")
                            print("3. Go to main menu")

                            option = int(input("Enter your option: "))

                            match option:
                                case 1:
                                    ca.combine_array_verticaly()  # Vertical concatenation
                                case 2:
                                    ca.combine_array_hirizentaly()  # Horizontal concatenation
                                case 3:
                                    break  # Exit to previous menu
                    case 2:
                        print("Split the array:")
                        ca.split_the_array()  # Split the array
                    case 3:
                        break  # Exit to main menu

        case 4:
            # Sub-menu for searching, sorting, and filtering
            while True:
                print("Search, sort, and filter array:")
                print("1. Search the array")
                print("2. Sort the array")
                print("3. Filter the array")
                print("4. Go to main menu")

                option = int(input("Enter your option: "))

                match option:
                    case 1:
                        print("Search the array:")
                        ca.search_the_array()  # Search operation
                    case 2:
                        print("Sort the array:")
                        ca.sort_the_array()  # Sort operation
                    case 3:
                        print("Filter the array:")
                        ca.filter_the_array()  # Filter operation
                    case 4:
                        break  # Exit to main menu

        case 5:
            # Sub-menu for computing aggregate statistics
            while True:
                print("Compute aggregate and statistics:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard deviation")
                print("5. Variance")
                print("6. Go to main menu")

                option = int(input("Enter your choice: "))

                match option:
                    case 1:
                        print("Sum")
                        ca.sum_of_the_array()  # Compute sum
                    case 2:
                        print("Mean")
                        ca.mean_array()  # Compute mean
                    case 3:
                        print("Median")
                        ca.median_array()  # Compute median
                    case 4:
                        print("Standard deviation")
                        ca.standard_deviation_array()  # Compute standard deviation
                    case 5:
                        print("Variance")
                        ca.variance_array()  # Compute variance
                    case 6:
                        break  # Exit to main menu

        case 6:
            # Exit the program
            print("Thank you for using NumPy Analyzer! Goodbye.")
            break
