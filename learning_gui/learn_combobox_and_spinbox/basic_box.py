import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title("combo and spin")

# Combobox
items = ("Icecream", "Pizza", "Broccoli")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo["values"] = items
combo.pack()

# new function:
def print_message(event):
    if food_string.get() == 'Icecream':
        print("So cool")
    if food_string.get() == "Pizza":
        print('So Tasty')
    if food_string.get() == 'Broccoli':
        print('So Healthy')

# event
combo.bind('<<ComboboxSelected>>',lambda event: print_message(event))

# # Spin box
# spin = ttk.Spinbox(window, from_=3, to=20, increment=3, command=lambda: print('spin is done'))
# # spin['values'] = items
# spin.bind('<<Increment>>', lambda event: print('up'))
# spin.bind('<<Decrement>>', lambda event: print('down'))
# spin.pack()


# exercise
chars = ['A', 'B', 'C', 'D', 'E']
spin_var = tk.StringVar(value=chars[0])
spin = ttk.Spinbox(
    master = window,
    values = chars,
    textvariable=spin_var
)
spin.bind('<<Decrement>>', lambda event: print(spin_var.get()))
spin.pack()

# run
window.mainloop()
