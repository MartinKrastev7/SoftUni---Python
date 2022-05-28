def get_primary_diagonal_sum(matrix):
    the_sum = 0
    n = len(matrix)
   # for row in range(n):
    #    for column in range(n):
     #       if row == column:
      #          the_sum += matrix[row][column] ako ne znaem che sa ravni ne se polzva chesto
    for i in range(n):
        the_sum += matrix[i][i]
    return the_sum
#   return sum(matrix[i][i] for i in range(n)) - na edin red gornoto

def get_secondary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][n - i - 1] for i in range(n))

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split(" ")]
    )

print(get_primary_diagonal_sum(matrix))