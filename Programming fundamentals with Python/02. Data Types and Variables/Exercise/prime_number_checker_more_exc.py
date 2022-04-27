num = int(input())

is_not_prime = False

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_not_prime = True
            break

if is_not_prime:
    print("False")
else:
    print("True")