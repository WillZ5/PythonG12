# Q10 Syracuse Calculator

def Syracuse(num):

    while True:
        if num != 1:
            if num % 2 == 0:
                num = num/2
                print(int(num))
            else:
                num = num*3+1
                print(int(num))
        else:
            break

Syracuse(int(input("Please enter a number: ")))