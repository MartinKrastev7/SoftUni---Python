n = int(input())
names_set = set()

for _ in range(n):
    names_set.add(input())

[print(name) for name in names_set]
#for name in names_set:
 #   print(name) za gornoto pulno

#vtoro reshenie
n = int(input())
names_set = {input() for _ in range(n)}
