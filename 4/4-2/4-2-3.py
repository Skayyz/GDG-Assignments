import customtkinter 

# calcluating the area of the room in both meter and foot
def calculate_area():
    try:
        # take the input from the user 
        width = float(width_entry.get())
        height = float(height_entry.get())
        unit = unit_var.get()
        
        if unit == "m":  # if the chosen unit is meter
            area_m = width * height
            area_ft = round(area_m / 0.09290304, 2)
        else:  # if the chosen unit is foot
            area_ft = width * height
            area_m = round(area_ft * 0.09290304, 2)
        
        # Display the calculated area in both units
        result_label.configure(text=f"Area in Square Meters: {area_m}\nArea in Square Feet: {area_ft}")
    except ValueError:
        result_label.configure(text="Please enter valid numeric values.")

# GUI start
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title("Rectangular Room Area Calculator")
app.geometry("400x400")

# UI Elements and buttons
unit_var = customtkinter.StringVar(value="m")

width_label = customtkinter.CTkLabel(app, text="Width:")
width_label.pack(pady=5)
width_entry = customtkinter.CTkEntry(app)
width_entry.pack(pady=5)

height_label = customtkinter.CTkLabel(app, text="Height:")
height_label.pack(pady=5)
height_entry = customtkinter.CTkEntry(app)
height_entry.pack(pady=5)

unit_label = customtkinter.CTkLabel(app, text="Select Unit:")
unit_label.pack(pady=5)

unit_frame = customtkinter.CTkFrame(app)
unit_frame.pack(pady=5)

meter_button = customtkinter.CTkRadioButton(unit_frame, text="Meters (m)", variable=unit_var, value="m")
meter_button.pack(side="left", padx=10)

foot_button = customtkinter.CTkRadioButton(unit_frame, text="Feet (ft)", variable=unit_var, value="ft")
foot_button.pack(side="left", padx=10)

calculate_button = customtkinter.CTkButton(app, text="Calculate Area", command=calculate_area)
calculate_button.pack(pady=10)

result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(pady=10)

# Run the app
app.mainloop()
