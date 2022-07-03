def stock_availability(*args):
    inventory_list = args[0]
    command = args[1]

    if command == "delivery":
        items = list(args[2:])
        inventory_list.extend(items)
    elif command == "sell":
        if len(args) > 2:
            third_param = list(args[2:])
            if str(third_param[0]).isdigit():
                number = int(args[2])
                inventory_list = inventory_list[number:]
            elif str(third_param[0].isalpha()):
                if len(third_param) == 1:
                    if third_param[0] in inventory_list:
                        inventory_list = [el for el in inventory_list if el != third_param[0]]
                elif len(third_param) > 1:
                    for el in third_param:
                        if el in inventory_list:
                            inventory_list = [par for par in inventory_list if par != el]

        else:
            inventory_list = inventory_list[1:]

    return inventory_list


print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
