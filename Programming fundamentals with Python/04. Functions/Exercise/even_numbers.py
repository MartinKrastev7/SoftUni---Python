numbers = [int(x) for x in input().split(" ")]

even = filter(lambda evens: evens % 2 == 0, numbers)

print(list(even))

#vtoro reshenie
result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))

#treto
def check_even(number):
    if number % 2 == 0:
        return True

    return False


result = filter(check_even, list(map(int, input().split(" "))))
print(list(result))
