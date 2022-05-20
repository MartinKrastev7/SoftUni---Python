#also known as Sum of 2
ll = map(int,input().split())
target = int(input())
targets = set()
values_map = {}

for value in ll:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f"{p1} + {p2} = {target}")
    else:
        targets.add(target - value)
        values_map[target - value] = value


####
from itertools import combinations

sequence = [int(el) for el in input().split()]
target = int(input())

my_set = set()
iterations = 0

for num in combinations(sequence, 2):
    if num[0] + num[1] == target:
        iterations += 1
        my_set.add((num[0], num[1]))
        print(f"{num[0]} + {num[1]} = {target}")
    else:
        iterations += 1

print(f"Iterations done: {iterations}")
if my_set:
    print(*my_set, sep="\n")