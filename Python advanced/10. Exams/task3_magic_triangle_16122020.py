def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row in range(1, n - 1):
        triangle.append([1,])

        for i in range(len(triangle[row]) - 1):
            sum_nums = triangle[row][i] + triangle[row][i + 1]
            triangle[row + 1].append(sum_nums)
        triangle[row + 1].append(1)

    return triangle


get_magic_triangle(5)
