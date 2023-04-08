import tkinter as tk
from tkinter import ttk


def button_func():
    print("a button is pressed")


def hello():
    print("hello")


# create a window
window = tk.Tk()
window.title("Window and widgets")
# window.geometry('500x250')

# ttk widgets
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk text
text_box = tk.Text(master=window, width=40, height=10)
text_box.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# my label
my_label = ttk.Label(master=window, text="my label")
my_label.pack()

# my button
# my_button = ttk.Button(master=window, text="hello", command=hello)
my_button = ttk.Button(master=window, text="hello", command=lambda: print('hello'))
my_button.pack()

# ttk button
button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()

# exercise
# add one more text label and a button with a function that print hello
# the label should say my label and be between the entry widget and the button


# run
window.mainloop()
