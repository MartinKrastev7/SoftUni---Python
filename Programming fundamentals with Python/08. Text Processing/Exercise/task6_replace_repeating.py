text = input()
new_word = []

for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        new_word.append(text[i])

new_word.append(text[len(text) - 1])

print("".join(new_word))

#Минавам през всички символи с for цикъл  от 0 до text.Length-1 и ако символите са еднакви програмата продължава, но ако са различни запазвам  само предходния символ. Накрая винаги си запазвам последния символ от текста.