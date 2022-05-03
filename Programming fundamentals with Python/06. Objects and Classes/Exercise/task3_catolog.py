class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        given_letter = []
        for i in self.products:
            if first_letter in i[0]:
                given_letter.append(i)
        return given_letter

    def __repr__(self):
        self.products.sort()
        output = f"Items in the {self.name} catalogue:\n"
        output += '\n'.join(sorted(self.products))
        return output



      #  return f"Items in the {self.name} catalogue: \n {' '.join(self.products)}"



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

#vtori nachin


