test_str = input()
all_freq = {}
#number_letters = len(test_str) - test_str.count(" ")

for i in test_str:
    if i != " ":
        if i not in all_freq:
            all_freq[i] = 0
            # Add or increment the value in the dictionary
        all_freq[i] += 1

for key, value in all_freq.items():
    print(f"{key} -> {value}")

#vtori nachin
word = input()
my_dict = {}

for ch in word:
    if ch not in my_dict and ch != " ":
        my_dict[ch] = 1
    else:
        my_dict[ch] += 1

print(my_dict)

#treti nachin
from collections import Counter

word = input()
result = Counter(word)
for key,value in result.items():
    if key != " ":
        print(f"{key} -> {value}")
