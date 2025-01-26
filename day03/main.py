def main_a(puzzle_input):
    total = 0
    schematic = list(puzzle_input.read().splitlines())
    x_bound, y_bound = len(schematic[0]), len(schematic)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    current_number = 0
    connected_to_symbol = False

    for y in range(y_bound):
        for x in range(x_bound):
            if not schematic[y][x].isnumeric() or x == 0:
                if connected_to_symbol:
                    total += current_number
                    # print(current_number)

                current_number = 0
                connected_to_symbol = False
                if not schematic[y][x].isnumeric(): continue

            current_number = 10 * current_number + int(schematic[y][x])
            for direction in directions:
                search_x, search_y = x + direction[0], y + direction[1]
                if 0 <= search_x < x_bound and 0 <= search_y < y_bound:
                    search_char = schematic[search_y][search_x]
                    if search_char != '.' and not search_char.isnumeric():
                        connected_to_symbol = True

    return total


def main_b(puzzle_input):
    total = 0
    schematic = list(puzzle_input.read().splitlines())
    x_bound, y_bound = len(schematic[0]), len(schematic)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    current_number = 0
    recent_star = (-1, -1)
    star_connections = {}

    for y in range(y_bound):
        for x in range(x_bound):
            if not schematic[y][x].isnumeric() or x == 0:
                if recent_star != (-1, -1):
                    star_connections[recent_star] = star_connections.get(recent_star, []) + [current_number]

                current_number = 0
                recent_star = (-1, -1)
                if not schematic[y][x].isnumeric(): continue

            current_number = 10 * current_number + int(schematic[y][x])
            for direction in directions:
                search_x, search_y = x + direction[0], y + direction[1]
                if 0 <= search_x < x_bound and 0 <= search_y < y_bound:
                    search_char = schematic[search_y][search_x]
                    if search_char == '*':
                        recent_star = (search_x, search_y)
            
    for gears in star_connections.values():
        if len(gears) == 2:
            total += gears[0] * gears[1]

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))