import tkinter as tk
from tkinter import Canvas

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Error! Invalid input")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Error! Invalid input")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Error! Invalid input")

def divide():
    try:
        if float(num2.get()) == 0:
            result.set("Error! Division by zero.")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        result.set("Error! Invalid input")

# Function to create a gradient background
def create_gradient(canvas, color1, color2):
    canvas.update()
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height
    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Maximize the window
root.state('zoomed')

# Create a canvas for the gradient background
canvas = Canvas(root)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, "#ff99cc", "#99ccff")

# Create a frame to hold the content
frame = tk.Frame(canvas, bg="white", bd=10, relief="raised")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create entry fields for numbers
num1_label = tk.Label(frame, text="Enter first number:", font=("Arial", 14))
num1_label.grid(row=0, column=0, padx=10, pady=10)
num1 = tk.Entry(frame, font=("Arial", 14), width=15)
num1.grid(row=0, column=1, padx=10, pady=10)

num2_label = tk.Label(frame, text="Enter second number:", font=("Arial", 14))
num2_label.grid(row=1, column=0, padx=10, pady=10)
num2 = tk.Entry(frame, font=("Arial", 14), width=15)
num2.grid(row=1, column=1, padx=10, pady=10)

# Create buttons for operations
button_font = ("Arial", 14)
button_color = "#4CAF50"
button_active_color = "#45a049"

add_button = tk.Button(frame, text="Add", command=add, font=button_font, bg=button_color, activebackground=button_active_color, width=10)
add_button.grid(row=2, column=0, padx=10, pady=10)

subtract_button = tk.Button(frame, text="Subtract", command=subtract, font=button_font, bg=button_color, activebackground=button_active_color, width=10)
subtract_button.grid(row=2, column=1, padx=10, pady=10)

multiply_button = tk.Button(frame, text="Multiply", command=multiply, font=button_font, bg=button_color, activebackground=button_active_color, width=10)
multiply_button.grid(row=3, column=0, padx=10, pady=10)

divide_button = tk.Button(frame, text="Divide", command=divide, font=button_font, bg=button_color, activebackground=button_active_color, width=10)
divide_button.grid(row=3, column=1, padx=10, pady=10)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result, font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
