from functools import cmp_to_key

def calculate_hand_strength(hand):
    card_counts = {}
    for card in hand:
        card_counts[card] = hand.count(card)

    match (len(card_counts), max(card_counts.values())):
        case (1, 5): return 6   # Five of a kind
        case (2, 4): return 5   # Four of a kind
        case (2, 3): return 4   # Full house
        case (3, 3): return 3   # Three of a kind
        case (3, 2): return 2   # Two pairs
        case (4, 2): return 1   # One pair
        case (5, 1): return 0   # High card


def calculate_hand_strength_b(hand):
    card_counts = {}
    J_count = 0
    for card in hand:
        if card != 'J':
            card_counts[card] = hand.count(card)
        else:
            J_count = hand.count(card)

    if J_count == 5: return 6
    
    match (len(card_counts), max(card_counts.values()) + J_count):
        case (1, 5): return 6   # Five of a kind
        case (2, 4): return 5   # Four of a kind
        case (2, 3): return 4   # Full house
        case (3, 3): return 3   # Three of a kind
        case (3, 2): return 2   # Two pairs
        case (4, 2): return 1   # One pair
        case (5, 1): return 0   # High card


def compare_cards(hand1, hand2, strenghts = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']):
    if hand1[2] > hand2[2]:
        return -1
    if hand1[2] < hand2[2]:
        return 1

    for c1, c2 in zip(hand1[0], hand2[0]):
        if strenghts.index(c1) < strenghts.index(c2):
            return -1
        if strenghts.index(c1) > strenghts.index(c2):
            return 1
        
    return 0


def compare_cards_b(hand1, hand2, strenghts = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']):
    if hand1[2] > hand2[2]:
        return -1
    if hand1[2] < hand2[2]:
        return 1

    for c1, c2 in zip(hand1[0], hand2[0]):
        if strenghts.index(c1) < strenghts.index(c2):
            return -1
        if strenghts.index(c1) > strenghts.index(c2):
            return 1
        
    return 0


def main_a(puzzle_input):
    total = 0
    card_list = []

    for line in puzzle_input:
        split_line = line.split()
        hand, bid = split_line[0], int(split_line[1])
        card_list.append((hand, bid, calculate_hand_strength(hand)))

    card_list.sort(key=cmp_to_key(compare_cards), reverse=True)
    for i, card in enumerate(card_list):
        total += (i + 1) * card[1]

    return total


def main_b(puzzle_input):
    total = 0
    card_list = []

    for line in puzzle_input:
        split_line = line.split()
        hand, bid = split_line[0], int(split_line[1])
        card_list.append((hand, bid, calculate_hand_strength_b(hand)))

    card_list.sort(key=cmp_to_key(compare_cards_b), reverse=True)
    for i, card in enumerate(card_list):
        total += (i + 1) * card[1]

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))