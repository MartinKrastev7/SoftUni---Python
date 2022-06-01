from functools import reduce


def operate(oper, *args):
    if oper == "+":
        return reduce(lambda a, b: a + b, args)
    elif oper == "-":
        return reduce(lambda a, b: a - b, args)
    elif oper == "*":
        return reduce(lambda a, b: a * b, args)
    elif oper == "/":
        return reduce(lambda a, b: a / b, args)


print(operate("*", 3, 4))

#vtori nachin
def operate(sign, *args):
    if sign in ("+","-"):
        result = 0
    else:
        result = 1

    if sign == "+":
        for el in args:
            result += el


    return result

#treti nachin
def operate(operation, *args):
    def add(*args):

