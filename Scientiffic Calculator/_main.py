import tkinter as tk
import math

# Function for button press
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function for clear button
def button_clear():
    entry.delete(0, tk.END)

# Function for evaluating the expression
def button_equals():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function for scientific functions
def button_sci_function(function):
    try:
        value = float(entry.get())
        if function == "sqrt":
            result = math.sqrt(value)
        elif function == "sin":
            result = math.sin(math.radians(value))
        elif function == "cos":
            result = math.cos(math.radians(value))
        elif function == "tan":
            result = math.tan(math.radians(value))
        elif function == "log":
            result = math.log(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Set a more neutral background like Windows application
root.config(bg='#f0f0f0')

# Entry widget for displaying the expression
entry = tk.Entry(root, width=25, font=("Segoe UI", 18), bd=2, relief="solid", justify='right', bg='white', fg='black')
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# Button layout and commands
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sin', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('cos', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('tan', 4, 4),
    ('log', 5, 0), ('C', 5, 1)
]

# Create buttons and add them to the grid with a Windows-like style
button_bg = '#dcdcdc'  # Light grey for normal buttons
button_fg = 'black'    # Black text color
button_highlight = '#f1f1f1'  # Highlighted color for button press

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, font=("Segoe UI", 14), bg="#0078d4", fg="white", relief="flat", command=button_equals).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        tk.Button(root, text=text, width=5, height=2, font=("Segoe UI", 14), bg="#ff4343", fg="white", relief="flat", command=button_clear).grid(row=row, column=col, padx=5, pady=5)
    elif text in ['sqrt', 'sin', 'cos', 'tan', 'log']:
        tk.Button(root, text=text, width=5, height=2, font=("Segoe UI", 14), bg="#e1e1e1", fg="black", relief="flat", command=lambda t=text: button_sci_function(t)).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Segoe UI", 14), bg=button_bg, fg=button_fg, relief="flat", command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
root.mainloop()
