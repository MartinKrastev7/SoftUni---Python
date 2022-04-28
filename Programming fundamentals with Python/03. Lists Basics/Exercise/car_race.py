numbers = input().split(" ")
middle = len(numbers) // 2
left_time = 0
right_time = 0
winner = ""
left_side = numbers[:middle]
right_side = numbers[-1:middle:-1]

for i in left_side:
    current_time = int(i)
    left_time += current_time
    if i == "0":
        left_time *= 0.8

for j in right_side:
    current_time = int(j)
    right_time += current_time
    if j == "0":
        right_time *= 0.8

if left_time < right_time:
    winner = "left"
    print(f"The winner is {winner} with total time: {left_time:.1f}")
elif left_time > right_time:
    winner = "right"
    print(f"The winner is {winner} with total time: {right_time:.1f}")


