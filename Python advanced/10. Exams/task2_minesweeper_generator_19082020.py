size = int(input())
number_bombs = int(input())
matrix = [[0 for el in range(size)] for _ in range(size)]
mines = [input().strip("()") for _ in range(number_bombs)]

for mine in mines:
    num1, num2 = [int(x) for x in mine.split(", ")]
    matrix[num1][num2] = "*"

for row in range(size):
    for col in range(size):
        position = matrix[row][col]

        if position == "*":
            continue

        #right
        if col + 1 < size and matrix[row][col + 1] == "*":
            position += 1
        #left
        if col - 1 >= 0 and matrix[row][col - 1] == "*":
            position += 1
        #down
        if row + 1 < size and matrix[row + 1][col] == "*":
            position += 1
        #up
        if row - 1 >= 0 and matrix[row - 1][col] == "*":
            position += 1
        #right - up diagonal
        if row - 1 >= 0 and col + 1 < size and matrix[row - 1][col + 1] == "*":
            position += 1
        #right down diagonal
        if row + 1 < size and col + 1 < size and matrix[row + 1][col + 1] == "*":
            position += 1
        #left up diagonal
        if row - 1 >= 0 and col - 1 >= 0 and matrix[row - 1][col - 1] == "*":
            position += 1
        # left down diagonal
        if row + 1 < size and col - 1 >= 0 and matrix[row + 1][col - 1] == "*":
            position += 1

        matrix[row][col] = position

for row in matrix:
    print(" ".join([str(x) for x in row]))