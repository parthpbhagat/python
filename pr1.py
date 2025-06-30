               #pr1
print("Welcome to the interactive personal data collector!")

# Collect user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert age to integer
height = input("Enter your height: ")
favorite_number = input("Enter your favorite number: ")

# Calculate birth year
current_year = 2025
birth_year = current_year - age

print(f"name:{name},  type:{(type(name))},   memory address:{(id(name))}") #used type() and id()function
print(f"age:{age},  type:{(type(age))},   memory address:{(id(age))}") #used type() and id()function
print(f"name:{height},  type:{(type(height))},   memory address:{(id(height))}") #used type() and id()function
print(f"name:{favorite_number},  type:{(type(favorite_number))},   memory address:{(id(favorite_number))}") #used type() and id()function


# Display result
print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")
print("Thank you for using the personal Data collector.Goodbye!")
