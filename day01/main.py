def main_a(puzzle_input):
    total = 0
    for line in puzzle_input:
        digit = 0

        # Find first digit
        for c in line:
            if c.isnumeric(): 
                digit += 10 * int(c)
                break
        
        # Find last digit
        for c in reversed(line):
            if c.isnumeric(): 
                digit += int(c)
                break

        total += digit

    return total


def main_b(puzzle_input):
    return 0


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))