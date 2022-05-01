def sum_of_numbers(num):

    even_sum = 0
    odd_sum = 0

    for i in str(num):
        current_digit = int(i)
        if current_digit % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
   # return


n = int(input())

sum_of_numbers(n)

#vtoro reshenie
def odd_even_sum(nums):
    odd_sum = 0
    even_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Odd sum: {odd_sum}, Even sum: {even_sum}")

numbers = map(int, list(input()))
odd_even_sum(numbers)