tabs_open = int(input())
salary = int(input())

for text in range(tabs_open):
    site_name = input()
    if site_name == "Facebook":
        salary = salary - 150
    elif site_name == "Instagram":
        salary = salary - 100
    elif site_name == "Reddit":
        salary = salary - 50
    else:
        salary = salary
    if salary <= 0:
         break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)