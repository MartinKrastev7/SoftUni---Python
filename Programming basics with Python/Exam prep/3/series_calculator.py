import math

serial_name = input()
seasons_number = int(input())
episodes_number = int(input())
episode_length_without_ads = int(input())

ads_length = 0.2 * episode_length_without_ads
episode_with_ads = episode_length_without_ads + ads_length
additional_time_special_episode = seasons_number * 10
total = episode_with_ads * episodes_number * seasons_number + additional_time_special_episode
total = math.floor(total)
print(f"Total time needed to watch the {serial_name} series is {total} minutes.")