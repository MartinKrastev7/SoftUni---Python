from collections import deque

#cups_capacity = deque([int(x) for x in input().split()]) # queue
#filled_bottles = deque([int(x) for x in input().split()]) # stack
#wasted_water = 0

#while cups_capacity:
#    current_cup = cups_capacity.popleft()
#    current_bottle = filled_bottles.pop()

#    if current_cup <= current_bottle:
#        wasted_water += abs(current_bottle - current_cup)
#    elif current_cup > current_bottle:
 #       while current_cup > 0:
#            current_cup -= current_bottle

#            if current_cup > 0:
#                current_bottle = filled_bottles.pop()

#                if current_bottle > current_cup:
#                    wasted_water += abs(current_bottle - current_cup)
#                    current_cup -= current_bottle
#            else:
#                current_cup -= current_bottle
#    if len(filled_bottles) == 0:
#        break

#if not cups_capacity:
#    print(f"Bottles: {' '.join(str(x) for x in filled_bottles)}")

#else:
#    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")

#print(f"Wasted litters of water: {wasted_water}")

#vtori nachin
cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while bottles and cups:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle < cup:
        cup -= bottle
        cups.appendleft(cup)
    else:
        wasted_water += bottle - cup

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")