number_bitcoin = int(input())
chinese_ioan_number = float(input())
commission = float(input())

one_bitcoin_price_lv = 1168 * number_bitcoin
one_chinese_ioan_price_lv = (0.15 * 1.76) * chinese_ioan_number
one_dollar_bg = 1.76
one_euro_bg = 1.95

total_eur = (one_bitcoin_price_lv + one_chinese_ioan_price_lv) / 1.95
commission = total_eur * commission / 100
result = total_eur - commission
print(f"{result:.2f}")


