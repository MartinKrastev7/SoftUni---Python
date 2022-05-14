import math

biscuits_per_worker = int(input())
count_of_workers = int(input())
number_biscuits_competitor = int(input())
biscuits_per_day = 0
biscuits_day_3 = 0

for i in range(1, 31):

    if i % 3 == 0:
        biscuits_day_3 = biscuits_per_worker * 0.75
        biscuits_per_day += biscuits_day_3 * count_of_workers
    else:
        biscuits_per_day += biscuits_per_worker * count_of_workers
    biscuits_per_day = math.floor(biscuits_per_day)


print(f"You have produced {biscuits_per_day} biscuits for the past month.")

if biscuits_per_day > number_biscuits_competitor:
    diff = biscuits_per_day - number_biscuits_competitor
    percent = diff * 100 / number_biscuits_competitor
    print(f"You produce {percent:.2f} percent more biscuits.")

else:
    diff = number_biscuits_competitor - biscuits_per_day
    percent = diff * 100 / number_biscuits_competitor
    print(f"You produce {percent:.2f} percent less biscuits.")