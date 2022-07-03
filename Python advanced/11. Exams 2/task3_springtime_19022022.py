def start_spring(**kwargs):
    types_dict = {}
    result = ""

    for key, value in kwargs.items():
        if value not in types_dict:
            types_dict[value] = []
        types_dict[value].append(key)

    sorted_elements = sorted(types_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for element in sorted_elements:
        type = element[0]
        item = element[1]
        sorted_items = sorted(item)
        result += f'{type}:\n'
        for item in sorted_items:
            result += f'-{item}\n'

    return result.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


