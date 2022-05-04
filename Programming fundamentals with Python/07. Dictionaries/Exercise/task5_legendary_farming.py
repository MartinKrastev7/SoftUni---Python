def print_func(legendary_items_dict, junk_items, special_item):
    print(f"{special_item} obtained!")
    print(f"shards: {legendary_items_dict['shards']}")
    print(f"fragments: {legendary_items_dict['fragments']}")
    print(f"motes: {legendary_items_dict['motes']}")

    for key,value  in junk_items.items():
        print(f"{key}: {value}")
def legendary_farming():
    legendary_items_dict = {"shards": 0, "fragments": 0, "motes": 0}
    junk_items = {}
    while_condition = False

    while True:
        items = input().lower()
        items = items.split(" ")


        for value, materials in zip(items[0::2], items[1::2]):
            materials = materials.lower()
            value = int(value)

            if materials in ["shards", "fragments", "motes"]:
                if materials not in legendary_items_dict:
                    legendary_items_dict[materials] = value

                else:
                    legendary_items_dict[materials] += value

                if legendary_items_dict[materials] >= 250:
                    legendary_items_dict[materials] -= 250
                    special_item = ""
                    if materials == "shards":
                        special_item = "Shadowmourne"
                    elif materials == "fragments":
                        special_item = "Valanyr"
                    elif materials == "motes":
                        special_item = "Dragonwrath"

                    print_func(legendary_items_dict, junk_items, special_item)
                    while_condition = True

            else:
                if materials not in junk_items:
                    junk_items[materials] = value
                else:
                    junk_items[materials] += value

            if while_condition:
                break

        if while_condition:
            break










legendary_farming()