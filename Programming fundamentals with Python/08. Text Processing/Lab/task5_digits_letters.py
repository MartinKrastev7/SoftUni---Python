text = input()
digits = ""
letters = ""
others = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        others += ch

print(digits)
print(letters)
print(others)

#vtori nachin
text = input()
digits = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isupper() and ch.islower():
        letters += ch
    else:
        symbols += ch

#treti nachin
for ch in text:
    if ch.isalnum():
        if ch.isdigit():
            digits += ch
        else:
            letters += ch
    else:
        symbols += ch