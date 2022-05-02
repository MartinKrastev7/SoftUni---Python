text = input()
list_text = list(text)
symbols = ['a', 'o', 'u', 'e', 'i']

new_list = [x for x in list_text if x not in symbols]
print("".join(new_list))

