target_symbols = ["-", ",", ".", "!", "?"]

with open('./text.txt', 'r') as file:
    # idx = 0
    #  for line in file:
    #     if idx % 2 == 0:
    #        print(line.strip())
    #   idx += 1
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for symbol in target_symbols:
                result = result.replace(symbol, "@")
            print(result)