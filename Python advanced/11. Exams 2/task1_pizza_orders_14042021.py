from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacity = [int(x) for x in input().split(", ")]
made_pizzas = 0

while pizza_orders and employees_capacity:
    current_order = pizza_orders.popleft()
    current_capacity = employees_capacity.pop()

    if 0 >= current_order or current_order > 10:
        employees_capacity.append(current_capacity)
        continue

    if current_order <= current_capacity:
        made_pizzas += current_order
    elif current_order > current_capacity:
        diff = current_order - current_capacity
        made_pizzas += current_capacity
        pizza_orders.appendleft(diff)

if employees_capacity:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {made_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees_capacity])}")

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")