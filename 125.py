card_deck = []
card_value = ['J', 'Q', 'K', 'A']


def createDesk():
    for i in range(2, 11):
        card_deck.append(str(i) + 's')
        card_deck.append(str(i) + 'h')
        card_deck.append(str(i) + 'd')
        card_deck.append(str(i) + 'c')

    for s in card_value:
        card_deck.append(s + 's')
        card_deck.append(s + 'h')
        card_deck.append(s + 'd')
        card_deck.append(s + 'c')
    return card_deck


print(createDesk())


def shuffle(cards):
    for i in range(len(cards)):
        pass


shuffle(card_deck)
