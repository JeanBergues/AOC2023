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
    total = 0
    number_names = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    for line in puzzle_input:
        first_numeric_digit, last_numeric_digit = -1, -1
        text_before_digit, text_after_digit = "", ""
        # Find first digit
        for i, c in enumerate(line):
            if c.isnumeric(): 
                first_numeric_digit = int(c)
                text_before_digit = line[:i]
                break
        
        # Find last digit
        for i in reversed(range(len(line))):
            if line[i].isnumeric(): 
                last_numeric_digit = int(line[i])
                text_after_digit = line[i+1:]
                break

        if first_numeric_digit == -1:
            text_before_digit = line
            text_after_digit = line

        lowest_left_index = 100_000_000
        highest_right_index = -2
        for digit_name in number_names:
            left_i = text_before_digit.find(digit_name)
            if 0 <= left_i < lowest_left_index:
                first_numeric_digit = number_names[digit_name]
                lowest_left_index = left_i
            
            right_i = text_after_digit.rfind(digit_name)
            if 0 <= right_i and highest_right_index < right_i:
                last_numeric_digit = number_names[digit_name]
                highest_right_index = right_i
    
        total += 10 * first_numeric_digit + last_numeric_digit
        print(line.strip())
        print(10 * first_numeric_digit + last_numeric_digit)
        # print(text_before_digit.strip(), text_after_digit.strip())

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))