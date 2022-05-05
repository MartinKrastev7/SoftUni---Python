def additional_func(partition):
    current_max_num = 0
    special_char = ""

    for ch in partition:
        if ch != special_char:
            if current_max_num >= 6:
                break
            current_max_num = 1
            special_char = ch
        else:
            current_max_num += 1

    return [current_max_num, special_char]


def ticket_validator(ticket):
    ticket_condition = ""

    if len(ticket) != 20:
        ticket_condition = "invalid ticket"

    elif ticket[0] * 20 == ticket and ticket[0] in "@#$^":
        ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'

    else:
        data_source = ""
        if additional_func(ticket[0:int(len(ticket) /2)]) > additional_func(ticket[int(len(ticket) / 2):]):
            data_source = additional_func(ticket[int(len(ticket) / 2):])
        else:
            data_source = additional_func(ticket[0:int(len(ticket) / 2)])

        number_of_special_sings = data_source[0]
        special_signs = data_source[1]

        if number_of_special_sings < 6 or special_signs not in "@#$^":
            ticket_condition = f'ticket "{ticket}" - no match'
        else:
            ticket_condition = f'ticket "{ticket}" - {number_of_special_sings}{special_signs}'


    return ticket_condition



def winning_ticket(data):

    for ticket in data:
       print(ticket_validator(ticket))


tickets_info = input()
data = [x.strip() for x in tickets_info.split(",")]
winning_ticket(data)

#vtori nachin
tickets = input().replace(" ", "")
tickets = tickets.split(',')
count = 0
symb = ''


def check_next(symbol, first, second):
    back = 6
    for i in range(7, 11):
        if (i * symbol) in first and (i * symbol) in second:
            back += 1
    return back


for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    left = ticket[0:int(len(ticket) / 2)]
    right = ticket[int(len(ticket) / 2):]
    if (6 * '@') in left and (6 * '@') in right:
        count = check_next('@', left, right)
        symb = '@'
    elif (6 * '$') in left and (6 * '$') in right:
        count = check_next('$', left, right)
        symb = '$'
    elif (6 * '#') in left and (6 * '#') in right:
        count = check_next('#', left, right)
        symb = '#'
    elif (6 * '^') in left and (6 * '^') in right:
        count = check_next('^', left, right)
        symb = '^'
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    if count != 10:
        print(f'ticket "{ticket}" - {count}{symb}')
    else:
        print(f'ticket "{ticket}" - {count}{symb} Jackpot!')