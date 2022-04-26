number = input()
n = str(number)
m = sorted(n, reverse=True)

for d, digit in enumerate(m):
    print(digit, end="")

# vtoro reshenie s list

number = list(input())
number.sort(reverse=True)
print(''.join(number))
#На първия ред преобразуваме стринга, който сме получили, в лист от отделните му символи. Например при вход '1234' ще получим ['1', '2', '3', '4'].

#После сортираме листа в обърнат ред, т.е. ще получим ['4', '3', '2', '1']

#Накрая сливаме листа в стринг, който отпечатваме: '4321'