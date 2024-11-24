import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check for correct username and password
    if username.lower() == "admin" and password.lower() == "pass":
        messagebox.showinfo("Login Success", "Login Successful! Opening Project...")
        open_project()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

# Function to open the Project.py file
def open_project():
    # You can replace this with your actual project path
    project_path = "Project.py"  # Assuming the Project.py is in the same directory
    if os.path.exists(project_path):
        # Open the Project.py file using Python
        subprocess.run(["python", project_path])
    else:
        messagebox.showerror("Error", f"Project file '{project_path}' not found.")

# Creating the Tkinter window
root = tk.Tk()
root.title("Login Window")
root.geometry("300x200")
root.config(bg="#f4f4f9")

# Create a label and input field for username
label_username = tk.Label(root, text="Username", font=("Helvetica", 12), bg="#f4f4f9")
label_username.pack(pady=5)

entry_username = tk.Entry(root, font=("Helvetica", 12), width=20, bd=2)
entry_username.pack(pady=5)

# Create a label and input field for password
label_password = tk.Label(root, text="Password", font=("Helvetica", 12), bg="#f4f4f9")
label_password.pack(pady=5)

entry_password = tk.Entry(root, font=("Helvetica", 12), width=20, bd=2, show="*")
entry_password.pack(pady=5)

# Create a login button
login_button = tk.Button(root, text="Login", font=("Helvetica", 12), command=validate_login, width=20, height=2, bg="#4CAF50", fg="white")
login_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
