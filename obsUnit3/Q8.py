#   Q8 Average calculator interactive loop
def calculator():
    counter = 0
    Num = 0

    while True:
        UserInput = str(input("Do you want to enter a new number? (yes or no): "))

        if UserInput == "yes":
            Num = Num  + int(input("Enter a number: "))
            counter = counter + 1
        else:
            print(f"The average is: {Num / counter}")
            break

calculator()