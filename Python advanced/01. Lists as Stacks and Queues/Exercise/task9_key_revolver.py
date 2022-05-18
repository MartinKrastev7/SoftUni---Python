from collections import deque

price_of_bullets = int(input())
gun_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
shoots = 0

while bullets:
    shoots += 1
    bullet = bullets.pop()
    lock = locks.popleft()
    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    if shoots % gun_barrel == 0 and bullets:
        print("Reloading!")
    if not locks:
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (shoots * price_of_bullets)}")