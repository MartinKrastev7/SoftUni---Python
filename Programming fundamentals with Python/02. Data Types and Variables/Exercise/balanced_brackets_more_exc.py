number_lines = int(input())
is_open = False
is_balanced = True


for i in range(1, number_lines + 1):
    symbols = input()

    if symbols == "(":
        if not is_open:
            is_open = True
        else:
            is_balanced = False

    if symbols == ")":
        if is_open:
            is_open = False
        else:
            is_balanced = False

if is_balanced and not is_open:
    print("BALANCED")
else:
    print("UNBALANCED")