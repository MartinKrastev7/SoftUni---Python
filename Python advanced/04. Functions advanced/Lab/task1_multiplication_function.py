def multiply(*args):
    result = 1
    for el in args:
        result *= el
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))

#vtori nachin
def multiply(*args):
    product = 1
    for v in args:
        product *= v
    return product