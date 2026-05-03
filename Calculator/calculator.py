import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = op_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


root = tk.Tk()
root.title("Simple Calculator App")
root.geometry("300x300")
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)


frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)


tk.Label(frame, text="Enter first number:", font=("Arial", 10)).pack(anchor="w")
entry_num1 = tk.Entry(frame, font=("Arial", 12))
entry_num1.pack(fill=tk.X, pady=(0, 10))


tk.Label(frame, text="Enter second number:", font=("Arial", 10)).pack(anchor="w")
entry_num2 = tk.Entry(frame, font=("Arial", 12))
entry_num2.pack(fill=tk.X, pady=(0, 10))


tk.Label(frame, text="Choose operation:", font=("Arial", 10)).pack(anchor="w")
op_var = tk.StringVar(root)
op_var.set("+")  # default value
op_menu = tk.OptionMenu(frame, op_var, "+", "-", "*", "/")
op_menu.config(font=("Arial", 11))
op_menu.pack(fill=tk.X, pady=(0, 15))


btn_calc = tk.Button(frame, text="Calculate", command=calculate, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white")
btn_calc.pack(fill=tk.X, pady=(0, 15))


lbl_result = tk.Label(frame, text="Result: ---", font=("Arial", 12, "bold"), fg="#333333")
lbl_result.pack()


if __name__ == "__main__":
    root.mainloop()
