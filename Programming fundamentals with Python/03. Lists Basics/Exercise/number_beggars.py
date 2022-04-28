coins = [int(num) for num in input().split(", ")]
beggars = int(input())
count = 0
beggars_list = [0] * beggars
for coin in coins:
    beggars_list[count] += coin
    count += 1
    if count >= beggars:
        count = 0
print(beggars_list)

############################
numbers_list = [int(x) for x in input().split(", ")] # Правиш лист за първия input и ги разделяш с ',' (чрез comprehension)
number_of_beggars = int(input())

beggars_list = [0] * number_of_beggars # Тази част прави в този случей един лист с толкова нули колкото са просяците, за да може сле това в loop-a да се пълнят в зависимост кой е под ред:

# След това първия for цикъл прави така че да вземе всеки един от всички просяци, и current_beggar е равен на текущия просяк.:
for num in range(len(beggars_list)):
    current_beggar = num

    for n in range(len(numbers_list)):
        current_num = n % number_of_beggars
        if current_num == current_beggar:
            if beggars_list[num] == 0:
                if numbers_list[n] == 0:
                    beggars_list[current_num] = 0
                    break
                beggars_list[current_num] = numbers_list[n]
            else:
                 beggars_list[current_num] += numbers_list[n]

print(beggars_list)

