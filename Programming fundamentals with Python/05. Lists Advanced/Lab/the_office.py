employees = input().split(" ")
happy_factor = int(input())
employees = list(map(lambda x: int(x) * happy_factor, employees ))

filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")


#vtoro reshenie
employees = input().split(" ")
employees = list(map(int, employees))
factor = int(input())

happy_employees = list(filter(lambda employee: employee >= sum(employees) / len(employees), employees))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
