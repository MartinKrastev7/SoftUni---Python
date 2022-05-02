substrings = input().split(", ")
strings = input().split(", ")

result = [x for x in substrings if [y for y in strings if x in y]]

print(result)

#vtori nachin
substrings = input().split(", ")
sentance = input()
result = [el for el in substrings if el in sentance]
print(result)