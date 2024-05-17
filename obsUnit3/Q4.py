def maxFinder():

    # Define the largeNum before running the loop
    UserInput = str(input("Enter a number (press enter to end): "))
    largeNum = int(UserInput)

    while True:

        UserInput = str(input("Enter a number (press enter to end): "))
        if UserInput == "":
            break
        else:
            if largeNum < int(UserInput):
                largeNum = int(UserInput)

    print(f"The largest number you enter is: {largeNum}")

maxFinder()
