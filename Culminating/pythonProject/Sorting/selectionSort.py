def s_Sort(Nums):
    for i in range(len(Nums)):
        lowest_value = i
        for ii in range(i+1, len(Nums)):
            if Nums[ii] < Nums[lowest_value]:
                lowest_value = ii
        Nums[i], Nums[lowest_value] = Nums[lowest_value], Nums[i]
    return Nums

def input_Values():
    numbers = []
    while True:
        try:
            user_Input = input("Enter a number (or enter 'DONE' to finish): ")
            if user_Input.upper() == "DONE":
                break
            number = int(user_Input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer!")
    return numbers

def main():
    Nums = input_Values()
    Final = s_Sort(Nums)
    print(f"Sorted numbers are: {Final}")
main()
