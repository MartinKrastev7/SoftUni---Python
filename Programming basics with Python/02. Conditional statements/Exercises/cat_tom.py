holidays = int(input())

time_for_play_holidays = holidays * 127
working_days = 365 - holidays
time_for_play_working_days = working_days * 63
total_time_for_playing = time_for_play_holidays + time_for_play_working_days
playing_norm = 30000

if total_time_for_playing > playing_norm:
    difference_minutes = total_time_for_playing - playing_norm
    hour_difference = difference_minutes // 60
    minute_difference = difference_minutes % 60
    print("Tom will run away")
    print(f"{hour_difference} hours and {minute_difference} minutes more for play")
else:
    minutes_left = playing_norm - total_time_for_playing
    hour_difference = minutes_left // 60
    minute_difference = minutes_left % 60
    print("Tom sleeps well")
    print(f"{hour_difference} hours and {minute_difference} minutes less for play")
