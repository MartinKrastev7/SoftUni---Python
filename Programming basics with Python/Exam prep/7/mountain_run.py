import math

record_seconds = float(input())
distance_m = float(input())
time_seconds_for_1m = float(input())

time_for_distance_seconds = distance_m * time_seconds_for_1m
delay_m = distance_m / 50
delay_m = math.floor(delay_m)
delay_for_50m = delay_m * 30
total_time = time_for_distance_seconds + delay_for_50m
diff = abs(record_seconds - total_time)

if total_time < record_seconds:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")