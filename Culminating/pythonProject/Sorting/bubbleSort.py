def b_Sort(numbers): #  Sorting algorithm
    for i in range(len(numbers)):
        for ii in range(len(numbers) -1):
            if numbers[ii] > numbers[ii+1]:
                numbers[ii], numbers[ii+1] = numbers[ii+1], numbers[ii]
    return numbers

def input_Values():  # Take input and error handling
    Nums=[]
    while True:
        try:
            user_Input = input("Please enter a number (or enter 'DONE' to finish): ")
            if user_Input.upper() == "DONE":
                break
            UserInput = int(user_Input)
            Nums.append(UserInput)
        except ValueError:
            print("Please enter a valid integer!")
    return Nums

def main():  # Run code
    Nums = input_Values()
    Final = b_Sort(Nums)
    print(f"Sorted numbers are: {Final}")
main()
