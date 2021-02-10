"""Joseph Nguyen PSID: 1779987"""
# zyLabs 3.18.1 #

import math

wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_height*wall_width
print("Wall area:", wall_area, "square feet")
paint_needed = wall_area/350
print("Paint needed:", '{:.2f}'.format(paint_needed), "gallons")
cans_needed = math.ceil(paint_needed)
print("Cans needed:", cans_needed, "can(s)\n")

color = input("Choose a color to paint the wall:\n")
price = 0
if color == "red":
    price = 35*cans_needed
elif color == "blue":
    price = 25*cans_needed
elif color == "green":
    price = 23*cans_needed
print("Cost of purchasing", color, "paint: $"+str(price))
