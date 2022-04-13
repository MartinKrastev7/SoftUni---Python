from math import pi

shape_type = str(input())

if shape_type == "square":
    size_face_sq = float(input())
    square_surface = size_face_sq * size_face_sq
    print(f"{square_surface:.3f}")
elif shape_type == "rectangle":
    size_face_re1 = float(input())
    size_face_re2 = float(input())
    rectangle_surface = size_face_re1 * size_face_re2
    print(f"{rectangle_surface:.3f}")
elif shape_type == "circle":
    radius = float(input())
    circle_surface = pi * (radius ** 2)
    print(f"{circle_surface:.3f}")
elif shape_type == "triangle":
    size_face_tr = float(input())
    height_tr = float(input())
    triangle_surface = (size_face_tr * height_tr) / 2
    print(f"{triangle_surface:.3f}")
