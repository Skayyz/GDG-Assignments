# 3 | Write a version of the program that displays different greetings for different people.

User_name = str(input("What is your name ?")) # Take input from the user and store in the variable "User_name"
User_name = User_name.capitalize()
Greetings = ''

if (User_name == "Fahad") or (User_name == "Emad") : # if the name is fahad or emad, it will print a different greeting than the rest
    Greetings = "Hello Leader," + f" {User_name}," + " Great to have you here!"
else:
    Greetings = "Hello," + f" {User_name}," + " nice to meet you!" # Include the User name in the variable "User_name" in the Greetings varaible 

print(Greetings) # Print the Greetings statement 