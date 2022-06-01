def sorting_cheeses(**kwargs):
    """
    this function sorts the cheeses by its quantity descending then by its name ascending
    Concats the string with the result and sorts the elements of the result quantity descending for each
    cheese
    """
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for name, quantities in sorted_cheeses:
        result += name + "\n"
        sorted_quantities = sorted(quantities, reverse=True)
        result += "\n".join([str(el) for el in sorted_quantities]) + "\n"
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

#vtori nachin
def sorting_cheeses(**kwargs):
    print(kwargs)
    sorted_cheeses = sorted(
        kwargs.items(),
        key= lambda x: (-len(x[1]), x[0]),
    )
    result = []
    for name, pieces_count in sorted_cheeses:
        result.append(name)
        result.extend(pieces_count) # ili samo tova vmesto dolniq for
        for piece_count in pieces_count:
            result.append(sorted(piece_count,reverse=True))

    return "\n".join([str(x) for x in result])