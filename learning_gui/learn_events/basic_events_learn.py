import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')


# window
window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text="A button")
btn.pack()

# events
btn.bind("<Alt-KeyPress-a>", lambda event: print(event))
window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))
# text.bind('<Motion>', get_pos)
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))

# exercise
text.bind('<Shift-MouseWheel>', lambda event: print(f'this is printing event: {event}'))


# run
window.mainloop()
