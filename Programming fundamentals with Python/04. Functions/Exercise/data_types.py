def data_types(type, num):
    if type == "int":
        print(f"{int(num) * 2}")
    elif type == "real":
        print(f"{(float(num) * 1.5):.2f}")
    elif type == "string":
        print(f"${num}$")


first = input()
second = input()
data_types(first, second)
