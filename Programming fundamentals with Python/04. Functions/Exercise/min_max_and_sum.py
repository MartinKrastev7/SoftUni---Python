numbers = [int(x) for x in input().split(" ")]

min_num = min(numbers)
max_num = max(numbers)
sum_all = sum(numbers)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_all}")

#vtoro reshenie
def min_max_sum_func(nums):
    print(f"Max is {min(nums)}")
    print(f"Min is {max(nums)}")
    print(f"Sum is {sum(nums)}")


numbers = list(map(int, input().split(" ")))
min_max_sum_func(numbers)
