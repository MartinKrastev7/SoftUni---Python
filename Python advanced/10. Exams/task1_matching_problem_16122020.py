from collections import deque

males = [int(x) for x in input().split(" ")]
female = deque([int(x) for x in input().split(" ")])
matches = 0

while males and female:
    current_male = males.pop()
    current_female = female.popleft()

    if current_male <= 0:
        female.appendleft(current_female)
        continue
    elif current_female <= 0:
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        males.pop()
        female.appendleft(current_female)
        continue
    elif current_female % 25 == 0:
        female.popleft()
        males.append(current_male)
        continue

    if current_male == current_female:
        matches += 1
    else:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches}")
if males:
    males = males[::-1]
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print("Males left: none")

if female:
    print(f"Females left: {', '.join([str(x) for x in female])}")
else:
    print("Females left: none")