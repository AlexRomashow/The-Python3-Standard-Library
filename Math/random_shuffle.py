import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

def new_deck():
    return [
        # Всегда использовать для значения две позиции, чтобы
        # обеспечить одинаковую ширину строк
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS), SUITS,)]

def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()

# Создать новую колоду c упорядоченным расположением карт
deck = new_deck()
print('Initial deck:')
show_deck(deck)

# Перетасовать колоду c помощью функции shuffle()
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)

# Раздать карты на 4 руки по 5 карт на каждую руку
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# Показать раздачу
print('\nHands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()

# Показать карты в оставшейся части колоды
print('\nRemaining deck:')
show_deck(deck)
