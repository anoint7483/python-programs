# import tkinter as tk

# # Create the main application window
# root = tk.Tk()

# # Set the title of the window
# root.title("Calculator")

# # Set the size of the window
# root.geometry("700x500")

# # Start the main event loop
# root.mainloop()


# import tkinter as tk

# # Function to be called when the button is clicked
# def on_button_click():
#     label.config(text="Button clicked!")

# # Create the main application window
# root = tk.Tk()
# root.title("Tkinter Widgets")

# root.geometry("1000x700")

# # Create a label widget
# label = tk.Label(root, text="Hello, Abhishek")
# label.pack(pady=10)

# # Create an entry widget
# entry = tk.Entry(root)
# entry.pack(pady=10)

# # Create a button widget
# button = tk.Button(root, text="click Me", width=6, height=1, font=('Arial', 10), command=on_button_click)
# button.pack(pady=10)

# canvas = tk.Canvas(root, width=200, height=200)
# canvas.pack()
# canvas.create_line(6, 3, 206, 200)

# # Create a listbox widget
# listbox = tk.Listbox(root)
# listbox.insert(1, "Option 1")
# listbox.insert(2, "Option 2")
# listbox.insert(3, "Option 3")
# listbox.pack(pady=10)

# # Start the main event loop
# root.mainloop()

# import tkinter as tk

# # Function to draw a circle
# def draw_circle(canvas, x, y, radius):
#     # Calculate the bounding box coordinates
#     x1 = x - radius
#     y1 = y - radius
#     x2 = x + radius
#     y2 = y + radius
#     # Draw the circle
#     canvas.create_oval(x1, y1, x2, y2, outline="black", fill="skyblue", width=1)

# # Create the main window
# root = tk.Tk()
# root.title("Draw Circle Example")

# # Create a Canvas widget
# canvas = tk.Canvas(root, width=500, height=500, bg="white")
# canvas.pack()

# # Draw a circle with center at (200, 200) and radius 100
# draw_circle(canvas, 250, 250, 150)

# # Start the Tkinter event loop
# root.mainloop()


# import tkinter as tk

# # Function to draw a rectangle
# def draw_rectangle(canvas, x1, y1, x2, y2):
#     # Draw the rectangle with specified coordinates
#     canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue", width=2)

# # Create the main window
# root = tk.Tk()
# root.title("Draw Rectangle Example")

# # Create a Canvas widget
# canvas = tk.Canvas(root, width=400, height=400, bg="white")
# canvas.pack()

# # Draw a rectangle with top-left corner (50, 50) and bottom-right corner (300, 200)
# draw_rectangle(canvas, 50, 50, 300, 200)

# # Start the Tkinter event loop
# root.mainloop()



# import tkinter as tk

# # Create the main window
# root = tk.Tk()

# # Set the title of the window
# root.title("Simple Tkinter Window")

# # Set the window size (width x height)
# root.geometry("400x300")

# # Run the application
# root.mainloop()



# import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.title("Tkinter Example")
# root.geometry("300x200")

# # Label widget
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack(pady=10)

# # Entry widget
# entry = tk.Entry(root)
# entry.pack(pady=10)

# # Button widget
# def on_button_click():
#     entered_text = entry.get()
#     label.config(text=f"Hello, {entered_text}!")

# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.pack(pady=10)

# # Run the application
# root.mainloop()




import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2)
entry.grid(row=0, column=0, columnspan=4)

# Button widgets
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=evaluate_expression).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
