char1 = ord(input())
char2 = ord(input())
strings = input()
strings_ascii = []
sum_total = 0

for i in strings:
    strings_ascii.append(ord(i))

for k in strings_ascii:
    if int(char1) < int(k) and int(char2) > int(k):
        sum_total += int(k)

print(sum_total)

