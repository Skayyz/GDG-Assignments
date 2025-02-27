# 6 | Implement this program using a graphical user interface and updatethe character counter every time a key is pressed.

import tkinter 

def update_label(event): # The main goal of this function is to check if any characters added and update the counter based on the length of the input string
    input_text = entry.get()  # Get the current inputted string
    char_count = len(input_text) # get the length of it
    output_label.config(text=f"You entered: {input_text}\nCharacter count: {char_count}") # update the counter alongside with name (if changed)

# First we create a the main GUI window

gui = tkinter.Tk()
gui.title("Character Counter")
gui.geometry("500x200")

# Then we need to create the lables, widgets, and textbox needed
label = tkinter.Label(gui, text="Enter your name : ") # creating the label for the input of the user
label.pack(pady=5)

entry = tkinter.Entry(gui, width=40) # creating the textbox for the input
entry.pack(pady=5)
entry.bind("<KeyRelease>", update_label) # Whenever a key is realeased, it will go to the function "update_label"

output_label = tkinter.Label(gui, text="You entered: \nCharacter count: ") # Create lables for the entered string + the character counter
output_label.pack(pady=15)

# After creating the widgets, Run the GUI
gui.mainloop()
