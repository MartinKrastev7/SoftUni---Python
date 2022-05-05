MORSE_CODE_DICT = {
                    'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..'}

code_reversed = {value: key for key, value in MORSE_CODE_DICT.items()}
text = input().split(" | ")
decipher = ""

for i in text:
    words = i.split(" ")
    for word in words:
        if word in code_reversed.keys():
            decipher += code_reversed[word]
    decipher += " "

print(decipher)
