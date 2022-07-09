def shopping_cart(*args):
    dishes = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []

    }
    result = ""

    for i in range(len(args)):
        if args[i] == "Stop":
            break
        type_of_meal = args[i][0]
        products = args[i][1]

        if type_of_meal == "Soup":
            if len(dishes[type_of_meal]) < 3:
                if products not in dishes[type_of_meal]:
                    dishes[type_of_meal].append(products)
        elif type_of_meal == "Pizza":
            if len(dishes[type_of_meal]) < 4:
                if products not in dishes[type_of_meal]:
                    dishes[type_of_meal].append(products)
        elif type_of_meal == "Dessert":
            if len(dishes[type_of_meal]) < 2:
                if products not in dishes[type_of_meal]:
                    dishes[type_of_meal].append(products)

    if len(dishes["Soup"]) > 0 or len(dishes["Pizza"]) > 0 or len(dishes["Dessert"]) > 0:
        sorted_elements = sorted(dishes.items(), key=lambda x: (-len(x[1]), x[0]))
        for element in sorted_elements:
            meal = element[0]
            product = element[1]
            sorted_products = sorted(product)
            result += f'{meal}:\n'
            for item in sorted_products:
                result += f' - {item}\n'
    else:
        result = f"No products in the cart!"

    return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


