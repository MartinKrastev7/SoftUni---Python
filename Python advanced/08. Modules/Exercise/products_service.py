from json import loads
from auth_service import get_current_user


def get_all_products():
    with open('./products.txt','r') as products_file:
        result = []
        for line in products_file:
            product = loads(line.strip())
            result.append(product)
        return result


def buy_product(product_id):
    user = get_current_user()