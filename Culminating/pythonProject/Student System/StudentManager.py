import os

class StudentManager:
    def __init__(self, folder_Path="file"):  # Initialize path
        self.folder_Path = folder_Path
        if not os.path.exists(self.folder_Path):
            os.makedirs(self.folder_Path)

    def Create(self, file_name, content=""):  # Create a file
        file_path = os.path.join(self.folder_Path, file_name)
        with open(file_path, "w") as file:
            file.write(content)

    def Modify(self, file_name, content):  # Modify file
        file_Path = os.path.join(self.folder_Path, file_name)
        if os.path.exists(file_Path):
            with open(file_Path, "a") as file:
                file.write(content)
        else:
            raise FileNotFoundError(f"File \"{file_name}\" does not exist.")

    def Overwrite(self, file_Name, content):  # Overwrite file
        file_Path = os.path.join(self.folder_Path, file_Name)
        if os.path.exists(file_Path):
            with open(file_Path, "w") as file:
                file.write(content)
        else:
            raise FileNotFoundError(f"File \"{file_Name}\" does not exist.")

    def Delete(self, file_Name):  # Delete file
        file_Path = os.path.join(self.folder_Path, file_Name)
        if os.path.exists(file_Path):
            os.remove(file_Path)
        else:
            raise FileNotFoundError(f"File \"{file_Name}\" does not exist.")

    def Display(self, file_Name):  # Display file
        file_Path = os.path.join(self.folder_Path, file_Name)
        if os.path.exists(file_Path):
            with open(file_Path, 'r') as file:
                content = file.read()
            return content
        else:
            raise FileNotFoundError(f"File \"{file_Name}\" does not exist.")

    def List(self):  # file loop
        return [f for f in os.listdir(self.folder_Path) if os.path.isfile(os.path.join(self.folder_Path, f))]



# GUI tkinter

import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

class StudentInfoManager:
    def __init__(self, window):  #  student manager program
        self.manager = StudentManager()
        self.window = window
        self.window.title("Student Manager")

        self.create_Widgets()

    def create_Widgets(self):
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.frame = tk.Frame(self.window)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.label = tk.Label(self.frame, text="Student Manager")
        self.label.pack(pady=10)

        self.add_Student_Button = tk.Button(self.frame, text="Add a New Student", command=self.student_Add)
        self.add_Student_Button.pack(pady=5)

        self.display_Student_Button = tk.Button(self.frame, text="Display All Students", command=self.student_Display)
        self.display_Student_Button.pack(pady=5)

    def student_Add(self):  # Add new student structure
        try:
            self.student_Window = tk.Toplevel(self.window)
            self.student_Window.title("Add Student")

            # Values
            labels = ["First Name", "Last Name", "Grade", "Score", "Absent", "Late", "Parents/Guardian", "Contact"]
            self.entries = {}

            for idx, label_Text in enumerate(labels):
                label = tk.Label(self.student_Window, text=label_Text + ":")
                label.grid(row=idx, column=0, sticky="E")
                entry = tk.Entry(self.student_Window)
                entry.grid(row=idx, column=1, sticky="EW")
                self.entries[label_Text] = entry

            save_Info_Button = tk.Button(self.student_Window, text="Save", command=self.student_Save)
            save_Info_Button.grid(row=len(labels), column=0, columnspan=2, sticky="EW")
        except Exception as e:  # Error Handling
            messagebox.showerror("Error!", f"There's an error while adding student, error code: {str(e)}")

    # Save student info
    def student_Save(self):
        try:
            student_Info = {label: entry.get() for label, entry in self.entries.items()}
            file_Name = f"{student_Info['First Name']}_{student_Info['Last Name']}.txt"
            content = "\n".join([f"{label}: {data}" for label, data in student_Info.items()])
            self.manager.Create(file_Name, content)
            messagebox.showinfo("Done!", f"Student info has been added successfully!")
            self.student_Window.destroy()
        except Exception as e:  # Error Handling
            messagebox.showerror("Error!", f"There's an error while saving student, error code: {str(e)}")

    def student_Display(self):
        try:
            self.list_Window = tk.Toplevel(self.window)
            self.list_Window.title("Student List")

            scrollbar = Scrollbar(self.list_Window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.listbox = Listbox(self.list_Window, yscrollcommand=scrollbar.set)
            self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            students = self.manager.List()
            for student in students:
                self.listbox.insert(tk.END, student)

            self.listbox.bind("<<ListboxSelect>>", self.student_Show)
            scrollbar.config(command=self.listbox.yview)
        except Exception as e:
            messagebox.showerror("Error!", f"There's an error while displaying students, error code: {str(e)}")

    def student_Show(self, event):
        try:
            student_Selected = self.listbox.get(self.listbox.curselection())
            content = self.manager.Display(student_Selected)
            self.student_Show_Window(student_Selected, content)
        except Exception as e:
            messagebox.showerror("Error!", f"There's an error while showing student, error code: {str(e)}")

    def student_Show_Window(self, file_Name, content):
        try:
            self.student_info_window = tk.Toplevel(self.window)
            self.student_info_window.title(f"Student Info - {file_Name}")

            self.entries = {}
            for idx, line in enumerate(content.splitlines()):
                label_text, data = line.split(": ", 1)
                label = tk.Label(self.student_info_window, text=label_text + ":")
                label.grid(row=idx, column=0, sticky="E")
                entry = tk.Entry(self.student_info_window)
                entry.grid(row=idx, column=1, sticky="EW")
                entry.insert(0, data)
                self.entries[label_text] = entry

            info_Save_Button = tk.Button(self.student_info_window, text="Save",
                                         command=lambda: self.student_Update(file_Name))
            info_Save_Button.grid(row=len(self.entries), column=0, sticky="EW")

            info_Delete_Button = tk.Button(self.student_info_window, text="Delete",
                                           command=lambda: self.student_Delete(file_Name))
            info_Delete_Button.grid(row=len(self.entries), column=1, sticky="EW")

            info_Exit_Button = tk.Button(self.student_info_window, text="Exit", command=self.student_info_window.destroy)
            info_Exit_Button.grid(row=len(self.entries) + 1, column=0, columnspan=2, sticky="EW")
        except Exception as e:
            messagebox.showerror("Error!", f"There's an error while showing student window: {str(e)}")

    def student_Update(self, file_Name):
        try:
            student_Info = {label: entry.get() for label, entry in self.entries.items()}
            content = "\n".join([f"{label}: {data}" for label, data in student_Info.items()])
            self.manager.Overwrite(file_Name, content)
            messagebox.showinfo("Done!", f"Student record has been updated.")
            self.student_info_window.destroy()
        except Exception as e:
            messagebox.showerror("Error!", f"There's an error while updating student, error code: {str(e)}")

    def student_Delete(self, file_Name):
        try:
            user_Confirm = messagebox.askyesno("WARNING!", f"Are you sure you want to delete '{file_Name}'?")
            if user_Confirm:
                self.manager.Delete(file_Name)
                messagebox.showinfo("Done!", f"Student record has been deleted.")
                self.student_info_window.destroy()
                self.list_Window.destroy()
        except Exception as e:
            messagebox.showerror("Error!", f"There's an error while deleting student, error code: {str(e)}")



def main():
    root = tk.Tk()
    Manager = StudentInfoManager(root)
    root.mainloop()
main()