import math

days = int(input())
km_first_day = float(input())

total_km = km_first_day


for day in range(1, days + 1):
    percent_increase = int(input())
    km_first_day *= 1 + percent_increase / 100
    total_km += km_first_day

diff = abs(1000 - total_km)
diff = math.ceil(diff)
if total_km >= 1000:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")