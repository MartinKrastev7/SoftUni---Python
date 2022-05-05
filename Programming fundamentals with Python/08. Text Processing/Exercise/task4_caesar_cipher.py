text = input()
new_crypt = []

for word in text:
    for ch in word:
        char = ord(ch) + 3
        new_char = chr(char)
        new_crypt.append(new_char)

print("".join(new_crypt))

#vtori nachin
def caesar_cipher(text):
    result = [chr(ord(ch)+3) for ch in text]
    print("".join(result))


text = input()
caesar_cipher(text)