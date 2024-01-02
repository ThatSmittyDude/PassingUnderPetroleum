#PassingUnderPetroleumGUIv1.4
#Author: Austin Smith
#Email: ThatSmittyDude@outlook.com
#github.com/ThatSmittyDude
#Unix Timestamp: 1704143032

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def calculate_laps(event=None):
    lapsRun = float(entry_laps.get())
    galStart = float(entry_gallons_start.get())
    galRem = float(entry_gallons_remaining_entry.get())

    galUsed = galStart - galRem
    lapGal = round((lapsRun / galUsed), 1)
    lapTank = round((lapGal * galStart), 1)

    label_result_laps_per_gallon.configure(text=f"Laps per gallon: {lapGal}")
    label_result_laps_per_tank.configure(text=f"Laps per Tank: {lapTank}")

# Create the main window
root = customtkinter.CTk()
root.geometry("650x450")

# Create a frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Create entry widgets
label_laps = customtkinter.CTkLabel(master=frame, text="Laps run:")
label_laps.pack(pady=5)
entry_laps = customtkinter.CTkEntry(master=frame, width=400)
entry_laps.pack(pady=5)
label_gallons_start = customtkinter.CTkLabel(master=frame, text="Gallons start:")
label_gallons_start.pack(pady=5)
entry_gallons_start = customtkinter.CTkEntry(master=frame, width=400)
entry_gallons_start.pack(pady=5)
label_gallons_remaining = customtkinter.CTkLabel(master=frame, text="Gallons remaining:")
label_gallons_remaining.pack(pady=5)
entry_gallons_remaining_entry = customtkinter.CTkEntry(master=frame, width=400)
entry_gallons_remaining_entry.pack(pady=5)

# Create a button to calculate laps
button_calculate = customtkinter.CTkButton(master=frame, text="Calculate Laps", command=calculate_laps)
button_calculate.pack(pady=10)

# Create result labels
label_result_laps_per_gallon = customtkinter.CTkLabel(master=frame, text="Laps per gallon:")
label_result_laps_per_gallon.pack(pady=5)
label_result_laps_per_tank = customtkinter.CTkLabel(master=frame, text="Laps per Tank:")
label_result_laps_per_tank.pack(pady=5)

# Bind the Enter key to the calculate_laps function
root.bind('<Return>', lambda event=None: button_calculate.invoke())

root.mainloop()

