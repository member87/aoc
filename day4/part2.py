# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
#
#     Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
#     Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
#     Your copy of card 2 also wins one copy each of cards 3 and 4.
#     Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
#     Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
#     Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
#     Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
#
# Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

import numpy as np

card_count = {}

with open('input.txt') as f:
    count = 0
    for line in f.readlines():
        [card_num, cards] = line[:-1].split(': ')
        [win, have] = (cards.split('|'))
        print(card_num)
        card_num = card_num.split()[1]
        win = list(filter(None, win.split(' ')))
        have = list(filter(None, have.split(' ')))
        intersect = np.intersect1d(win, have)
        count = len(intersect)

        
        print('CARDS ' + card_num + ': ' + str(count) + ' matching numbers')
        card_count[str(card_num)] = card_count.get(str(card_num), 0) + 1
        for x in range(card_count.get(str(card_num), 0)):
            for i in range(count):
                card_count[str(i + int(card_num) + 1)] = (card_count.get(str(i + int(card_num) + 1), 0) + 1)
    print(sum(card_count.values()))
