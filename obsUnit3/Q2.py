# Q2 quadratic equation
import math
def Calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if b == 0:
        print("Cannot divide by zero")
    elif (4*a*b) < 0:
        print("Can not square root a negative answer")

    else:

        Solution1 = ((b*b) + math.sqrt(4*a*c)) / (2*b)
        Solution2 = ((b*b) - math.sqrt(4*a*c)) / (2*b)

        print(f"The solutions are {Solution1} and {Solution2}")

Calculator()