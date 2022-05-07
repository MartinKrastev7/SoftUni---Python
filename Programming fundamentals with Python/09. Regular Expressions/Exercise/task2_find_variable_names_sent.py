import re

pattern = r"\b_[A-Za-z0-9]+\b"
text = input()

result = re.findall(pattern, text)
#x = [x.replace("_", "") for x in result]
word_list = []

for word in result:
    word_list.append(word[1:])

print(",".join(word_list))
#(?<=\b_)([a-zA-Z0-9]+)\b"