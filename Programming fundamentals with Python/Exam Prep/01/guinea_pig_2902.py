food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight_kg = float(input())

food_gr = food_kg * 1000
hay_gr = hay_kg * 1000
cover_gr = cover_kg * 1000
weight_gr = weight_kg * 1000
is_out_of = False

for i in range(1, 31):
    food_gr -= 300
    if i % 2 == 0:
        hay_gr -= food_gr * 0.05
    if i % 3 == 0:
        cover_gr -= weight_gr / 1/3
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        is_out_of = True
        print("Merry must go to the pet store!")
        break

if not is_out_of:
    food_gr /= 1000
    hay_gr /= 1000
    cover_gr /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_gr:.2f}, Hay: {hay_gr:.2f}, Cover: {cover_gr:.2f}.")