first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    command_params = line_args[1]

    if command == "Add":
        if command_params == "First":
            [first.add(int(x)) for x in line_args[2:]]

        elif command_params == "Second":
            [second.add(int(x)) for x in line_args[2:]]

    elif command == "Remove":
        if command_params == "First":
            first = first.difference([int(x) for x in line_args[2:]])
        elif command_params == "Second":
            second = second.difference([int(x) for x in line_args[2:]])

    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")

