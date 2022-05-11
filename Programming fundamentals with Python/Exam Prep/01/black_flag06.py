days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
is_reached = False
gathered_plunder = 0

for day in range(1, days + 1):
    gathered_plunder += daily_plunder

    if day % 3 == 0:
        extra_plunder = daily_plunder * 0.5
        gathered_plunder += extra_plunder
    if day % 5 == 0:
        gathered_plunder = gathered_plunder - (gathered_plunder * 0.3)

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    percent = gathered_plunder * 100 / expected_plunder
    print(f"Collected only {percent:.2f}% of the plunder.")
