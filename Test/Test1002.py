# This is a Python program that can use simultaneous assignment to swap two variables that user input

# Print the user instructions of the program.
print("This program will use the simultaneous assignment to swap x and y variables.")

# Define the function for the program that can swap two variables.
def SimulSwap ():

    # Get the input from the users of the x value.
    x = eval(input("Please input the value of x： "))

    # Get the input from the users of the y value.
    y = eval(input("Please input the value of y： "))

    # Use the simultaneous assignment to swap the value of x and y.
    x, y = y, x

    # Print the output of the new value of x and new value of y.
    print("Now x is", x, "and y is", y)

# Call the function.
SimulSwap()
