my_list =[int(num) for num in input().split(" ")]
count_to_remove = int(input())

my_list.sort(reverse=True)

for num in range(count_to_remove):
    my_list.pop()

result = ", ".join(map(str, my_list))
print(result)

# vtori nachin
a = input()
number = int(input())
ll = [int(i) for i in a.split(' ')]

for _ in range(number):
    x = min(ll)
    ll.remove(x)

result = ', '.join(map(str, ll))
print(result)

#treti nachin
nums = input().split(" ")
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(", ".join(nums))
