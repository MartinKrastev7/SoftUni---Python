sum = float(input())
sum = int(sum * 100)
coins_counter = 0
coins_counter += sum // 200
sum %= 200
coins_counter += sum // 100
sum %= 100
coins_counter += sum // 50
sum %= 50
coins_counter += sum // 20
sum %= 20
coins_counter += sum // 10
sum %= 10
coins_counter += sum // 5
sum %= 5
coins_counter += sum // 2
sum %= 2
coins_counter += sum // 1
sum %= 1
print(coins_counter)


########### sus while cikul
while sum > 0:
    if sum - 200 >= 0:
        coins_counter += 1
        sum -= 200
        continue
    elif sum - 100 >= 0:
        coins_counter += 1
        sum -= 100
        continue