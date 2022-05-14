import re

text = input()
digits_pattern = r"[0-9]"
result_digits = re.findall(digits_pattern, text)
int_digit = [int(x) for x in result_digits]
#cool_threshold = math.prod(int_digit) ili po dolniq nachin
cool_threshold = 1
for i in int_digit:
    cool_threshold *= i 


pattern = r"(\*\*|\:\:)([A-Z][a-z]{2,})\1"
result = re.finditer(pattern, text)
cool_emojis = []
all_emojis = []

for match in result:
    all_emojis.append(match.group())
    suming = 0
    for i in match.group(2):
        suming += int(ord(i))
    if suming > cool_threshold:
        cool_emojis.append(match.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)