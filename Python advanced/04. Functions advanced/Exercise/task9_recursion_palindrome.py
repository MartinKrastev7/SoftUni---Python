def palindrome(word, idx):
    if idx >= len(word) // 2: # tova e dunoto base case, indexa stiga sredata na dumata i ako poluchi false prekratqva ako produlji e True i dumata e palindrome
        return f"{word} is a palindrome"
    left = word[idx]
    right = word[-1 - idx]
    if left != right:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)  #izvikvane na rekursiqta


print(palindrome("abcba", 0))