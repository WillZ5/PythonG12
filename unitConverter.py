import tkinter as tk

# Conversion rates
CONVERSION_RATES = {
    "meters to feet": 3.2808,
    "feet to meters": 0.3048,
    "kilograms to pounds": 2.2046,
    "pounds to kilograms": 0.4536,
    "liters to gallons": 0.2642,
    "gallons to liters": 3.7854,
}


def on_set_click():
    conversion_type = option_menu.get()
    if conversion_type == "Length":
        options2 = ("meters to feet", "feet to meters")
    elif conversion_type == "Weight":
        options2 = ("kilograms to pounds", "pounds to kilograms")
    elif conversion_type == "Volume":
        options2 = ("liters to gallons", "gallons to liters")

    # Update the options of the second dropdown menu
    menu2['menu'].delete(0, 'end')
    for choice in options2:
        menu2['menu'].add_command(label=choice, command=tk._setit(option_menu_2, choice))
    option_menu_2.set("Please select a conversion")


def on_convert_click():
    try:
        input_val = float(e1.get())
        conversion = option_menu_2.get()

        # Check if conversion exists and calculate result.
        # If not found, an error message is output
        if conversion in CONVERSION_RATES:
            result = input_val * CONVERSION_RATES[conversion]
            e2.delete(0, tk.END)
            e2.insert(tk.END, str(result))
        else:
            e2.delete(0, tk.END)
            e2.insert(tk.END, "Error: Unknown conversion unit.")

    except ValueError:
        # Handle when input is not a number
        e2.delete(0, tk.END)
        e2.insert(tk.END, "Error: Input is not a number.")


window = tk.Tk()

for i in range(3):
    window.grid_rowconfigure(i, weight=1)
for i in range(2):
    window.grid_columnconfigure(i, weight=1)


label_input = tk.Label(window, text="Input")
label_input.grid(row=0, column=0)
e1 = tk.Entry(window)
e1.grid(row=0, column=1)

output_label = tk.Label(window, text="Output")
output_label.grid(row=1, column=0)
e2 = tk.Entry(window)
e2.grid(row=1, column=1)

option_menu = tk.StringVar(window)
options = ("Length", "Weight", "Volume")
menu = tk.OptionMenu(window, option_menu, *options)
menu.grid(row=2, column=0)
option_menu.set("Length")  # Set an initial option

option_menu_2 = tk.StringVar(window)
menu2 = tk.OptionMenu(window, option_menu_2, "")
menu2.grid(row=2, column=1)

set_button = tk.Button(window, text="Set", command=on_set_click)
set_button.grid(row=3, column=0)

convert_button = tk.Button(window, text="Convert", command=on_convert_click)
convert_button.grid(row=3, column=1)

on_set_click()
window.mainloop()