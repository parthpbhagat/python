import math

class MathematicalOperations:
    def factorial(self):
        number = int(input("Enter your number: "))
        result = math.factorial(number)
        print(f"{number} factorial is {result}")

    def trigonometric_calculation(self):
        angle_degree = int(input("Enter angle in degrees: "))
        angle_radians = math.radians(angle_degree)
        print(f"sin({angle_degree}) = {math.sin(angle_radians)}")
        print(f"cos({angle_degree}) = {math.cos(angle_radians)}")
        print(f"tan({angle_degree}) = {math.tan(angle_radians)}")

    def area_of_triangle(self):
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))
        print("Area of triangle:", 0.5 * base * height)

    def area_of_square(self):
        side = float(input("Enter side of square: "))
        print("Area of square:", side * side)

    def area_of_rectangle(self):
        width = float(input("Enter width: "))
        length = float(input("Enter length: "))
        print("Area of rectangle:", width * length)

    def area_of_circle(self):
        radius = float(input("Enter radius: "))
        print("Area of circle:", math.pi * radius ** 2)

    def compound_interest(self):
        principal = float(input("Enter principal: "))
        rate = float(input("Enter rate (%): "))
        time_period = float(input("Enter time (in years): "))
        amount = principal * (1 + rate / 100) ** time_period
        ci = amount - principal
        print(f"Compound Interest = {ci:.2f}")
