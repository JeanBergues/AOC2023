def main_a(puzzle_input):
    total = 0

    cosmos = list(puzzle_input.read().splitlines())
    empty_row_indexes, empty_column_indexes = [], []

    # Find the empty rows
    for i, row in enumerate(cosmos):
        if '#' not in row:
            empty_row_indexes.append(i)

    # Find the empty columns
    for i in range(len(cosmos[0])):
        if '#' not in [r[i] for r in cosmos]:
            empty_column_indexes.append(i)

    # Find all galaxies
    galaxies = []
    for x in range(len(cosmos[0])):
        for y in range(len(cosmos)):
            if cosmos[y][x] == '#': galaxies.append((x, y))

    # Calculate total distances
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]

            crossed_empty_columns = len([x for x in empty_column_indexes if min(g1[0], g2[0]) < x < max(g1[0], g2[0])])
            crossed_empty_rows = len([y for y in empty_row_indexes if min(g1[1], g2[1]) < y < max(g1[1], g2[1])])
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + crossed_empty_columns + crossed_empty_rows

    return total


def main_b(puzzle_input):
    total = 0
    f = 999999

    cosmos = list(puzzle_input.read().splitlines())
    empty_row_indexes, empty_column_indexes = [], []

    # Find the empty rows
    for i, row in enumerate(cosmos):
        if '#' not in row:
            empty_row_indexes.append(i)

    # Find the empty columns
    for i in range(len(cosmos[0])):
        if '#' not in [r[i] for r in cosmos]:
            empty_column_indexes.append(i)

    # Find all galaxies
    galaxies = []
    for x in range(len(cosmos[0])):
        for y in range(len(cosmos)):
            if cosmos[y][x] == '#': galaxies.append((x, y))

    # Calculate total distances
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]

            crossed_empty_columns = len([x for x in empty_column_indexes if min(g1[0], g2[0]) < x < max(g1[0], g2[0])])
            crossed_empty_rows = len([y for y in empty_row_indexes if min(g1[1], g2[1]) < y < max(g1[1], g2[1])])
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + crossed_empty_columns * f + crossed_empty_rows * f

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))