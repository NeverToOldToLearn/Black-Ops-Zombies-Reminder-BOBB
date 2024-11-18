import tkinter as tk
from tkinter import messagebox

# Initialize the main Tkinter window
root = tk.Tk()
root.title("BOBB - Zombies Reminder Tool")
root.geometry("200x700")  # Compact wide length
root.attributes('-alpha', 0.75)  # 75% transparant
root.attributes("-topmost", True)  # Always on top
def apply_dark_theme(widget):
    widget.configure(bg="#4B0082", fg="#4B0082", highlightbackground="#008B8B", highlightcolor="#008B8B")
# Codes to unlock Nathan
code_frame = tk.LabelFrame(root, text="Unlock Codes")
code_frame.grid(row=0, column=0, padx=5, pady=5)

# Clock en Playcard naast elkaar
clock_label = tk.Label(code_frame, text="Clock:")
clock_label.grid(row=0, column=0, sticky="w")
clock_entry = tk.Entry(code_frame, width=5)
clock_entry.grid(row=0, column=1)

playcard_label = tk.Label(code_frame, text="Playcard:")
playcard_label.grid(row=0, column=2, sticky="w")
playcard_entry = tk.Entry(code_frame, width=5)
playcard_entry.grid(row=0, column=3)

days_label = tk.Label(code_frame, text="Days:")
days_label.grid(row=1, column=0, sticky="w")
days_entry = tk.Entry(code_frame, width=5)
days_entry.grid(row=1, column=1)
# Function to perform the calculation and display up to three results
def calculate_results():
    try:
        x_value = int(entry_x.get())
        y_value = int(entry_y.get())
        z_value = int(entry_z.get())
        
        # Basisberekeningen als voorbeeld, pas deze gerust aan
        result1 = abs(2 * x_value + 11)
        result2 = abs(2 * z_value + y_value - 5)
        result3 = abs(y_value + z_value - x_value)

        # Display the results
        result_1_label.config(text=f"Result 1: {result1}")
        result_2_label.config(text=f"Result 2: {result2}")
        result_3_label.config(text=f"Result 3: {result3}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for X, Y, and Z.")
def minimize_to_taskbar():
    root.iconify()
# Calculator frame voor Wonder Weapon
calc_frame = tk.LabelFrame(root, text="Calculator")
calc_frame.grid(row=1, column=0, padx=5, pady=5)

calc_label = tk.Label(calc_frame, text="Input:")
calc_label.grid(row=0, column=0, sticky="w")
entry_x = tk.Entry(calc_frame, width=10)
entry_x.grid(row=0, column=1)

entry_y = tk.Entry(calc_frame, width=10)
entry_y.grid(row=1, column=1)

entry_z = tk.Entry(calc_frame, width=10)
entry_z.grid(row=2, column=1)

# Labels for input fields
tk.Label(calc_frame, text="X Value:").grid(row=0, column=0, sticky="e")
tk.Label(calc_frame, text="Y Value:").grid(row=1, column=0, sticky="e")
tk.Label(calc_frame, text="Z Value:").grid(row=2, column=0, sticky="e")

# Calculate button
calculate_button = tk.Button(calc_frame, text="Calculate", command=calculate_results,)
calculate_button.grid(row=3, columnspan=2, pady=10,)



# Result labels
result_1_label = tk.Label(calc_frame, text="Result 1: -")
result_1_label.grid(row=4, columnspan=2)

result_2_label = tk.Label(calc_frame, text="Result 2: -")
result_2_label.grid(row=5, columnspan=2)

result_3_label = tk.Label(calc_frame, text="Result 3: -")
result_3_label.grid(row=6, columnspan=2)

# Checklist voor WonderWeapon Parts
parts_frame = tk.LabelFrame(root, text="WonderWeapon Parts")
parts_frame.grid(row=3, column=0, padx=5, pady=5)

# Checkbox opties
part_items = [
    "EMF-Fob", "Injector", "AMP-Munition", "HardDrive",
    "Nathan Key-Card", "Com-Room PC", "Repair-Pipes",
    " (Peck) Hacking Device", "HackBuoys 1", "HackBuoys 2",
    "HackBuoys 3", "Bomb Defusion", "Ready up and start main boss"
]

# Maak checkboxes voor onderdelen
part_vars = []
for idx, part in enumerate(part_items):
    var = tk.IntVar()
    chk = tk.Checkbutton(parts_frame, text=part, variable=var)
    chk.grid(row=idx, column=0, sticky="w")
    part_vars.append(var)

# Functie om door checklist te navigeren met F1
current_index = 0  # Houdt bij welk item als laatste is aangevinkt

def check_next_item( ):
    global current_index
    for i in range(len(part_vars)):
        index = (current_index + i) % len(part_vars)
        if part_vars[index].get() == 0:  # Zoek het eerstvolgende niet-afgevinkte item
            part_vars[index].set(1)
            current_index = index + 1  # Update de index
            break
    else:
        # Als alles is afgevinkt, reset naar begin
        for var in part_vars:
            var.set(0)
        current_index = 0

# Bind de F1-toets aan de functie
root.bind('<F1>', check_next_item(  ))
# Bind F2 key to toggle visibility of the window
root.bind('<F2>', lambda event: minimize_to_taskbar())

# Additional instructions
instruction_label = tk.Label(root, text="Press F1 to check next item", font=("Arial", 8))
instruction_label.grid(row=8, column=0, padx=5, pady=(5, 0), sticky="w")
instructions_label = tk.Label(root, text="Press F2 to toggle BOBB visibility", font=("Arial", 8))
instructions_label.grid(row=7, column=0, padx=5, pady=(5, 0), sticky="w")


# Run the main application loop
root.mainloop()
