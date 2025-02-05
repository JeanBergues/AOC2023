def find_next_value(numbers):
    if numbers == [0] * len(numbers):
        return 0
    
    diff_numbers = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    return numbers[-1] + find_next_value(diff_numbers)


def find_prev_value(numbers):
    if numbers == [0] * len(numbers):
        return 0
    
    diff_numbers = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    return numbers[0] - find_prev_value(diff_numbers)


def main_a(puzzle_input):
    total = 0

    for line in puzzle_input:
        numbers = list(map(int, line.strip().split()))
        total += find_next_value(numbers)

    return total


def main_b(puzzle_input):
    total = 0

    for line in puzzle_input:
        numbers = list(map(int, line.strip().split()))
        total += find_prev_value(numbers)

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))