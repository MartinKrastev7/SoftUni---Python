words = input().split(" ")
searched_palindrome = input()
palindromes = []

for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

#vtori nachin
words = input().split(" ")
palindrome = input()
palindrome_words = []

for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindrome_words.append(rev_word)



print(f"{palindrome_words}")
print(f"Found palindrome {words.count(palindrome)} times")
