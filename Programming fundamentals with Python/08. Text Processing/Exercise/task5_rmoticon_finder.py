text = input()


for i in range(len(text)):
    if text[i] == ":":
        print(f":{text[i + 1]}")

#ili samo s tova
[print(f":{text[i + 1]}") for i in range(len(text) - 1) if text[i] == ':']

#treti nachiin
def emoticon_finder(text):
    result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":" and text[i + 1] != " "]
    print("\n".join(result))


text = input()
emoticon_finder(text)