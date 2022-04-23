number_days = int(input())
money_win = 0
money_lose = 0
win_count = 0
lose_count = 0
win_count_current = 0
lose_count_current = 0
current_money = 0


for day in range(1, number_days + 1):
    sport = input()
    win_count_current = 0
    lose_count_current = 0
    current_money = 0

    while sport != "Finish":
        result = input()

        if result == "win":
            win_count += 1
            money_win += 20
            current_money += 20
            win_count_current += 1
        elif result == "lose":
            lose_count += 1
            money_lose = 0
            lose_count_current += 1

        sport = input()
    if win_count_current > lose_count_current:
       money_win += (current_money * 0.1)

if win_count > lose_count:
    money_win +=money_win * 0.2
    print(f"You won the tournament! Total raised money: {money_win:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_win:.2f}")




