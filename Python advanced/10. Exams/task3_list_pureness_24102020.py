from collections import deque


def best_list_pureness(*args):
    list_numbers = list(args[0])
    number = args[1]
    count_rotation = 0
    best_pureness = 0
    best_rotation = 0
    for el in range(len(list_numbers)):
        best_pureness += list_numbers[el] * el

    while not number == 0:
        sum_el = 0
        count_rotation += 1
        new_first = list_numbers[-1]
        list_numbers.pop()
        list_numbers.insert(0, new_first)

        for el in range(len(list_numbers)):
            sum_el += list_numbers[el] * el
        if sum_el > best_pureness:
            best_pureness = sum_el
            best_rotation = count_rotation
        number -= 1

    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

#vtori nachin
def best_list_pureness(*args):
    numbers, k = args
    numbers = deque(numbers)
    best_rotation = 0
    best_pureness = 0
    for rotation in range(k + 1):
        pureness = sum([n * i for i, n in enumerate(numbers)])
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        num = numbers.pop()
        numbers.appendleft(num)
    return f'Best pureness {best_pureness} after {best_rotation} rotations'