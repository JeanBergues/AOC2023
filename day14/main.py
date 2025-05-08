import numpy as np

def main_a(puzzle_input):
    total = 0

    platform = np.array(list(map(list, puzzle_input.read().splitlines())))
    for x in range(platform.shape[1]):
        for y in range(platform.shape[0]):
            if platform[y, x] != 'O':
                continue
            platform[y, x] = '.'
            new_pos = raycast(x, y, platform)
            platform[new_pos[1], new_pos[0]] = 'O'
            total += platform.shape[0] - new_pos[1]

    return total


def raycast(x, y, platform, d = (0, -1)):
    prev_step = (x, y)
    while True:
        next_step = (prev_step[0] + d[0], prev_step[1] + d[1])
        if next_step[0] < 0 or next_step[0] >= platform.shape[1]:
            return prev_step
        if next_step[1] < 0 or next_step[1] >= platform.shape[0]:
            return prev_step
        if platform[next_step[1], next_step[0]] != '.':
            return prev_step
        prev_step = next_step


def process_cycle(platform):
    total = 0
    for d in [(0, -1), (-1, 0)]:
        for x in range(platform.shape[1]):
            for y in range(platform.shape[0]):
                if platform[y, x] != 'O':
                    continue
                platform[y, x] = '.'
                new_pos = raycast(x, y, platform, d)
                platform[new_pos[1], new_pos[0]] = 'O'
    
    count = False
    for d in [(0, 1), (1, 0)]:
        if d == (1, 0): count = True
        for x in range(platform.shape[1] - 1, -1, -1):
            for y in range(platform.shape[0] - 1, -1, -1):
                if platform[y, x] != 'O':
                    continue
                platform[y, x] = '.'
                new_pos = raycast(x, y, platform, d)
                platform[new_pos[1], new_pos[0]] = 'O'
                if count: total += platform.shape[0] - new_pos[1]

    return (platform, total)


def main_b(puzzle_input):
    total = 0

    # platform = np.array(list(map(list, puzzle_input.read().splitlines())))

    # # Warm up iterations
    # for i in range(200):
    #     platform, t = process_cycle(platform)

    # for i in range(50):
    #     platform, t = process_cycle(platform)
    #     print(t)

    print((1000000000 - 201) % 26)

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))

# After 201 cycles: Score 90940
# Repeats every 26