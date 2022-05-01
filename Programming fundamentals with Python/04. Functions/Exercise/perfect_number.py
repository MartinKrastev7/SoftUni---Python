def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return


n = int(input())
perfect_number(n)
