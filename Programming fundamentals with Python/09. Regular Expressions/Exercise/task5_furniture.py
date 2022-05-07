import re

furniture = []
total_sum = 0

while True:
    text = input()
    if text == "Purchase":
        break

    pattern = r"\>>(?P<furniture>[A-Za-z]+)\<<(?P<price>\d+([\.]?)\d+)\!(?P<quantity>\d+)"

    result = re.finditer(pattern, text)

    for match in result:
        furniture.append(match.group("furniture"))
        total_sum += float(match.group("price")) * int(match.group("quantity"))

print("Bought furniture:")

for i in furniture:
    print(i)

print(f"Total money spend: {total_sum:.2f}")

#vtori nachin
def furniture_info():
    pattern = r">>([A-Za-z]+)<<(\d+|\d+\.\d+)!(\d+)"
    spend_money = 0
    product_list = []

    while True:
        data = input()

        if data == "Purchase":
            break

        result = re.match(pattern, data)

        if result is not None:
            product = result[1]
            price = float(result[2])
            quantity = int(result[3])
            spend_money += price * quantity
            product_list.append(product)

    print("Bought furniture:")

    if spend_money > 0:
        print("\n".join(product_list))
    print(f"Total money spend: {spend_money:.2f}")

furniture_info()