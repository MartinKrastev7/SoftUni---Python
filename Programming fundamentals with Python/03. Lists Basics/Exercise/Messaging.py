numbers = input().split(" ")
strings = input()
final_mess = ""

for i in range(len(numbers)):
    digits_sum = 0
    for j in str(numbers[i]):
        digits_sum += int(j)

    numbers[i] = digits_sum

new_coded_mess = strings

for k in numbers:
    if k > len(new_coded_mess):
        k = k % len(new_coded_mess)
    final_mess += new_coded_mess[k]

    new_coded_mess = new_coded_mess[0:k] + new_coded_mess[k+1:]

print(final_mess)

