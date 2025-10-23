import tkinter as tk
from tkinter import messagebox, simpledialog

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

# Functions
def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        tasks.append(task)
        update_listbox()
        messagebox.showinfo("Success", f"Task '{task}' added successfully!")

def update_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Task", "Please select a task to update.")
        return
    index = selected[0]
    new_task = simpledialog.askstring("Update Task", "Enter new task:")
    if new_task:
        old_task = tasks[index]
        tasks[index] = new_task
        update_listbox()
        messagebox.showinfo("Success", f"Task '{old_task}' updated to '{new_task}'.")

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Task", "Please select a task to delete.")
        return
    index = selected[0]
    task = tasks.pop(index)
    update_listbox()
    messagebox.showinfo("Deleted", f"Task '{task}' deleted successfully!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Widgets
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(button_frame, text="Update Task", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

exit_btn = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_btn.pack(pady=10)

# Run the app
root.mainloop()
