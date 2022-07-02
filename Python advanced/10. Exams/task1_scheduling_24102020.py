jobs = [int(x) for x in input().split(", ")]
idx_of_job = int(input())
tasks = []

for i in range(len(jobs)):
    tasks.append([jobs[i], i])

cycles = 0
for i in sorted(tasks):
    cycles += i[0]
    if idx_of_job == i[1]:
        break

print(cycles)