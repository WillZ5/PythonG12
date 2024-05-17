#   Q9 Average calculator sentinel loop
def calculator():
    counter = 0
    Num = 0
    while True:
        UserInput = str(input("Please enter a number (press enter to quit): "))
        if UserInput == "":
            break
        else:
            Num = Num + int(UserInput)
            counter = counter + 1

    print(f"The average is: {Num/counter}")

calculator()