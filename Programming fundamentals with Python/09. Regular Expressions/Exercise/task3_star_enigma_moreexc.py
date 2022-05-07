import re

number = int(input())
attacked = []
destroyed = []


for i in range(1, number + 1):
    lines = input()
    names = ""
    first_pattern = r"[starSTAR]"
    result = re.findall(first_pattern, lines)
    remove_count = int(len(result))

    for j in lines:
        after = ord(j) - remove_count
        names += "".join(chr(after))

    second_pattern = r".*\@(?P<planet>[A-Za-z]+)[^\@\-\!\:\>]*\:(?P<population>\d+)[^\@\-\!\:\>]*\!(?P<attack>[AD]+)\!"\
                     r"[^\@\-\!\:\>]*\->(?P<count>\d+).*"
    second_result = re.finditer(second_pattern, names)
    for match in second_result:
        if match.group("attack") == "A":
            attacked.append(match.group("planet"))
        elif match.group("attack") == "D":
            destroyed.append(match.group("planet"))

print(f"Attacked planets: {len(attacked)}")
attacked.sort()
for i in attacked:
    print(f"-> {i}")

print(f"Destroyed planets: {len(destroyed)}")
destroyed.sort()
for j in destroyed:
    print(f"-> {j}")

