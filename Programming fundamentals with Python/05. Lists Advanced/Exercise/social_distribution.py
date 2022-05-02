population = [int(x) for x in input().split(", ")]
min_limit = int(input())
for i in range(len(population)):
    wealthiest = max(population)
    if wealthiest <= min_limit:
        break
    poorest = min(population)
    take_inx_rich = population.index(wealthiest)
    take_inx_poor = population.index(poorest)
    difer = min_limit - poorest
    if difer == 0:
        continue
    population[take_inx_poor] += difer  # Suma la diferencia al index mas pobre

    population[take_inx_rich] -= difer  # Resta la diferencia al index mas rico

if not min(population) >= min_limit:  # Si actual pobreza es mayor o igual al min limit entra
    print("No equal distribution possible")
else :
    print(population)