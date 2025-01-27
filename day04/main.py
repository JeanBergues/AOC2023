def main_a(puzzle_input):
    total = 0
    
    for line in puzzle_input:
        winning_numbers, card_numbers = [c.strip().split() for c in line.split(':')[1].split('|')]
        matches = 0
        for number in winning_numbers:
            if number in card_numbers: matches += 1
        
        if matches > 0: total += 2 ** (matches - 1)

    return total


class Scratchcard:
    def __init__(self, n, winning_numbers, card_numbers):
        self.n = n
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
    
    def calculate_card_matches(self):
        matches = 0
        for number in self.winning_numbers:
            if number in self.card_numbers: 
                matches += 1

        return [self.n + i + 1 for i in range(matches)]

def main_b(puzzle_input):
    total = 0
    card_dict = {}
    card_totals = {}

    for i, line in enumerate(puzzle_input):
        winning_numbers, card_numbers = [c.strip().split() for c in line.split(':')[1].split('|')]
        card_dict[i+1] = Scratchcard(i+1, winning_numbers, card_numbers)
        card_totals[i+1] = 1

    for n, card in card_dict.items():
        cards_won = card.calculate_card_matches()

        for c in cards_won:
            if c in card_totals:
                card_totals[c] = card_totals[c] + card_totals[n]

    for i in card_totals.values():
        total += i
    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))