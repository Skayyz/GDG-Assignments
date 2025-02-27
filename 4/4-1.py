# Retirement Calculator
from datetime import date

# Defining the current year 
current_year = int(date.today().year)

# Getting user current age and retirement age
user_age = int(input("What is your age now ? "))
retirement_age = int(input("At what age will you retire ? "))

if ((retirement_age - user_age) <= 0) : # To check if user can already retire if his age equals or more than the age he wants to retire
    print("You can already retire")
    exit(1)

# defining variables 
retirement_year = current_year + (retirement_age - user_age)

# printing the number of years left before retirement and the year of retirement
print(f"You have {retirement_year - current_year} years until you retire.\nit's {current_year}, you can retire at {retirement_year}")