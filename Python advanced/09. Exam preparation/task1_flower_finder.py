from collections import deque

def mark_words_letter(vowel, consonant,word_dict):
    result = False
    if vowel in word_dict:
        word_dict[vowel] = True
        result = True
    if consonant in word_dict:
        word_dict[consonant] = True
        result = True

vowels = deque(input().split())
consonants = input().split()

rose = {letter: False for letter in "rose"}
tulip = {letter: False for letter in "tulip"}
lotus = {letter: False for letter in "lotus"}
daffodil = {letter: False for letter in "daffodil"}

found_flower = None

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    if mark_words_letter(vowel, consonant, rose):
        if all(rose.values()):
            found_flower = "rose"
            break

    if mark_words_letter(vowel, consonant, tulip):
        if all(tulip.values()):
            found_flower = "tulip"
            break

    if mark_words_letter(vowel, consonant, lotus):
        if all(lotus.values()):
            found_flower = "lotus"
            break

    if mark_words_letter(vowel, consonant, daffodil):
        if all(daffodil.values()):
            found_flower = "daffodil"
            break


if found_flower:
    print(f"Word found: {found_flower}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

#vtori nachin
def mark_words_letters(vowel, consonant, word_set):
    if vowel in word_set:
        word_set.remove(vowel)
    if consonant in word_set:
        word_set.remove(consonant)


rose = set("rose")
tulip = set("tulip")
lotus = set("lotus")
daffodil = set("daffodil")

vowels = deque(input().split())
consonants = input().split()

found_flower = None
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    mark_words_letters(vowel, consonant, rose)
    if len(rose) == 0:
        found_flower = 'rose'
        break

    mark_words_letters(vowel, consonant, tulip)
    if len(tulip) == 0:
        found_flower = 'tulip'
        break

    mark_words_letters(vowel, consonant, lotus)
    if len(lotus) == 0:
        found_flower = 'lotus'
        break

    mark_words_letters(vowel, consonant, daffodil)
    if len(daffodil) == 0:
        found_flower = 'daffodil'
        break