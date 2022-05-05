strings = input().split(" ")
result = ""

for word in strings:
    length = len(word)
    result += word * length

print(result)

#vtori nachin
words = input().split(" ")
output = ""

for word in words:
    output += word * len(word)

print(output)