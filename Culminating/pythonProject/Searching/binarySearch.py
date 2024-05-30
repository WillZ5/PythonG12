def b_Search(values, InputNum):  # Binary search value
    Low, High = 0, len(values)-1
    while Low <= High:
        Mid = (Low + High)//2
        if values[Mid] == InputNum:
            return Mid
        elif values[Mid] < InputNum:
            Low = Mid+1
        else:
            High = Mid-1
    return-1

try:  # Error Handling
    # sort the values then convert them to a list
    values = list(sorted(map(int, input("Please enter a sorted list of numbers (separated by comma): ").split(","))))
    InputNum = int(input("Please enter the value you want to find: "))
    result_Num = b_Search(values, InputNum)
    if result_Num != (-1):
        print(f"The number {InputNum} you are looking for is at the {result_Num}th place.")
    else:
        print("The number you entered is not in the list.")
except ValueError:
    print("Please input an integer.")
