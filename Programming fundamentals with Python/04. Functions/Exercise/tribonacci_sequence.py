def tribonacci(num):
   first = 1
   second = 1
   third = 2
   print(first, end=" ")
   print(second, end=" ")
   print(third, end=" ")

   for i in range(3, num):
       current = first + second + third
       first = second
       second = third
       third = current

       print(current, end=" ")


number = int(input())
if number < 3:
    for i in range(-1, number-1):
        print(1, end=" ")
    print()
else:
    tribonacci(number)

