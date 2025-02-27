# Area of a Rectangular Room
import math

def calculate_the_area_of_the_room(width, height) : # calcluating the area of the room in both meter and square
    area_in_sm = width * height # the area in square meter
    area_in_sf = round((area_in_sm) / 0.09290304,2) # calculate the area in square foot
    return area_in_sm, area_in_sf


# get the width and the height of the room from the user
while(True):
    try :
        room_width = int(input("What is the room's width ? "))
        room_height = int(input("What is the room's height ? "))
        break
    except :
        print("Must be numric values")
        
# printing the dimension entered by the users
print (f"You entered dimensions {room_width} x {room_height}")

# defining and getting the area of the room in both meter and square
area_of_the_room = calculate_the_area_of_the_room(room_width, room_height)

# printing the area values
print(f"Square meter | {area_of_the_room[0]}\nSquare foot | {area_of_the_room[1]}")
