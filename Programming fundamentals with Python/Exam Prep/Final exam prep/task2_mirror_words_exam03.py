import re

text_string = input()
pattern = r"\@([A-Za-z]{3,})\@{2}([A-Za-z]{3,})\@|" \
          r"\#([A-Za-z]{3,})\#{2}([A-Za-z]{3,})\#"

result = re.findall(pattern, text_string)
word_list = []

for item in result:
    current_item = [el for el in item if el != ""]
    word_list.append(current_item)

if len(word_list) > 0:
    print(f"{len(word_list)} word pairs found!")
else:
    print("No word pairs found!")

palindromes = []
for word in word_list:
    first_word = word[0]
    second_word = word[1]
    reversed_second = "".join(reversed(second_word))
    if first_word == reversed_second:
        palindromes.append(first_word + " <=> " + second_word)

if len(palindromes) > 0:
    print("The mirror words are:")
    print(", ".join([str(x) for x in palindromes]))

else:
    print("No mirror words!")
