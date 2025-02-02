import math

def abc_solver(a, b, c):
    x1 = (-1 * b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-1 * b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    return (x1, x2)


def main_a(puzzle_input):
    total = 1

    times = list(map(int, puzzle_input.readline().split(':')[1].split()))
    distances = list(map(int, puzzle_input.readline().split(':')[1].split()))

    for time, distance in zip(times, distances):
        t1, t2 = abc_solver(-1, time, -1 * distance)
        total *= math.floor(t2 - 1e-9) - math.ceil(t1 + 1e-9) + 1

    return total


def main_b(puzzle_input):
    time = int(puzzle_input.readline().split(':')[1].replace(' ', ''))
    distance = int(puzzle_input.readline().split(':')[1].replace(' ', ''))
    t1, t2 = abc_solver(-1, time, -1 * distance)

    return math.floor(t2 - 1e-9) - math.ceil(t1 + 1e-9) + 1


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))