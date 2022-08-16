def reverse_text(text):
    index = len(text) - 1
    while index > -1:
        yield text[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')

#vtori nachin
def reverse_text(text):
    index = 0
    n = len(text)
    while index < n:
        yield text[n - index - 1]
        index += 1

