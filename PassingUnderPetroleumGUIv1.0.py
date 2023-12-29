import tkinter as tk

def calculate_laps():
    lapsRun = float(laps_run_entry.get())
    galStart = float(gal_start_entry.get())
    galRem = float(gal_rem_entry.get())

    galUsed = galStart - galRem
    lapGal = round((lapsRun / galUsed), 1)
    lapTank = round((lapGal * galStart), 1)

    result_label.config(text=f"Laps per gallon: {lapGal}\nLaps per Tank: {lapTank}")

# Create the main window
root = tk.Tk()
root.title("Laps Calculator")

# Create input fields
laps_run_label = tk.Label(root, text="Laps run:")
laps_run_label.pack()
laps_run_entry = tk.Entry(root)
laps_run_entry.pack()

gal_start_label = tk.Label(root, text="Gallons start:")
gal_start_label.pack()
gal_start_entry = tk.Entry(root)
gal_start_entry.pack()

gal_rem_label = tk.Label(root, text="Gallons remaining:")
gal_rem_label.pack()
gal_rem_entry = tk.Entry(root)
gal_rem_entry.pack()

# Button to calculate laps
calculate_button = tk.Button(root, text="Calculate", command=calculate_laps)
calculate_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter main loop
root.mainloop()
