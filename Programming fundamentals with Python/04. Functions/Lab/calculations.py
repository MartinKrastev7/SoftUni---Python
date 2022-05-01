operatos = input()
a = int(input())
b = int(input())

def calculates(operato, first, second):
    if operato == "multiply":
        return first * second
    elif operato == "divide":
        return int(first / second)
    elif operato == "add":
        return first + second
    elif operato == "subtract":
        return first - second

print(calculates(operatos,a,b))
print(calculates(operato=input(),first=int(input()), second = int(input())))

#vtoro
result = None
if operato == "multiply":
    result = first * second
return result