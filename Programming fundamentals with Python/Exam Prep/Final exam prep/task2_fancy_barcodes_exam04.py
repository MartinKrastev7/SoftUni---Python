import re

count_barcodes = int(input())


for i in range(count_barcodes):
    strings = input()

    pattern = r"\@\#+([A-Z][A-Za-z\d]{4,}[A-Z])\@\#+"
    #pattern = r'\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+'
    result = re.findall(pattern, strings)

    if result:
        strings = "".join(result)
        product_group = "".join([x for x in strings if x.isdigit()])
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

