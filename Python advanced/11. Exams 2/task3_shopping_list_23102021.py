def shopping_list(n, **kwargs):
    basket = 0
    bought = []
    if n >= 100:
        for key, value in kwargs.items():
            product = key
            price = value[0]
            quantity = value[1]
            total = price * quantity
            if basket == 5:
                break
            if total <= n:
                basket += 1
                n -= total
                bought.append(f"You bought {product} for {total:.02f} leva.")
        return '\n'.join(bought)
    else:
        return f"You do not have enough budget."


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


