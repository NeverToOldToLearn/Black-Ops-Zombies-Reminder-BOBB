import tkinter as tk
from tkinter import messagebox

def calculate_results():
    try:
        x_value = int(entry_x.get())
        y_value = int(entry_y.get())
        z_value = int(entry_z.get())
        
        result1 = abs(2 * x_value + 11)
        result2 = abs(2 * z_value + y_value - 5)
        result3 = abs(y_value + z_value - x_value)
        
        result_label.config(text=f"Result 1: {result1:02d}\nResult 2: {result2:02d}\nResult 3: {result3:02d}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers for X, Y, and Z.")

# Create the main window
root = tk.Tk()
root.title("gui_Bo6BackPack")
root.attributes("-topmost", True)

# Make the GUI draggable
def start_drag(event):
    x = event.x
    y = event.y
    def drag(event):
        root.geometry(f"+{event.x_root - x}+{event.y_root - y}")
    root.bind("<B1-Motion>", drag)

root.bind("<Button-1>", start_drag)

# Create input fields
tk.Label(root, text="X:").grid(row=0, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

tk.Label(root, text="Y:").grid(row=1, column=0)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1)

tk.Label(root, text="Z:").grid(row=2, column=0)
entry_z = tk.Entry(root)
entry_z.grid(row=2, column=1)

# Create a button to calculate results
calculate_button = tk.Button(root, text="Calculate", command=calculate_results)
calculate_button.grid(row=3, columnspan=2)

# Explanation Label (using grid)
explanation = tk.Label(root, text="*Symbol Guide: Find the shapes, and look to the left for the first number. "
                                  "Then look down vertically from that same image, and find the next number. "
                                  "Add them together and fill them in.", wraplength=300)
explanation.grid(row=4, column=0, columnspan=2)

# Create a label to display results
result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

# Slot number entries
tk.Label(root, text="Enter slot numbers:").grid(row=6, column=0, columnspan=2)
entry1 = tk.Entry(root, width=3)
entry2 = tk.Entry(root, width=3)
entry3 = tk.Entry(root, width=3)
entry1.grid(row=7, column=0)
entry2.grid(row=7, column=1)
entry3.grid(row=7, column=2)

# Start the GUI event loop
root.mainloop()
