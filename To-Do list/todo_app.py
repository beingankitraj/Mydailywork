import tkinter as tk
from tkinter import messagebox
import task_manager

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(padx=20, pady=20)
        
        # Keep track of task list locally for mappings from listbox index to task ID
        self.tasks = []

        # --- UI Construction ---
        
        # Title Label
        title_label = tk.Label(root, text="My Tasks", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=(0, 10))

        # Entry and Add Button frame
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.task_entry = tk.Entry(input_frame, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        add_btn = tk.Button(input_frame, text="Add Task", bg="#4CAF50", fg="white", 
                            font=("Helvetica", 10, "bold"), command=self.add_task)
        add_btn.pack(side=tk.RIGHT)

        # Listbox for Tasks
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#a6a6a6", 
                                       activestyle="none", height=15)
        self.task_listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Action Buttons frame
        action_frame = tk.Frame(root)
        action_frame.pack(fill=tk.X)

        toggle_btn = tk.Button(action_frame, text="Toggle Complete", bg="#2196F3", fg="white", 
                               font=("Helvetica", 10, "bold"), command=self.toggle_task)
        toggle_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        delete_btn = tk.Button(action_frame, text="Delete Task", bg="#f44336", fg="white", 
                               font=("Helvetica", 10, "bold"), command=self.delete_task)
        delete_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

        # Load tasks on startup
        self.refresh_listbox()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = task_manager.get_all_tasks()
        
        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "O"
            display_text = f"[{status}] {task['title']}"
            self.task_listbox.insert(tk.END, display_text)
            
            if task["completed"]:
                # strikethrough logic (simulated by gray color since Tkinter Listbox doesn't support rich text easily)
                self.task_listbox.itemconfig(index, {'fg': 'gray'})
            else:
                self.task_listbox.itemconfig(index, {'fg': 'black'})

    def add_task(self):
        title = self.task_entry.get().strip()
        if title:
            task_manager.add_task(title)
            self.task_entry.delete(0, tk.END)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_id = self.tasks[selected_index]["id"]
            task_manager.delete_task(task_id)
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def toggle_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_id = self.tasks[selected_index]["id"]
            task_manager.toggle_task(task_id)
            self.refresh_listbox()
            self.task_listbox.selection_set(selected_index) # Keep it selected
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to toggle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
