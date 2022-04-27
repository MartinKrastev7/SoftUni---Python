year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    str_year = str(year)
    set_year = set()

    for i in range(len(str_year)):
        set_year.add(str_year[i])

    if len(str_year) == len(set_year):
        is_happy_year = True
    # ili is_happy_year = len(str_year) == len(set_year)
print(year)

#vtoro reshenie
while not is_happy_year:
    year += 1
    str_year = str(year)
    set_year = set(str_year) # bez nujda ot for; proverqva za unikalni cifri (nepovtarqshti se )

# treto reshenie
while len(set(str(year))) != len(str(year)):
year += 1 # i posle samo if
