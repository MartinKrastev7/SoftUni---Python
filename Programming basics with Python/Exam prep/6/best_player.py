import sys

player_name = input()
is_hat_trick = False
max_number = -sys.maxsize
winner = ""
while player_name != "END":
    goals = int(input())

    if goals > max_number:
        max_number = goals
        winner = player_name
    if goals >= 3:
        is_hat_trick = True
    if goals >= 10:
        break

    player_name = input()


print(f"{winner} is the best player!")
if is_hat_trick:
    print(f"He has scored {max_number} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_number} goals.")
