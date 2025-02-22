import tkinter as tk

# Function to update the expression in the entry field
def update_expression(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

# Function to evaluate the expression and display the result
def evaluate_expression(event=None):
    try:
        current_text = entry.get()
        result = str(eval(current_text))  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear_expression(event=None):
    entry.delete(0, tk.END)

# Function to handle key presses
def key_handler(event):
    if event.char.isdigit() or event.char in '+-*/.':
        update_expression(event.char)
    elif event.keysym == 'Return':
        evaluate_expression()
    elif event.keysym == 'BackSpace':
        entry.delete(len(entry.get())-1, tk.END)

# Creating the main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the expression and result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Bind keys to the main window
root.bind('<Key>', key_handler)
root.bind('<Return>', evaluate_expression)
root.bind('<Escape>', clear_expression)

# Button layout for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons in the window
row_value = 1
col_value = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 18), command=lambda x=button_text: update_expression(x) if x != '=' else evaluate_expression())
    button.grid(row=row_value, column=col_value, ipadx=10, ipady=10, sticky="nsew")
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Clear button
clear_button = tk.Button(root, text='C', font=('Arial', 18), command=clear_expression)
clear_button.grid(row=row_value, column=0, ipadx=10, ipady=10, sticky="nsew")

# Adjust column and row weight for resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
