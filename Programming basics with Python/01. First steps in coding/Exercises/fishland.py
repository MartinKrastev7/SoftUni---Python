mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
shell_kg = int(input())

shell_price = 7.50 * shell_kg
price_bonito = (mackerel_price + mackerel_price * 0.60) * bonito_kg
price_scad = (sprat_price + sprat_price * 0.8) * scad_kg
total_amount = shell_price + price_scad + price_bonito
print(f"{total_amount:.2f}")
