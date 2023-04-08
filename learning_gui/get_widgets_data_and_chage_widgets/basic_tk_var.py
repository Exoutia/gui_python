import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tkinter variables')


# function
def print_val():
    print(string_var.get())
    string_var.set('button pressed')

# tkinter variables
string_var = tk.StringVar(value='start value')

# widgets
label = ttk.Label(master= window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master= window, textvariable=string_var)
entry.pack()

# entry2 = ttk.Entry(master= window, textvariable=string_var)
# entry2.pack()

button = ttk.Button(master= window, text= 'button', command=print_val)
button.pack()

my_var = tk.StringVar(value='test')

entry1 = ttk.Entry(master=window, textvariable=my_var)
entry1.pack()
entry2 = ttk.Entry(master=window, textvariable=my_var)
entry2.pack()
my_label = ttk.Label(master = window, textvariable=my_var)
my_label.pack()


# run
window.mainloop()