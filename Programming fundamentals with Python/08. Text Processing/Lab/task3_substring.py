first = input()
second = input()

while first in second:
    second = second.replace(first, "")

print(second)

#vtori nachin
search = input()
text = input()

while search in text:
    text = text.replace(search, "")
