rows_count, columns_count = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows_count):
    matrix.append(
        [int(x) for x in input().split(" ")]
    )

column_sums = [0] * columns_count

for row_index in range(rows_count):
    for column_index in range(columns_count):
        column_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sums]

#vtori nachin
def get_column_sum(matrix):
    column_sums = [0] * columns_count

    for row_index in range(rows_count):
        for column_index in range(columns_count):
            column_sums[column_index] += matrix[row_index][column_index]

    return column_sums

#treti nachin
column_sums = []
for column_index in range(columns_count):
    column_sums.append(0)
    for row_index in range(rows_count):
        column_sums[-1] += matrix[row_index][column_index]