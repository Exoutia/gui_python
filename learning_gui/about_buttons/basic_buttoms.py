import tkinter as tk
from tkinter import ttk

# main window
window = tk.Tk()
window.title("Fun with buttons")
window.geometry("600x400")

# # tk var
# button_string = tk.StringVar(value="hunter")

# # button
# button = ttk.Button(
#     window,
#     text="simple button",
#     command=lambda: print("button is pressed"),
#     textvariable=button_string,
# )
# button.pack()

# # checkbutton
# check_var = tk.IntVar(value=10)
# check_button = ttk.Checkbutton(
#     window,
#     text="egg",
#     command=lambda: print(check_var.get()),
#     variable=check_var,
#     onvalue=10,
#     offvalue=89,
# )
# check_button.pack()


# # radiobuttons
# radio_var = tk.StringVar()
# radio1 = ttk.Radiobutton(
#     window,
#     text="rad1",
#     value="radio1",
#     command=lambda: print(radio_var.get()),
#     variable=radio_var,
# )
# radio1.pack()
# radio2 = ttk.Radiobutton(
#     window,
#     text="rad1",
#     value="radio2",
#     variable=radio_var,
#     command=lambda: print(radio_var.get()),
# )
# radio2.pack()

# exercise
check_var = tk.BooleanVar()
check = ttk.Checkbutton(
    window, text="check", variable=check_var, command=lambda: print(exercise_var.get())
)
check.pack()


def check_connect():
    print(check_var.get())
    check_var.set(False)


exercise_var = tk.StringVar()
radio3 = ttk.Radiobutton(
    window, text="A", value="A", variable=exercise_var, command=check_connect
)
radio3.pack()
radio4 = ttk.Radiobutton(
    window, text="B", value="B", variable=exercise_var, command=check_connect
)
radio4.pack()

# using function with args and we already solved it using the
# python lamda let me show you

entry_string_var = tk.StringVar(value="write here ")
entry = ttk.Entry(window, textvariable=entry_string_var)
entry.pack()


def to_upper(val):
    return val.get().upper()


upper_button = ttk.Button(
    window,
    text="to upper",
    command=lambda: entry_string_var.set(to_upper(entry_string_var)),
)
upper_button.pack()

# run
window.mainloop()
