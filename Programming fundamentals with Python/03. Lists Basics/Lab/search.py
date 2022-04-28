number_lines = int(input())
word = input()
words_first = []
words_second = []

for i in range(1, number_lines + 1):
    some_strings = input()
    words_first.append(some_strings)

    if word in some_strings:
        words_second.append(some_strings)

print(words_first)
print(words_second)

#vtori nachin s premahvane na elementi i bez vtori list:
#for i in range(len(word_first) -1, -1, -1):
# element = word_first[i]
#if word not in element:
#word_first.remove(element)