elements = input().split(" ")
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

searched_products = input().split(" ")

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

#vtori nachin
data = input().split(" ")
bakery = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i + 1]
    bakery[food] = quantity
search_data = input().split(" ")

for search_term in search_data:
    if search_term in bakery.keys():
        print(f"we have {bakery[search_term]} of {search_term} left")


