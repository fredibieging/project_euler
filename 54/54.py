#!/usr/bin/python

f = open("hands.txt", "r")
sequence = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def get_suit(card):
    return card[1]

def get_symbol(card):
    return card[0]

def get_value(card):
    return sequence.index(card[0]) + 2

def n_of_kind(hand):
    kinds = sorted([get_symbol(card) for card in hand])
    max_count = 0
    for x in range(4):
        count = 0
        for y in range(x + 1, 5):
            if kinds[x] == kinds[y]:
                count += 1
        if count > max_count:
            max_count = count
    return max_count + 1

def royal_flush(hand):
    return straight_flush(hand) and get_symbol(high_card(hand)) == 'A'

def straight_flush(hand):
    return straight(hand) and flush(hand)

def four_of_kind(hand):
    return n_of_kind(hand) == 4

def full_house(hand):
    return three_of_kind(hand) and one_pair(hand)

def flush(hand):
    suits = [get_suit(card) for card in hand]
    return len(set(suits)) == 1

def straight(hand):
    values = sorted([get_value(card) for card in hand])
    highest_value = get_value(high_card(hand))
    expected = sorted(range(highest_value, 1, -1))[-5:]
    return expected == values

def three_of_kind(hand):
    return n_of_kind(hand) == 3

def two_pairs(hand):
    kinds = sorted([get_symbol(card) for card in hand])
    if kinds[1] == kinds[2] and kinds[3] == kinds[4]:
        return True
    if kinds[0] == kinds[1] and kinds[3] == kinds[4]:
        return True
    if kinds[0] == kinds[1] and kinds[2] == kinds[3]:
        return True
    return False

def one_pair(hand):
    return n_of_kind(hand) == 2

def high_card(hand):
    highest = 0
    high_card = ''
    for card in hand:
        current_card = get_value(card)
        if current_card > highest:
            high_card = card
            highest = current_card
    return high_card

def remove_high(hand):
    high = high_card(hand)
    return remove_card(hand, high)

def remove_card(hand, card):
    hand.remove(card) 
    return hand

def high_pair_value(hand):
    symbols = sorted([get_symbol(card) for card in hand])
    return get_value([s for s in symbols if symbols.count(s) == 2][0] + 'H') 

def rank_hand(hand):
    if royal_flush(hand):
        return 900
    elif straight_flush(hand):
        return 800
    elif four_of_kind(hand):
        return 700
    elif full_house(hand):
        return 600
    elif flush(hand):
        return 500
    elif straight(hand):
        return 400
    elif three_of_kind(hand):
        return 300
    elif two_pairs(hand):
        return 200
    elif one_pair(hand):
        return 100
    else: 
        return get_value(high_card(hand))

hands = f.readline()
p1wins = 0
while hands:
    cards = hands.split()
    p1 = cards[:5]
    p2 = cards[5:] 
    rp1 = rank_hand(p1)
    rp2 = rank_hand(p2)
    while rp1 == rp2:
        if rp1 < 100:
            p1 = remove_high(p1)
            p2 = remove_high(p2)
            rp1 = get_value(high_card(p1))
            rp2 = get_value(high_card(p2))
        elif rp1 == 100:
            rp1 += high_pair_value(p1)
            rp2 += high_pair_value(p2)
        elif rp1 > 100 and rp1 < 200:
            rp1 += get_value(high_card(p1))
            rp2 += get_value(high_card(p2))
            p1 = remove_high(p1)
            p2 = remove_high(p2)
    if rp1 > rp2:
        p1wins += 1
    hands = f.readline()
print p1wins
