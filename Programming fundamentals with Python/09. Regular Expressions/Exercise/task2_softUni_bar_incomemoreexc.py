import re
lines = input()
total = 0

while lines != "end of shift":

    pattern = r"\%(?P<name>[A-Z][a-z]+)\%[^\|\$\%\.]*?\<(?P<product>\w+)\>[^\|\$\%\.]*?\|(?P<count>[0-9]+)\|[\w\-]*?" \
              r"(?P<price>[0-9.]+[0-9])(?=\$)"

    result = re.finditer(pattern, lines)

    for match in result:
        price_current = float(match.group("price")) * int(match.group("count"))
        total += price_current
        print(f"{match.group('name')}: {match.group('product')} - {price_current:.2f}")


    lines = input()

print(f"Total income: {total:.2f}")