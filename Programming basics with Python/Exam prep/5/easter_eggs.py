import sys

eggs_painted = int(input())
count_red = 0
count_orange = 0
count_blue = 0
count_green = 0
max_count = -sys.maxsize
max_colour = ""
for egg in range(1, eggs_painted + 1):
    colour = input()

    if colour == "red":
        count_red += 1
        if count_red > max_count:
            max_count = count_red
            max_colour = colour
    elif colour == "orange":
        count_orange += 1
        if count_orange > max_count:
            max_count = count_orange
            max_colour = colour
    elif colour == "blue":
        count_blue += 1
        if count_blue > max_count:
            max_count = count_blue
            max_colour = colour
    elif colour == "green":
        count_green += 1
        if count_green > max_count:
            max_count = count_green
            max_colour = colour

print(f"Red eggs: {count_red}")
print(f"Orange eggs: {count_orange}")
print(f"Blue eggs: {count_blue}")
print(f"Green eggs: {count_green}")
print(f"Max eggs: {max_count} -> {max_colour}")



