def find_the_smallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < b and c < a:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(find_the_smallest(num1, num2, num3))

# vtori nachin
def find_the_smallest(a, b ,c):
    print(min(a, b, c))
