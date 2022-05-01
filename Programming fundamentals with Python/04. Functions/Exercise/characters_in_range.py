def char_to_num(a, b):
    num1 = ord(a)
    num2 = ord(b)
    new_list = []
    for i in range(num1 + 1, num2):
        new_item = chr(i)
        new_list.append(new_item)

    return " ".join(new_list)

char_1 = input()
char_2 = input()

print(char_to_num(char_1, char_2))

#vtoro reshenie
def char_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()
char_in_range(char1, char2)