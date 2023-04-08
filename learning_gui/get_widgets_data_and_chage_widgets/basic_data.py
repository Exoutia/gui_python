import tkinter as tk
from tkinter import ttk


def button_func():
    # get the contet of the entry
    print(entry_text := entry.get())

    # update the label
    # label.configure(text=f'{entry_text}')
    label["text"] = entry_text
    entry["state"] = "disabled"
    # print(label.config())


def reset():
    entry["state"] = "enabled"
    label["text"] = "howdy"


# window
window = tk.Tk()
window.title("Gettin and setting widgets")

# widgets
label = ttk.Label(master=window, text="Howdy")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

reset_button = ttk.Button(window, text="reset", command=reset)
reset_button.pack()

# run
window.mainloop()
