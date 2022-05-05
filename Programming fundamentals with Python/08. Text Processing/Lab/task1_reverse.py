text = input()

while text != "end":
    text_reversed = ""

    for i in reversed(text):
        text_reversed += i

    print(f"{text} = {text_reversed}")

    text = input()


#vtori nachin
text = input()

while text != "end":
    for char in reversed(text):
        print(char, end="")

    text = input()

#ili
while text != "end":
    rev = reversed(text)
    reversed_text = "".join(rev)
    print(f"{text} = {reversed_text}")
    text = input()