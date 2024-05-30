import os
import shutil

# Default folder
Path = "file"

def create_File(file_Name, content=""):  # Create a file and write
    file_Path = os.path.join(Path, file_Name)
    with open(file_Path, "w") as file:
        file.write(content)
    print(f"File \"{file_Name}\" has been created.")

def modify_File(file_Name, content):  # Append the file
    file_Path = os.path.join(Path, file_Name)
    if os.path.exists(file_Path):
        with open(file_Path, "a") as file:
            file.write(content)
        print(f"File \"{file_Name}\" has been modified.")
    else:
        print(f"File \"{file_Name}\" does not exist.")

def overwrite_File(file_Name, content):  # Overwrite file
    file_Path = os.path.join(Path, file_Name)
    if os.path.exists(file_Path):
        with open(file_Path, "w") as file:
            file.write(content)
        print(f"File \"{file_Name}\" has been overwritten.")
    else:
        print(f"File \"{file_Name}\" does not exist.")

def delete_File(file_Name):  # Delete the file
    file_Path = os.path.join(Path, file_Name)
    if os.path.exists(file_Path):
        os.remove(file_Path)
        print(f"File \"{file_Name}\" has been deleted.")
    else:
        print(f"File \"{file_Name}\" does not exist.")

def copy_file(file_Name, new_File_Name):  # Copy the file
    file_path = os.path.join(Path, file_Name)
    new_File_Path = os.path.join(Path, new_File_Name)
    if os.path.exists(file_path):
        shutil.copy(file_path, new_File_Path)
        print(f"File \"{file_Name}\" has been copied to \"{new_File_Name}\".")
    else:
        print(f"File \"{file_Name}\" does not exist.")

def display_File(file_Name):  # File Display
    file_Path = os.path.join(Path, file_Name)
    if os.path.exists(file_Path):
        with open(file_Path, 'r') as file:
            content = file.read()
        print(f"Content of file \"{file_Name}\":\n{content}")
    else:
        print(f"File \"{file_Name}\" does not exist.")

def get_Multiline_Input(prompt):  # User Input
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":  # Break the input loop
            break
        lines.append(line)
    return "\n".join(lines)  # Multi Line Input

def main():
    file_Name = input("Please enter the file name: ")
    file_Path = os.path.join(Path, file_Name)

    if not os.path.exists(file_Path):
        content = get_Multiline_Input(
            "File does not exist. Please enter content to create a new file (type \"DONE\" to finish):")
        create_File(file_Name, content)
    else:
        display_File(file_Name)

    Selection = input("Menu: 1) Copy file 2) Modify file 3) Overwrite file 4) Delete file 5) Exit \nPlease enter your selection: ")

    if Selection == "1":
        new_File_Name = input("Please enter the new file name: ")
        copy_file(file_Name, new_File_Name)
    elif Selection == "2":
        content = get_Multiline_Input("Please enter content to append (type \"DONE\" to finish):")
        modify_File(file_Name, content)
    elif Selection == "3":
        content = get_Multiline_Input("Please enter new content (type \"DONE\" to finish):")
        overwrite_File(file_Name, content)
    elif Selection == "4":
        confirm = input("Are you sure you want to delete the file? (y/n): ")
        if confirm.lower() == "y":
            delete_File(file_Name)
        else:
            print("Operation cancelled.")
    elif Selection == "5":
        print("No changes made.")
    else:
        print("Invalid selection number.")

main()
