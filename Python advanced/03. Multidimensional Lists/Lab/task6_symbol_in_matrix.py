n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

is_found = False

for row_index in range(n):
    if is_found:
        break
    for column_index in range(n):
        if matrix[row_index][column_index] == symbol:
            is_found = True
            print(f"({row_index}, {column_index})")
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")

#vtori nachin
def find_symbol(matrix, symbol):
    for row_index in range(n):
        for column_index in range(n):
            if matrix[row_index][column_index] == symbol:
                return row_index, column_index


n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)

if result:
    row_index, column_index = result
    print(f"({row_index}, {column_index})")
else:
    print(f"{symbol} does not occur in the matrix")