import tkinter as tk

# Function to handle button clicks
def button_click(value):
    if value == "=":
        try:
            result = str(eval(entry.get()))  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        entry.insert(tk.END, value)  # Append the clicked button's value to the entry field

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying the input and results
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons in a simple list
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+',
    'C'
]

# Create buttons and arrange them in the grid
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
              command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
