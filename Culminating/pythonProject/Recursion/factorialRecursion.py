def factorial(InputNum):  # Factorial Calculator
    if InputNum == 0 or InputNum == 1:
        return 1
    else:
        return InputNum * factorial (InputNum - 1)

try:  # Error Handling
    InputNum = int(input("Please a a number: "))
    if InputNum < 0:
        print(f"\"{InputNum}\" is a not valid input! Please enter a positive integer.")
    else:
        print(f"The factorial of {InputNum} is:", factorial(InputNum))
except ValueError:
    print("Input Invalid! You must be a positive integer.")
