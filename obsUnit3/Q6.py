#   Q6 Fine calculator
def FineCalculator():

    Fine = 0
    speedLimit = int(input("Enter speed limit: "))
    carSpeedLimit = int(input("Enter car speed: "))

    if carSpeedLimit > speedLimit:
        if carSpeedLimit > 90:
            Fine = 50+(carSpeedLimit-speedLimit)*5 + 200
        else:
            Fine = 50+(carSpeedLimit-speedLimit)*5

        print(f"The fine will be {Fine} dollars")

    else:
        print("You are not speeding")

FineCalculator()