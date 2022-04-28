card = input().split()

list_team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_less = False

for el in card:
    element = el.split("-")
    team = element[0]
    player = int(element[1])
    if team == "A":
        if player in list_team_A:
            list_team_A.remove(player)
    elif team == "B":
        if player in list_team_B:
            list_team_B.remove(player)
    if len(list_team_A) < 7 or len(list_team_B) < 7:
        is_less = True
        break

print(f"Team A - {len(list_team_A)}; Team B - {len(list_team_B)}")

if is_less:
    print("Game was terminated")

#vtoro reshenie
info = input().split(" ")
team_a_players = 11
team_b_players = 11

player_loses = []
condition = False
for card in info:
    if card not in player_loses:
        player_loses.append(card)
        if "A" in card:
            team_a_players -= 1
        elif "B" in card:
            team_b_players -= 1

        if team_a_players < 7 or team_b_players < 7:
            condition = True
            break

print(f"Team A - { team_a_players}; Team B - {team_b_players}")
if condition:
    print("Game was terminated ")


