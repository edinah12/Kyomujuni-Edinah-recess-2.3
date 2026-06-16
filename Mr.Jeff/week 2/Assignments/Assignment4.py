import tkinter as tk
from tkinter import messagebox


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2


def calculate(operation):
    try:
        num1 = float(first_number_entry.get())
        num2 = float(second_number_entry.get())

        if operation == "add":
            result = add(num1, num2)
            symbol = "+"
        elif operation == "subtract":
            result = subtract(num1, num2)
            symbol = "-"
        elif operation == "multiply":
            result = multiply(num1, num2)
            symbol = "x"
        else:
            result = divide(num1, num2)
            symbol = "/"

        result_label.config(text=f"Result: {num1} {symbol} {num2} = {result}")
    except ValueError as error:
        messagebox.showerror("Input Error", str(error))


root = tk.Tk()
root.title("Menu-Driven GUI Calculator")
root.geometry("360x260")
root.resizable(False, False)

title_label = tk.Label(root, text="Calculator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

tk.Label(input_frame, text="First Number:", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
first_number_entry = tk.Entry(input_frame, width=18, font=("Arial", 11))
first_number_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Second Number:", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
second_number_entry = tk.Entry(input_frame, width=18, font=("Arial", 11))
second_number_entry.grid(row=1, column=1, padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=12)

tk.Button(button_frame, text="Add", width=10, command=lambda: calculate("add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtract", width=10, command=lambda: calculate("subtract")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", width=10, command=lambda: calculate("multiply")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", width=10, command=lambda: calculate("divide")).grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=12)

root.mainloop()