import tkinter as tk
from tkinter import font, messagebox
import random
import string
import pyperclip

def generate_password():
    password_length = int(length_entry.get())

    if password_length < 1:
        password_label.config(text="Please enter a valid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    pw_entry.delete(0, tk.END)
    pw_entry.insert(0, password)

def accept_password():
    generated_password = pw_entry.get()
    if generated_password:
        pyperclip.copy(generated_password)
        password_label.config(text="Copied to clipboard")
    else:
        messagebox.showinfo("Info", "Please generate a password first.")

def reset_password():
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    pw_entry.delete(0, tk.END)
    password_label.config(text="")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg='white')

label_font = font.Font(size=22, underline=True, weight="bold")
heading_label = tk.Label(root, pady=10, padx=10, bg="white", fg="blue", text="Password Generator", font=label_font)
heading_label.pack()

main_frame = tk.Frame(root, pady=5, padx=10, bg="white")
main_frame.pack()

name_frame = tk.Frame(main_frame, pady=5, padx=10, bg="white")
name_frame.pack(side=tk.TOP)

length_label = tk.Label(name_frame, pady=5, padx=10, bg="white", text="Enter User Name:")
length_label.pack(side=tk.LEFT)

name_entry = tk.Entry(name_frame)
name_entry.pack(side=tk.LEFT)

length_frame = tk.Frame(main_frame, pady=5, padx=10, bg="white")
length_frame.pack(side=tk.TOP)

length_label = tk.Label(length_frame, pady=5, padx=10, bg="white", text="Enter Password Length:")
length_label.pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame)
length_entry.pack(side=tk.LEFT)

pw_frame = tk.Frame(main_frame, pady=5, padx=10, bg="white")
pw_frame.pack(side=tk.TOP)

pw_label = tk.Label(pw_frame, pady=5, padx=10, bg="white", text="Generated Password:")
pw_label.pack(side=tk.LEFT)

pw_entry = tk.Entry(pw_frame)
pw_entry.pack(side=tk.LEFT)

btn_frame = tk.Frame(root, pady=10, padx=10, bg="white")
btn_frame.pack(side=tk.TOP)

generate_button = tk.Button(btn_frame, pady=5, padx=10, fg="white", bg="blue", text="Generate Password", command=generate_password)
generate_button.pack(side=tk.TOP)

accept_button = tk.Button(btn_frame, pady=5, padx=10, fg="blue", bg="white", text="Accept", command=accept_password)
accept_button.pack(side=tk.TOP)

reset_button = tk.Button(btn_frame, pady=5, padx=10, fg="blue", bg="white", text="Reset", command=reset_password)
reset_button.pack(side=tk.TOP)

password_label = tk.Label(btn_frame, pady=10, padx=10, text="")
password_label.pack(side=tk.TOP)

root.mainloop()
