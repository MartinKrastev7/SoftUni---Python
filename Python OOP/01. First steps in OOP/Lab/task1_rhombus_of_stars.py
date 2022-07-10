def print_rhombus(n):
    for i in range(n):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(" " * spaces_count + "* " * stars_count)
    for i in range(n -2, -1, -1):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(" " * spaces_count + "* " * stars_count)


n = int(input())
print_rhombus(n)

#vtori nachin
def get_line(i, n):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return f" " * spaces_count + "* " * stars_count

def print_line(n):
    print(get_line(n-1, n-1))

def print_rhombus(n):
    for i in range(0, n, 1):
        print(get_line(i, n))
    for i in range(n -2, -1, -1):
        print(get_line(i, n))