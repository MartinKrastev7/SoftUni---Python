single_string = input()
my_list = []
my_list.append(single_string)
my_list = single_string.split()

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])*-1

print(my_list)

#vtoro reshenie
numbers = input().split()
list = []
for number in numbers:
    current_number = int(number)
    list.append(-current_number)
print(list)

#treto reshenie
nums = input().split(" ")
new_list =[]

for num in nums:
    if int(num) > 0:
        new_list.append(-int(num))
    else:
        new_list.append(abs(int(num)))
print(new_list)

#chetv reshenie
nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
print(nums)