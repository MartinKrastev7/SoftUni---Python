country = input()
tool = input()
level_number = 0
execution = 0
total_points = 0
percent = 0
points_diff = 0

if tool == "ribbon":
    if country == "Russia":
        level_number = 9.100
        execution = 9.400
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
    elif country == "Bulgaria":
        level_number = 9.600
        execution = 9.400
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
    elif country == "Italy":
        level_number = 9.200
        execution = 9.500
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
elif tool == "hoop":
    if country == "Russia":
        level_number = 9.300
        execution = 9.800
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
    elif country == "Bulgaria":
        level_number = 9.550
        execution = 9.750
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
    elif country == "Italy":
        level_number = 9.450
        execution = 9.350
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
elif tool == "rope":
    if country == "Russia":
        level_number = 9.600
        execution = 9.000
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
    elif country == "Bulgaria":
        level_number = 9.500
        execution = 9.400
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20
    elif country == "Italy":
        level_number = 9.700
        execution = 9.150
        total_points = level_number + execution
        points_diff = 20 - total_points
        percent = points_diff * 100 / 20

print(f"The team of {country} get {total_points:.3f} on {tool}.")
print(f"{percent:.2f}%")