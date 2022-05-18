expression = input()
opening_brackets = []
pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}
#predefinira kakva da e otvarqshtata i zatvarqshtata skoba
balanced = True
for ch in expression:
    if ch in "([{":
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False

    if not balanced:
        break

if not balanced or opening_brackets:
    print("NO")
else:
    print("YES")

#vtori nachin
parentheses = input()
BALANCED_PAIRS = ["{}", "[]", "()"]
open_brackets = []
is_valid = True

for char in parentheses:
    if char in "([{":
        open_brackets.append(char)
    else:
        if not open_brackets:
            is_valid = False
            break
        else:
            pair = open_brackets.pop() + char
            if pair in BALANCED_PAIRS:
                continue
            else:
                is_valid = False
                break

if is_valid and not open_brackets:
    print("YES")
else:
    print("NO")