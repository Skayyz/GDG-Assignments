# Area of a Rectangular Room
import math
room_width = 0
room_height = 0

def calculate_the_area_of_the_room(width, height, unit) : # calcluating the area of the room in both meter and foot
    if unit == "m" : # if the choosen unit is meter
        area_in_sm = width * height 
        area_in_sf = round((area_in_sm) / 0.09290304,2) 
    else :
        area_in_sf = width * height # if the choosen unit is foot
        area_in_sm = round((area_in_sf) * 0.09290304,2) 
    return area_in_sm, area_in_sf

# get the input unit from the user
input_unit = ''
while True:
    input_unit = str(input("m | meter\nft | foot\nWhat unit do you want to use ? ")).lower()
    if input_unit == "m" or input_unit == "ft" :
        break
    
    print("Please enter (m) for meters or (ft) for foot")

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
area_of_the_room = calculate_the_area_of_the_room(room_width, room_height,input_unit)

# printing the area values
print(f"Square meter | {area_of_the_room[0]}\nSquare foot | {area_of_the_room[1]}")
