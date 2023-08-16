import tkinter as tk
from tkinter import messagebox, simpledialog

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_frame()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def edit_task(index):
    updated_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=tasks[index])
    if updated_task is not None:
        tasks[index] = updated_task
        update_frame()

def delete_task(index):
    tasks.pop(index)
    update_frame()

def update_frame():
    for widget in frame_tasks.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        task_frame = tk.Frame(frame_tasks, bg="white", highlightthickness=2)
        task_frame.pack(fill=tk.BOTH)
        task_frame.pack_propagate(50)
        label = tk.Label(task_frame, bg="white", text=task, font=("Helvetica", 12))
        label.pack(side=tk.LEFT, padx=5, fill=tk.BOTH)

        delete_button = tk.Button(task_frame, bg="red", fg="white", text="Delete", font=("Helvetica", 10), borderwidth=1, command=lambda index=index: delete_task(index))
        delete_button.pack(side=tk.RIGHT)

        edit_button = tk.Button(task_frame, bg="green", fg="white", text="Edit", font=("Helvetica", 10), borderwidth=1, command=lambda index=index: edit_task(index))
        edit_button.pack(side=tk.RIGHT, padx=5)

tasks = []

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x300")
root.configure(bg='white')

head_frame = tk.Frame(root, bg="green")
head_frame.pack(pady=10, padx=10, side=tk.TOP, fill="x")
label_heading = tk.Label(head_frame, bg="green", fg="white",  text="To Do List", font=("Helvetica", 22))
label_heading.pack(pady=10, fill=tk.BOTH)

entry_heading = tk.Label(root, bg="white", text="Add Items", font=("Helvetica", 14))
entry_heading.pack(pady=10, side=tk.TOP)

entry_frame = tk.Frame(root, bg="white")
entry_frame.pack(pady=10, padx=10, side=tk.TOP, fill="x")

entry_task = tk.Entry(entry_frame, bg="white", width=15, font=("Helvetica", 16))
entry_task.pack(pady=5, padx=10, side=tk.LEFT)

button_add = tk.Button(entry_frame, bg="green", fg="white", text="Submit", font=("Helvetica", 12), width=500, borderwidth=1, command=add_task)
button_add.pack(pady=5, padx=10, side=tk.LEFT)

frame_tasks = tk.Frame(root, bg="white")
frame_tasks.pack(pady=10, padx=10, fill=tk.BOTH)

root.mainloop()
