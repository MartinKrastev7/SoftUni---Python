def words_sorting(*args):
    words_dict = {}
    sum_of_all = 0
    sorted_words = []
    for word in args:
        if word not in words_dict:
            words_dict[word] = 0
        sum_of_letters = 0
        for i in word:
            sum_of_letters += ord(i)
        words_dict[word] = sum_of_letters
        sum_of_all += sum_of_letters

    if sum_of_all % 2 == 0:
        sorted_key = sorted(words_dict.items())
        for i in sorted_key:
            sorted_words.append(f"{i[0]} - {i[1]}")
    else:
        sorted_values = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
        for i in sorted_values:
            sorted_words.append(f"{i[0]} - {i[1]}")

    return "\n".join(sorted_words)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

