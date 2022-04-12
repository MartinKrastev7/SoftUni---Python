x = float(input())
y = float(input())
h = float(input())

side_wall_size = x * y
window_size = 1.5 * 1.5
two_sides_size = (2 * side_wall_size) - (2 * window_size)
back_wall = x * x
entrance = 1.2 * 2
front_back_wall_size = (2 * back_wall) - entrance
total_area = two_sides_size + front_back_wall_size
green_paint = total_area / 3.4

two_rectangle_floors = 2 * (x * y)
two_triangles = 2 * (x * h / 2)
total_area_floor = two_rectangle_floors + two_triangles
red_paint = total_area_floor / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")