number_list = input().split(", ")
number_forward = ""
number_backward = ""
for number in number_list:
    number_forward = number
    number_backward = number[::-1]
    if number_forward == number_backward:
        print("True")
    else:
        print("False")

# s lambda
#number_list = input().split(", ")
#resultArr = list(map(lambda x: 'True' if (x == x[::-1]) else 'False', number_list))
#print("\n".join(resultArr))

#treto reshenie
def palindrome_func(nums):
    for num in nums:
        if num == num[::- 1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome_func(numbers)