print(sum([int(x) for x in open('./numbers.txt','r')]))

#vtori nachin po burzo i po malko pamet po optimalno
file = open('./numbers.txt','r')
the_sum = 0

for line in file:
    the_sum += int(line)

print(the_sum)