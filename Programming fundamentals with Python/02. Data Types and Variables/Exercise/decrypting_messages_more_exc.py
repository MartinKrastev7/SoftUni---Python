key = int(input())
number_lines = int(input())
new_word = ""
for i in range(1, number_lines + 1):
    letter = input()
    sum_them = key + ord(letter)
    sum_str = chr(sum_them)
    new_word += sum_str

print(new_word)