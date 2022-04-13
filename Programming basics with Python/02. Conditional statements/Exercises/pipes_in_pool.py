v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_filled = p1 * h
p2_filled = p2 * h
total_filled = p1_filled + p2_filled

if v >= total_filled:
    filled_percent = (total_filled / v) * 100
    p1_percent = (p1_filled / total_filled) * 100
    p2_percent = (p2_filled / total_filled) * 100
    print(f"The pool is {filled_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
else:
    litres_more = total_filled - v
    print(f"For {h:.2f} hours the pool overflows with {litres_more:.2f} liters.")
