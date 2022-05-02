numbers = [int(x) for x in input().split(", ")]
even_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

#vtori nachin
number_list = list(map(int, input().split(", ")))
found_indexes_or_no = map(lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))

even_indexes = list(filter(lambda a: a != "no", found_indexes_or_no))
print(even_indexes)

#treti nachin
numbers = input().split(", ")
numbers = list(map(int, numbers))
even_index = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index.append(i)

#chetvurti nachin
nums = [int(el) for el in input().split(", ")]
print([index for index in range(len(nums)) if nums[index] % 2 == 0])
