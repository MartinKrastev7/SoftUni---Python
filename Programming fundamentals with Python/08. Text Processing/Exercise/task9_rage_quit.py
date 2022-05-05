#text = input().upper()
#med = ''
#final = ''
#i = 0

#while i < len(text):
 #   if text[i].isdigit():
 #       if i < len(text) - 1:
 #           if text[i + 1].isdigit():
 #               final += (med * int(str(text[i]) + str(text[i + 1])))
 #               i += 1
  #          else:
 #               final += (med * int(text[i]))
#        else:
 #           final += (med * int(text[i]))
 #       med = ''
#    else:
 #       med += text[i]
 #   i += 1

#symbols = len(set(final))
#print(f"Unique symbols used: {symbols}\n{final}")

#vtori nachin
#data = input()
#symbol = ""
#string = ""
#number = ""
#unique_symbols = ""
#output = ""

#for i in range(len(data)):
#    if not data[i].isnumeric():
#        symbol = data[i].upper()
#        string += symbol
#        if symbol not in unique_symbols:
#            unique_symbols += symbol
 #   else:
 #       if i != len(data) - 1:                 # лекарство срещу index out of range
#            if data[i + 1].isnumeric():        # проверката за двуцифрени числа
 #               number += data[i]
 #               number += data[i + 1]
  #          else:
 #               number += data[i]
 #       else:
 #           number += data[i]
 #       string *= int(number)
 #       output += string
 #       string = ""
 #       number = ""


#print(f"Unique symbols used: {len(unique_symbols)}")
#print(output)

#treti nachin regex
import re

input_string = input().upper()

splitted_input = re.split(r"(\d+)", input_string)
result_list = []

for i in range(0, len(splitted_input) - 1, 2):
    string_to_repeat = splitted_input[i]
    repeat_times = int(splitted_input[i + 1])
    result_list.append(string_to_repeat * repeat_times)

result_to_print = ''.join(result_list)
unique_characters = len(set(result_to_print))

print(f"Unique symbols used: {unique_characters}")
print(result_to_print)