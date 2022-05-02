text = input().split()


def swap(c, i, j):
    c = list(c)
    x=c[i]
    c[i], c[j] = c[j], x
    return "".join(c)

res=[]

for key in text:
    list_zero = []
    list_element = []
    [list_zero.append(i) for i in key if i.isdigit()]
    num = int("".join(list_zero))
    num = chr(num)
    list_element.insert(0,num)
    [list_element.append(j) for j in key if not j.isdigit()]

    res.append(swap(list_element, 1, - 1))
    res.append(" ")
    list_zero.clear()
    list_element.clear()

res="".join(res)

print(res)

#vtoro reshenie
def int_to_chr(word):
    string = list(word)
    num_as_str = list()

    while string[0].isdigit():
        num_as_str.append(string[0])
        string.pop(0)

    num = int(''.join(num_as_str))
    string.insert(0, chr(num))
    return ''.join(string)


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


print(' '.join([switch_letters(int_to_chr(word)) for word in input().split()]))