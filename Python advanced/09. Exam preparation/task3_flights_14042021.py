def flights(*args):
    flights_dict = {}
    for i in range(0, len(args), 2):
        destination = args[i]

        if destination == "Finish":
            break
        passangers = int(args[i + 1])

        if destination not in flights_dict:
            flights_dict[destination] = passangers
        else:
            flights_dict[destination] += passangers

    return flights_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))