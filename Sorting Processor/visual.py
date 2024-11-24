import tkinter as tk
import random
import time

# Global variables for the Tkinter canvas
canvas_width = 600
canvas_height = 400
bars = []
num_bars = 50

# Function to create a random list of values
def generate_values():
    return [random.randint(10, canvas_height) for _ in range(num_bars)]

# Function to draw the bars on the canvas
def draw_bars(values, highlight=[]):
    canvas.delete("all")
    bar_width = canvas_width / num_bars
    for i, value in enumerate(values):
        x0 = i * bar_width
        y0 = canvas_height - value
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        color = "blue" if i not in highlight else "red"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update()

# Bubble Sort with animation
def bubble_sort(values):
    n = len(values)
    for i in range(n):
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                draw_bars(values, [j, j + 1])
                time.sleep(0.01)

# Insertion Sort with animation
def insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
            draw_bars(values, [j + 1])
            time.sleep(0.01)
        values[j + 1] = key
        draw_bars(values, [j + 1])
        time.sleep(0.01)

# Quick Sort with animation
def quick_sort(values, low, high):
    if low < high:
        pivot = partition(values, low, high)
        draw_bars(values, [pivot])
        time.sleep(0.01)
        quick_sort(values, low, pivot - 1)
        quick_sort(values, pivot + 1, high)

def partition(values, low, high):
    pivot = values[high]
    i = low - 1
    for j in range(low, high):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
            draw_bars(values, [i, j])
            time.sleep(0.01)
    values[i + 1], values[high] = values[high], values[i + 1]
    return i + 1

# Merge Sort with animation
def merge_sort(values):
    if len(values) > 1:
        mid = len(values) // 2
        left = values[:mid]
        right = values[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                values[k] = left[i]
                i += 1
            else:
                values[k] = right[j]
                j += 1
            draw_bars(values)
            k += 1
            time.sleep(0.01)

        while i < len(left):
            values[k] = left[i]
            i += 1
            k += 1
            draw_bars(values)
            time.sleep(0.01)

        while j < len(right):
            values[k] = right[j]
            j += 1
            k += 1
            draw_bars(values)
            time.sleep(0.01)

# Radix Sort with animation
def radix_sort(values):
    max_val = max(values)
    exp = 1
    while max_val // exp > 0:
        counting_sort(values, exp)
        exp *= 10

def counting_sort(values, exp):
    n = len(values)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = values[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = values[i] // exp
        output[count[index % 10] - 1] = values[i]
        count[index % 10] -= 1

    for i in range(n):
        values[i] = output[i]
        draw_bars(values)
        time.sleep(0.01)

# Function to start sorting with the selected algorithm
def start_sorting():
    values = generate_values()
    draw_bars(values)

    selected_algorithm = algorithm_var.get()
    if selected_algorithm == "Bubble Sort":
        bubble_sort(values)
    elif selected_algorithm == "Insertion Sort":
        insertion_sort(values)
    elif selected_algorithm == "Quick Sort":
        quick_sort(values, 0, len(values) - 1)
    elif selected_algorithm == "Merge Sort":
        merge_sort(values)
    elif selected_algorithm == "Radix Sort":
        radix_sort(values)
    
    draw_bars(values)

# Creating the main window
root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry(f"{canvas_width}x{canvas_height + 250}")

# Create a canvas to draw the bars
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create a label for instructions
instruction_label = tk.Label(root, text="Choose Sorting Algorithm", font=("Helvetica", 12))
instruction_label.pack()

# Create a variable to store the selected sorting algorithm
algorithm_var = tk.StringVar(value="Bubble Sort")

# Create radio buttons for selecting the sorting algorithm
bubble_sort_radio = tk.Radiobutton(root, text="Bubble Sort", variable=algorithm_var, value="Bubble Sort", font=("Helvetica", 12))
bubble_sort_radio.pack()

insertion_sort_radio = tk.Radiobutton(root, text="Insertion Sort", variable=algorithm_var, value="Insertion Sort", font=("Helvetica", 12))
insertion_sort_radio.pack()

quick_sort_radio = tk.Radiobutton(root, text="Quick Sort", variable=algorithm_var, value="Quick Sort", font=("Helvetica", 12))
quick_sort_radio.pack()

merge_sort_radio = tk.Radiobutton(root, text="Merge Sort", variable=algorithm_var, value="Merge Sort", font=("Helvetica", 12))
merge_sort_radio.pack()

radix_sort_radio = tk.Radiobutton(root, text="Radix Sort", variable=algorithm_var, value="Radix Sort", font=("Helvetica", 12))
radix_sort_radio.pack()

# Create a button to start the sorting process
start_button = tk.Button(root, text="Start Sorting", font=("Helvetica", 12), command=start_sorting)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
