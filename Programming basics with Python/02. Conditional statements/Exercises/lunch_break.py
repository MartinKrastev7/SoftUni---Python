from math import ceil

serial_name = str(input())
episode_time = int(input())
break_time = int(input())

lunch_time = break_time * 1/8
rest_time = break_time * 1/4
time_left = break_time - lunch_time - rest_time
free_time = abs(time_left - episode_time)
free_time = ceil(free_time)

if time_left >= episode_time:
    print(f"You have enough time to watch {serial_name} and left with {free_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {free_time} more minutes.")

