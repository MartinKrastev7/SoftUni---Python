length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

volume_aquarium = length_cm * width_cm * height_cm
volume_litres = volume_aquarium / 1000
litres_necessary = volume_litres * (1 - percent / 100)

print(litres_necessary)