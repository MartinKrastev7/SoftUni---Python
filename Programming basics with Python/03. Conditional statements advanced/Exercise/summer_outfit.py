degree = int(input())
type_of_day = input()
Outfit = ""
Shoes = ""

if 10 <= degree <=18:
    if type_of_day == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif type_of_day == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif type_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
elif 18 < degree <= 24:
    if type_of_day == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif type_of_day == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif type_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
elif degree >= 25:
    if type_of_day == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif type_of_day == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif type_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
