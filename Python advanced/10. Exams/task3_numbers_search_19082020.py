def numbers_searching(*args):
    numbers = list(sorted(args))
    min_number = numbers[0]
    max_number = numbers[-1]
    duplicates = set()
    missing_num = None

    for i in numbers:
        if numbers.count(i) >= 2:
            duplicates.add(i)

    for num in range(min_number, max_number + 1):
        if num not in numbers:
            missing_num = num

    return [missing_num, list(sorted(duplicates))]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))