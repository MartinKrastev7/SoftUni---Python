def loading_bar(n):
    ready = ("%"*int(n/10))
    remain = ("."*int(10-n/10))
    loading_bar = ready+remain
    return loading_bar


n = int(input())
if n == 100:
    print(f'100% Complete!\n[{loading_bar(n)}]')
else:
    print(f'{n}% [{loading_bar(n)}]\nStill loading...')

#vtoro reshenie
def loading_bar(num):

    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percent = (num//10)*'%'
        dots = (10 -(num // 10)) * '.'
        print(f"{num}% [{percent}{dots}]")
        print("Still loading...")


num = int(input())
loading_bar(num)