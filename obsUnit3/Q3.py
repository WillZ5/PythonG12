# Q3 quadratic equation with exception handling
import math
def Calculator():

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    try:

        Solution1 = ((b*b) + math.sqrt(4*a*c)) / (2*b)
        Solution2 = ((b*b) - math.sqrt(4*a*c)) / (2*b)

        print(f"The solutions are {Solution1} and {Solution2}")

    except ValueError:
        print("Invalid input error!")
    except ZeroDivisionError:
        print("Division by zero error!")
    except TypeError:
        print("Type Error error!")

Calculator()