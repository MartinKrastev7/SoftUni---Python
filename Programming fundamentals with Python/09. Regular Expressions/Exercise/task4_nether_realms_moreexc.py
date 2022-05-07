import re

names = input().split(",")
dict_demons = {}


for i in names:
    demon = i.strip()
    health_pattern = r"[^\d\+\-*\/\.]"
    damage_pattern = r"(?:\+|-)?[0-9]+(?:\.[0-9]+)?"
    operator_pattern = r"[\*/]"
    result_health = re.findall(health_pattern, demon)
    health = 0
    for h in result_health:
        health += ord(h)

    damage_result = re.findall(damage_pattern,demon)
    damage = 0
    for x in damage_result:
        damage += float(x)

    operator_result = re.findall(operator_pattern, demon)
    for sign in operator_result:
        if sign == "*":
            damage *= 2
        elif sign == "/":
            damage /= 2

    dict_demons[demon] = [health, damage]

output = {a: b for a, b in sorted(dict_demons.items(), key=lambda x: x[0])}
for key,value in output.items():
    print(f"{key} - {value[0]} health, {value[1]:.2f} damage")