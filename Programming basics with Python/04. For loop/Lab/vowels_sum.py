text = input()
total_sum = 0

for ch in (text):
    if ch == "a":
        total_sum += 1
    if ch == "e":
        total_sum += 2
    if ch == "i":
        total_sum += 3
    if ch == "o":
        total_sum += 4
    if ch == "u":
        total_sum += 5

print(total_sum)