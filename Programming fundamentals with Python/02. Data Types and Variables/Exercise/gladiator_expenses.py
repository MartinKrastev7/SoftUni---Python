lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repair = 0
sword_repair = 0
shield_repair = 0
armor_repair = 0
shield_break_count = 0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        helmet_repair += helmet_price
    if i % 3 == 0:
        sword_repair += sword_price
        if i % 2 == 0:
            shield_repair += shield_price
            shield_break_count += 1
            if shield_break_count == 2:
                armor_repair += armor_price
                shield_break_count = 0

total = helmet_repair + sword_repair + shield_repair + armor_repair

print(f"Gladiator expenses: {total:.2f} aureus")