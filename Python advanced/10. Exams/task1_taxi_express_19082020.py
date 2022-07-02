from collections import deque

customers_time = deque([int(x) for x in input().split(", ")])
taxis_time = [int(x) for x in input().split(", ")]
total_time = 0
is_ran_out_taxis = False

while customers_time:
    if len(taxis_time) <= 0:
        is_ran_out_taxis = True
        break

    current_customer = customers_time.popleft()
    current_taxi = taxis_time.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers_time.appendleft(current_customer)


if not customers_time:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
if is_ran_out_taxis:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers_time])}")

