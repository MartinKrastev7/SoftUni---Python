time = int(input())
scenes_number = int(input())
scene_time = int(input())

field_preparation = time * 0.15
total_time_scenes = scene_time * scenes_number
time_needed = field_preparation + total_time_scenes
diff = abs(time - time_needed)
diff = round(diff)

if time >= time_needed:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")