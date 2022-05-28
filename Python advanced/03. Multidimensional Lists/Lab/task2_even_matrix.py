n = int(input())

result = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    result.append(
        [x for x in row if x % 2 == 0]
    )

print(result)

#vtori nachin
n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
print([[x for x in row if x % 2 == 0] for row in matrix])


#ili
def is_even(number):
    return number % 2 == 0


def remove_odd(ll):
    return [x for x in ll if is_even(x)]


print(
    [remove_odd(row) for row in matrix]
)