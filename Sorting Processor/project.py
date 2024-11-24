import tkinter as tk
from tkinter import messagebox
import subprocess

# Quick Sort function to sort a list of values
def quick_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    
    if ascending:
        return quick_sort(less_than_pivot, ascending) + [pivot] + quick_sort(greater_than_pivot, ascending)
    else:
        return quick_sort(greater_than_pivot, ascending) + [pivot] + quick_sort(less_than_pivot, ascending)

# Bubble Sort function
def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Insertion Sort function
def insertion_sort(arr, ascending=True):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((ascending and arr[j] > key) or (not ascending and arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort function
def merge_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], ascending)
    right = merge_sort(arr[mid:], ascending)
    
    # Merge the sorted halves
    merged = []
    while left and right:
        if (ascending and left[0] <= right[0]) or (not ascending and left[0] > right[0]):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left if left else right)
    return merged

# Function to process the input, sort it using the selected algorithm, and display the output
def process_input():
    input_text = entry.get().strip()
    
    # Check if the input is empty
    if not input_text:
        messagebox.showwarning("Input Warning", "Please enter some values separated by commas.")
        return
    
    # Split the input text by commas and strip extra spaces
    values = [value.strip() for value in input_text.split(',')]
    
    # Get the selected sorting order (ascending or descending)
    ascending = ascending_var.get()
    
    # Get the selected sorting algorithm
    selected_algorithm = algorithm_var.get()
    
    # Apply the selected sorting algorithm
    if selected_algorithm == "Quick Sort":
        sorted_values = quick_sort(values, ascending)
        complexity_label.config(text="Time Complexity: O(n log n)\nSpace Complexity: O(log n)")
    elif selected_algorithm == "Bubble Sort":
        sorted_values = bubble_sort(values, ascending)
        complexity_label.config(text="Time Complexity: O(n^2)\nSpace Complexity: O(1)")
    elif selected_algorithm == "Insertion Sort":
        sorted_values = insertion_sort(values, ascending)
        complexity_label.config(text="Time Complexity: O(n^2)\nSpace Complexity: O(1)")
    elif selected_algorithm == "Merge Sort":
        sorted_values = merge_sort(values, ascending)
        complexity_label.config(text="Time Complexity: O(n log n)\nSpace Complexity: O(n)")

    # Display the sorted values in the result label
    result_label.config(text="Sorted Output: " + ", ".join(sorted_values))
    
    # Show the time and space complexity
    complexity_label.pack(pady=10)

# Function to run the visual.py file when the button is clicked
def run_visual_script():
    try:
        subprocess.run(["python", "visual.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while running visual.py: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "visual.py file not found. Please make sure the file exists.")

# Create the main window
root = tk.Tk()
root.title("Sorting Algorithm Input Processor")  # Set window title
root.geometry("1100x700")  # Set window size
root.config(bg="#f4f4f9")  # Set background color for the window

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter comma-separated values:", font=("Helvetica", 12, "bold"), bg="#f4f4f9")
instruction_label.pack(pady=10)  # Add label to the window with padding

# Create an entry widget for input
entry = tk.Entry(root, font=("Helvetica", 14), width=35, relief="solid", bd=2, fg="#333", bg="white")
entry.pack(pady=10)  # Add entry widget to the window with padding

# Create a label for the sorting order selection
order_label = tk.Label(root, text="Select sorting order:", font=("Helvetica", 12), bg="#f4f4f9")
order_label.pack(pady=5)

# Create a variable to store the sorting order (True for ascending, False for descending)
ascending_var = tk.BooleanVar(value=True)

# Create radio buttons for selecting the sorting order
ascending_radio = tk.Radiobutton(root, text="Ascending", variable=ascending_var, value=True, font=("Helvetica", 12), bg="#f4f4f9")
ascending_radio.pack()

descending_radio = tk.Radiobutton(root, text="Descending", variable=ascending_var, value=False, font=("Helvetica", 12), bg="#f4f4f9")
descending_radio.pack()

# Create a label for the algorithm selection
algorithm_label = tk.Label(root, text="Select sorting algorithm:", font=("Helvetica", 12), bg="#f4f4f9")
algorithm_label.pack(pady=5)

# Create a variable to store the selected sorting algorithm
algorithm_var = tk.StringVar(value="Quick Sort")

# Create radio buttons for selecting the sorting algorithm
quick_sort_radio = tk.Radiobutton(root, text="Quick Sort", variable=algorithm_var, value="Quick Sort", font=("Helvetica", 12), bg="#f4f4f9")
quick_sort_radio.pack()

bubble_sort_radio = tk.Radiobutton(root, text="Bubble Sort", variable=algorithm_var, value="Bubble Sort", font=("Helvetica", 12), bg="#f4f4f9")
bubble_sort_radio.pack()

insertion_sort_radio = tk.Radiobutton(root, text="Insertion Sort", variable=algorithm_var, value="Insertion Sort", font=("Helvetica", 12), bg="#f4f4f9")
insertion_sort_radio.pack()

merge_sort_radio = tk.Radiobutton(root, text="Merge Sort", variable=algorithm_var, value="Merge Sort", font=("Helvetica", 12), bg="#f4f4f9")
merge_sort_radio.pack()

# Create a button that will trigger the processing of input
process_button = tk.Button(root, text="Sort Input", command=process_input, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=4)
process_button.pack(pady=20)  # Add button to the window with padding

# Create a label to display the result
result_label = tk.Label(root, text="Sorted Output: ", font=("Helvetica", 12), bg="#f4f4f9")
result_label.pack(pady=20)  # Add label to the window with padding

# Create a label to display the time and space complexity (Initially hidden)
complexity_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f4f4f9")
# complexity_label.pack(pady=20)  # Initially hidden

# Create a button to run the visual.py script
visual_button = tk.Button(root, text="Run Visual Sorting", command=run_visual_script, font=("Helvetica", 14, "bold"), bg="#FF5722", fg="white", relief="raised", bd=4)
visual_button.pack(pady=20)  # Add button to run visual script

# Run the Tkinter event loop
root.mainloop()
