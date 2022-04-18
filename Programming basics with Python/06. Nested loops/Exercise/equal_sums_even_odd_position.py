first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(current_number_as_string, end = " ")

######### vtori nachin
first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    current_number_as_string = str(number)
    odd_sum = 0
    even_sum = 0
    for index in range(len(current_number_as_string)):
        current_digit = int(current_number_as_string[index])
        if index % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit
    if odd_sum == even_sum:
        print(number, end=" ")