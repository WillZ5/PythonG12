def fibonacci_sequence(InputNum):   # Fibonacci Sequence Calculator
    if InputNum <= 0:
        return []
    elif InputNum == 1:
        return [0]
    elif InputNum == 2:
        return [0,1]
    else:
        sequence = fibonacci_sequence(InputNum - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

try:    # Error Handling
    InputNum = int(input("Please enter a number: "))
    if InputNum < 0:
        print(f"\"{InputNum}\" is a not valid input! Please enter a positive integer.")
    else:
        print("Fibonacci sequence:", fibonacci_sequence(InputNum))
except ValueError:
    print("Input Invalid! You must enter a positive integer.")