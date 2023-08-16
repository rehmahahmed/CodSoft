import tkinter as tk
from math import sqrt, factorial


def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "<_":
        entry.delete(len(entry.get()) - 1, tk.END)
    elif text == "!":
        try:
            num = int(entry.get())
            result = str(factorial(num))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "√":
        try:
            num = float(entry.get())
            result = str(sqrt(num))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("C", 1, 0), ("√", 1, 1), ("/", 1, 2), ("<_", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("!", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]

# Set uniform button size
button_width = 4
button_height = 1

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 20), width=button_width, height=button_height)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
