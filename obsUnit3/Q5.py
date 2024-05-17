#   Q5
def maxFinder():

    numList = []
    while True:

        UserInput = str(input("Enter a number (press enter to end): "))
        if UserInput == "":
            break
        else:
            numList.append(int(UserInput))

    print(f"The largest number you enter is: {max(numList)}")

maxFinder()
