cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)


for i in range(0, shuffle):
    list = []
    for p in range(0, mid):
        list.append(cards[p])
        list.append(cards[mid])
        mid += 1
    cards = list
    mid = int(length / 2)

print(list)

# vtoro reshenie
string = input()
shuffles = int(input())
string_list = string.split()
shuffled_list = []
length = int(len(string_list) / 2)

for n in range(shuffles):
    first_half = string_list[:length]
    second_half = string_list[length:]
    for item in range(len(first_half)):
        shuffled_list.append(first_half[item])
        shuffled_list.append(second_half[item])
    string_list = shuffled_list
    shuffled_list = []

print(string_list)

# treti nachin sus zip
card_deck = input()
shuffles = int(input())
shuffled_deck = card_deck.split(" ")
for i in range(shuffles):
    deck_1 = shuffled_deck[:len(shuffled_deck) // 2]
    deck_2 = shuffled_deck[len(shuffled_deck) // 2:]
    shuffled_deck = [cards for cards in zip(deck_1, deck_2) for cards in cards]
print(shuffled_deck)