def main_a(puzzle_input):
    total = 0
    strings = puzzle_input.read().split(',')
    for s in strings:
        total += HASH(s)

    return total


def HASH(s):
    cval = 0
    for c in s:
        cval += ord(c)
        cval *= 17
        cval %= 256
    return cval


def main_b(puzzle_input):
    total = 0
    boxes = {x: {} for x in range(256)}

    commands = puzzle_input.read().split(',')
    for command in commands:
        if command[-1] == '-':
            label = command[:-1]
            lens = 0
        else:
            label = command[:-2]
            lens = int(command[-1])
        box = HASH(label)
        
        if lens == 0:
            if label in boxes[box].keys():
                del boxes[box][label]
        else:
            boxes[box][label] = lens
        
    for box_number in boxes:
        for i, (k, v) in enumerate(boxes[box_number].items()):
            total += (1 + box_number) * (i + 1) * v

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))