from collections import deque

quantity_food = int(input())
quantity_food_order = [int(x) for x in input().split(" ")]
#queue_orders = deque(map(int, input().split(" ")))
queue_orders = deque(quantity_food_order)

print(max(queue_orders))
while queue_orders:
    if quantity_food < queue_orders[0]:
        break
    quantity_food -= queue_orders.popleft()

if queue_orders:
    print(f"Orders left: {' '.join(map(str,queue_orders))}")
else:
    print("Orders complete")