numbers = [int(x) for x in input().split(" ")]

x = sorted(numbers, reverse=False)

print(list(x))

# vtoro reshenie
result = sorted(list(map(int, input().split(" "))))