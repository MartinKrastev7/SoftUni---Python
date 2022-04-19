number_game_sales = int(input())
percent_hearthstone = 0
percent_fornite = 0
percent_overwatch = 0
percent_others = 0
count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
countr_others = 0

for game in range(1, number_game_sales + 1):
    game_name = input()

    if game_name == "Hearthstone":
        count_hearthstone += 1
        percent_hearthstone = count_hearthstone * 100 / number_game_sales
    elif game_name == "Fornite":
        count_fornite += 1
        percent_fornite = count_fornite * 100 / number_game_sales
    elif game_name == "Overwatch":
        count_overwatch += 1
        percent_overwatch = count_overwatch * 100 / number_game_sales
    else:
        countr_others += 1
        percent_others = countr_others * 100 / number_game_sales

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")