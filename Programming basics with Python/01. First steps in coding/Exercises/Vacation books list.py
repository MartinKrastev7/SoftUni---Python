number_of_pages = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())
total_time_for_reading = number_of_pages / pages_for_one_hour
hours_needed_per_day = total_time_for_reading / number_of_days

print(int(hours_needed_per_day))