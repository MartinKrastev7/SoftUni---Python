import math


def factorial_division(first_num, second_num):
    return math.factorial(first_num) / math.factorial(second_num)


#def factorial(num):
 #   factorial_n = 1
 # if num >=1:
  #  for i in range(1, num + 1):
   #     factorial_n *= i

   # return factorial


number_1 = int(input())
number_2 = int(input())
print(f"{factorial_division(number_1, number_2):.2f}")

#vtoro reshenie
def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)



number = int(input())
number2 = int(input())
result = factorial(number) / factorial(number2)
print(f"{result:.2f}")