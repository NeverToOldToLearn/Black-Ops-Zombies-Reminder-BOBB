import tkinter as tk

root = tk.Tk()
root.title("BOBB - Zombies Reminder Tool")
root.geometry("300x500")
root.attributes("-alpha", 0.85)
root.attributes("-topmost", True)

# Instructie bovenaan voor betere ruimtebenutting
instruction_label = tk.Label(root, text="Press F1 to check next item", font=("Arial", 8))
instruction_label.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="w")

# Codes to unlock Nathan
code_frame = tk.LabelFrame(root, text="Unlock Codes")
code_frame.grid(row=1, column=0, padx=5, pady=5)

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

# Calculator frame voor Wonder Weapon
calc_frame = tk.LabelFrame(root, text="Calculator")
calc_frame.grid(row=2, column=0, padx=5, pady=5)

# Calculator inputs voor x, y, z
x_label = tk.Label(calc_frame, text="X:")
x_label.grid(row=0, column=0, sticky="w")
x_entry = tk.Entry(calc_frame, width=5)
x_entry.grid(row=0, column=1)

y_label = tk.Label(calc_frame, text="Y:")
y_label.grid(row=1, column=0, sticky="w")
y_entry = tk.Entry(calc_frame, width=5)
y_entry.grid(row=1, column=1)

z_label = tk.Label(calc_frame, text="Z:")
z_label.grid(row=2, column=0, sticky="w")
z_entry = tk.Entry(calc_frame, width=5)
z_entry.grid(row=2, column=1)

# Knop om de berekening uit te voeren
def calculate():
    try:
        x = float(x_entry.get())
        y = float(y_entry.get())
        z = float(z_entry.get())
        result = x + y + z
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input")

calc_button = tk.Button(calc_frame, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=5)

# Resultaatveld voor de calculator
result_label = tk.Label(calc_frame, text="Result:")
result_label.grid(row=4, column=0, sticky="w")
result_entry = tk.Entry(calc_frame, width=10)
result_entry.grid(row=4, column=1)

# Checklist voor WonderWeapon Parts
parts_frame = tk.LabelFrame(root, text="WonderWeapon Parts")
parts_frame.grid(row=3, column=0, padx=5, pady=5)

# Checkbox opties
part_items = [
    "1st Boss - EMF-Fob", "1st Boss - Injector", "1st Boss - AMP-Munition",
    "Main Boss - Key-Card", "Main Boss - Com-Room PC", "Main Boss - Pipes",
    "Main Boss - Hacking Device", "HackBuoys 1", "HackBuoys 2",
    "HackBuoys 3", "Bomb Defusion"
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

def check_next_item(event=None):
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
root.bind("<F1>", check_next_item)

root.mainloop()
