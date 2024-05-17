#   Q1 FileReader

def FileRead():
    FilePath = str(input("Enter file path: "))

    file = open('FilePath', 'r')
    data = file.read()
    file.close()
    print(data)

FileRead()
