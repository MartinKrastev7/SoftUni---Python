town_name = input()
type_packet = input()
vip_have = input()
days = int(input())

price_for_day = 0
total_price = 0

if days > 7:
    days -= 1

if not (town_name in ("Bansko", "Borovets") and type_packet in ("noEquipment", "withEquipment",)) and not (
        town_name in ("Varna", "Burgas") and type_packet in ("noBreakfast", "withBreakfast")):
    print(f'Invalid input!')

elif days < 1:
    print(f'Days must be positive number!')

else:
    if town_name == "Bansko" or town_name == "Borovets":
        if type_packet == "withEquipment":
            price_for_day = 100
            total_price = days * price_for_day
            if vip_have == "yes":
                total_price *= 0.90
        elif type_packet == "noEquipment":
            price_for_day = 80
            total_price = days * price_for_day
            if vip_have == "yes":
                total_price *= 0.95

    elif town_name == "Varna" or town_name == "Burgas":
        if type_packet == "withBreakfast":
            price_for_day = 130
            total_price = days * price_for_day
            if vip_have == "yes":
                total_price *= 0.88
        elif type_packet == "noBreakfast":
            price_for_day = 100
            total_price = days * price_for_day
            if vip_have == "yes":
                total_price *= 0.93

    print(f'The price is {total_price:.2f}lv! Have a nice time!')
