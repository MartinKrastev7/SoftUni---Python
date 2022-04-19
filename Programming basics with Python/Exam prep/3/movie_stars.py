budget = float(input())
is_finished = False
command = input()

while command != "ACTION":
    if len(command) <= 15:
        reward = float(input())
        budget -= reward
    else:
        budget *= 0.80
    if budget <= 0:
        is_finished = True
        break


    command = input()

if is_finished:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")