# 5 | If the user enters nothing, state that the user must enter something into the program.

def Print_total(string): # This function will print the number of characters of the inputted name 
    print(f"{string} has {len(string)} characters")
    exit(1)
    
while True : # The main loop of the program
    User_name = str(input("What is your name ?")) # Take the name of user
    print("You must enter something!") if (len(User_name) <= 0) else Print_total(User_name) # If the name is empty, it will print an error message, else will print the number of the characters


